# Báo cáo cải thiện nhận diện giọng nói tiếng Việt

Ngày cập nhật: 17/09/2026

> Cập nhật mới: khi có `GROQ_API_KEY`, backend mặc định chuyển sang Groq
> `whisper-large-v3` cho cả Việt/Anh/Trung. Đây là model Groq khuyến nghị khi
> ưu tiên độ chính xác. PhoWhisper-medium và Whisper Turbo bên dưới vẫn được
> giữ làm fallback local; các số đo cũ trong báo cáo là baseline của fallback.

## 1. Mục tiêu

Các thay đổi trong đợt này tập trung xử lý ba vấn đề quan sát được khi dùng app cho cuộc họp:

1. Whisper Turbo tạo transcript giả từ tiếng ồn, điển hình là các câu quảng bá như “Cảm ơn các bạn đã theo dõi”, “đăng ký kênh” và “để không bỏ lỡ những video hấp dẫn”.
2. Câu ngắn, nhỏ như “Khảo sát chưa…” có thể bị bỏ hoặc nhận sai.
3. Transcript và bản tóm tắt cần giữ được các số liệu, quyết định, người phụ trách và thời hạn của cuộc họp.

## 2. Kết quả hiện tại

- Khi đã cấu hình API key, Việt/Anh/Trung dùng **Groq Whisper Large V3**.
- Khi thiếu API key, tiếng Việt dùng **PhoWhisper-medium** MLX float16 và Anh/Trung dùng `mlx-community/whisper-turbo`.
- Màn hình Cài đặt hiển thị backend và model ASR đang chạy thực tế.
- Bộ test pipeline hiện đạt **21/21**.
- Bài test meeting thu được các thông tin trọng yếu:
  - “khảo sát chưa hoàn tất”;
  - “tám mươi sáu trên một trăm hai mươi phản hồi”;
  - “chị Mai hoàn thiện báo cáo trước thứ Sáu”.
- Checkpoint tải lỗi 3.167.560.219 byte đã được xoá. Máy hiện chỉ giữ checkpoint nguồn hợp lệ và model MLX cần cho app.

## 3. Thay đổi model và cơ chế tích hợp

### 3.1. Tách model theo ngôn ngữ

Backend hiện nạp hai model riêng:

| Ngôn ngữ | Model |
| --- | --- |
| Tiếng Việt | `.cache/models/phowhisper-medium-mlx` |
| Tiếng Trung | `mlx-community/whisper-turbo` |

Worker kiểm tra cả `config.json` và `weights.safetensors` trước khi bật PhoWhisper. Nếu PhoWhisper chưa hoàn chỉnh, app vẫn chạy và fallback sang Whisper Turbo với trạng thái cảnh báo rõ ràng.

Hai model được warm-up trước khi app báo sẵn sàng. Khi đổi ngôn ngữ, backend chọn đúng model đã nạp thay vì tải lại từ đầu.

### 3.2. Cài đặt PhoWhisper an toàn hơn

Installer được thay đổi để:

- ghim đúng revision `55a7e3eb6c906de891f8f06a107754427dd3be79` của `vinai/PhoWhisper-medium`;
- kiểm tra kích thước checkpoint là `3.055.754.969` byte;
- kiểm tra SHA-256 là `699b8650035692ceb72db1d24c2879654e1cf9fa2d422a3bb14ac990b5141c59`;
- tải bằng Hugging Face Hub qua HTTP chuẩn và tắt Xet vì Xet bị treo trước byte đầu tiên trên máy thử nghiệm;
- bảo toàn file sai kích thước dưới tên `.invalid-*` thay vì tự động xoá dữ liệu;
- ghi weights qua file tạm rồi mới đổi tên, tránh để lại model MLX trông có vẻ hoàn chỉnh khi conversion thất bại;
- tương thích với `mlx-whisper 0.4.3` bằng cách loại `alignment_heads` khỏi phép so sánh trọng số. Đây là runtime buffer được MLX tự khởi tạo, không phải weight trong checkpoint Hugging Face.

Model sau chuyển đổi:

- `weights.safetensors`: 1.524.744.036 byte;
- định dạng: MLX float16;
- suy luận: Apple Silicon/Metal, không gửi âm thanh lên cloud.

## 4. Cải thiện phát hiện giọng nói và chống nhiễu

### 4.1. VAD thích nghi theo môi trường

VAD trước đây chủ yếu dựa trên một ngưỡng năng lượng cố định nên tiếng quạt, tiếng phòng hoặc microphone có gain lớn có thể liên tục kích hoạt ASR.

Pipeline mới:

1. Dùng 300 ms đầu để đo nền âm thanh.
2. Lấy percentile 30 của cửa sổ khởi động để tránh việc người dùng nói sớm làm mức nền tăng quá cao.
3. Dùng ngưỡng động `max(0.006, noise_floor × 1.6)`.
4. Cập nhật noise floor bằng EMA chậm khi đang ở frame yên lặng.
5. Trừ DC offset của từng frame trước khi đo RMS.
6. Yêu cầu ít nhất 60 ms liên tục vượt ngưỡng mới bắt đầu một đoạn thoại, giúp bỏ click bàn phím và glitch ngắn.
7. Giảm điều kiện tối thiểu xuống 8 voiced frames để vẫn giữ câu ngắn/nhỏ.
8. Kết thúc đoạn sau 500 ms im lặng; buộc commit ở 3,2 giây để giữ trải nghiệm realtime.

Đã thử tăng hard cut lên 4,8 giây để model có thêm ngữ cảnh. Cách này không sửa được từ đầu câu trong mẫu meeting, trong khi end-to-end latency tăng từ khoảng 5,4 lên 7,6 giây, nên thay đổi đã được hoàn tác về 3,2 giây.

### 4.2. Lọc kết quả decoder

Mỗi segment từ Whisper chỉ được giữ khi đồng thời đạt:

- `no_speech_prob < 0.6`;
- `avg_logprob > -1.0`;
- `compression_ratio < 2.4`.

Sau đó pipeline tiếp tục loại:

- output lặp bất thường;
- câu tiếng Việt dài không khả thi so với thời lượng âm thanh;
- các hallucination đã quan sát được như “Cảm ơn các bạn đã theo dõi”, nội dung “đăng ký/subscribe kênh”, “ủng hộ kênh”;
- fragment “Để không bỏ lỡ những video…” khi hallucination quảng bá bị chia sang hai ASR job;
- phần trùng ở đoạn overlap sau hard cut.

Ngữ cảnh decoder được giữ riêng cho âm thanh hệ thống và microphone. Vì vậy transcript của một nguồn không làm lệch nguồn còn lại.

## 5. Thay đổi và thử nghiệm prompt

### Trạng thái ban đầu

`initial_prompt` trước đây chỉ được dùng cho tiếng Trung. Tiếng Việt luôn chạy không prompt và không tái sử dụng transcript trước.

### Các phương án đã thử

1. **Prompt meeting dài**: “Biên bản cuộc họp bằng tiếng Việt: khảo sát, phản hồi, tiến độ, báo cáo…”
   - Có lúc sửa được câu ngắn.
   - Nhưng model có thể phát lại một phần prompt hoặc sinh thêm nội dung không có trong audio.
2. **Prompt meeting rút gọn, bỏ từ “báo cáo”**
   - Không giải quyết ổn định và tạo hallucination nặng hơn trên đoạn dài.
3. **Prompt một từ “Khảo sát.”**
   - Whisper coi prompt như nội dung đã nói trước đó, do đó có lần bỏ chính cụm “khảo sát” khỏi output.

### Quyết định cuối cùng

- `ASR_PROMPT_VI` vẫn được hỗ trợ để có thể cấu hình theo deployment, nhưng mặc định là chuỗi rỗng.
- Không hard-code một prompt dài vào mọi cuộc họp.
- Từ segment thứ hai, tối đa 120 ký tự transcript trước được dùng làm `initial_prompt` để giữ mạch hội thoại.
- `condition_on_previous_text=False` vẫn được giữ nhằm tránh vòng lặp/hallucination dây chuyền; app tự quản lý context ngắn và có kiểm soát.

## 6. Chuẩn hoá thuật ngữ meeting

PhoWhisper trên giọng tổng hợp Linh nhận cụm “khảo sát chưa hoàn tất” thành các biến thể ổn định như:

- “đảo sát chưa hoàn tất”;
- “báo sát chưa hoàn tất”;
- “điều kiểm soát chưa hoàn tất hiện tại nhóm…”.

Một lớp chuẩn hoá hẹp được thêm sau decoder:

- chỉ chạy cho tiếng Việt;
- chỉ sửa hai pattern đã quan sát;
- pattern “điều kiểm soát…” chỉ được sửa khi ngay sau đó là “hiện tại nhóm”, để không thay đổi câu hợp lệ “Điều kiểm soát chưa hoàn tất.” nói riêng lẻ;
- không sửa prose chung hoặc các từ gần giống ngoài ngữ cảnh trên.

Đây là post-correction có chủ đích, không phải bằng chứng rằng model gốc luôn nhận đúng từ “khảo”.

## 7. Kết quả đo

### 7.1. Mẫu tiếng Việt ngắn có sẵn

Audio: 3,2 giây, nội dung “Xin chào, đây là bài kiểm tra tiếng Việt.”

| Model | Transcript | Thời gian nạp | ASR |
| --- | --- | ---: | ---: |
| Whisper Turbo | `Xin chào, đây là bài kiểm tra tiếng Việt.` | 5.155 ms | 1.881 ms |
| PhoWhisper-medium | `xin chào đây là bài kiểm tra tiếng việt.` | 10.130 ms | 1.907 ms |

Hai model đều đúng nội dung. PhoWhisper viết hoa và dấu câu ít hơn; inference gần tương đương, nhưng warm-up chậm hơn.

### 7.2. Kịch bản meeting tổng hợp

Nội dung gốc:

> Khảo sát chưa hoàn tất. Hiện tại nhóm đã nhận được tám mươi sáu trên một trăm hai mươi phản hồi. Chị Mai hoàn thiện báo cáo trước thứ Sáu.

Whisper Turbo:

- segment đầu sinh “Cảm ơn các bạn đã theo dõi.” và bị bộ lọc loại;
- giữ được `86/120` ở segment sau;
- nhận “chị Mai” thành “chị May”;
- làm mất thông tin “khảo sát chưa hoàn tất”.

PhoWhisper sau pipeline cuối:

1. `khảo sát chưa hoàn tất hiện tại nhóm đã nhận được tài liệu.` — 2.355 ms ASR;
2. `được tám mươi sáu trên một trăm hai mươi phản hồi.` — 2.197 ms ASR;
3. `chị mai hoàn thiện báo cáo trước thứ sáu.` — 2.149 ms ASR.

Đánh giá:

- PhoWhisper giữ được cả trạng thái khảo sát, số liệu và action item; tốt hơn Turbo cho use case meeting này.
- Trung bình ASR khoảng 2,23 giây/segment 3,2 giây.
- End-to-end đo được khoảng 5,3–5,6 giây vì bao gồm thời gian gom audio.
- Vẫn còn từ sai “tài liệu” ở partial đầu. Segment kế tiếp phục hồi đúng `86/120`, nhưng transcript chưa đạt mức hoàn hảo.

### 7.3. Khởi động app đầy đủ

Log của app build cuối:

- Whisper Turbo tiếng Trung ready: 2.850 ms;
- PhoWhisper tiếng Việt ready: 11.080 ms;
- ZeroTTS ready: 5.762 ms;
- worker mở socket thành công và giao diện hiển thị PhoWhisper-medium.

## 8. Test tự động

Bộ `tests/test_pipeline.py` hiện có 21 test, bao phủ:

- silence;
- noise floor thích nghi;
- speech dài và hard cut có giới hạn;
- giới hạn segment cloud 10 giây;
- câu ngắn/nhỏ;
- fragmentation và overlap;
- output lặp;
- tốc độ nói phi thực tế;
- các hallucination quảng bá tiếng Việt;
- chuẩn hoá hẹp “khảo sát chưa…” và negative case;
- protocol socket;
- deduplication;
- chọn đúng model/ngôn ngữ;
- không publish hallucination đã biết;
- ánh xạ weight Hugging Face sang MLX;
- tách context system audio và microphone.
- payload WAV và tham số gọi Groq audio transcription.

Kết quả hiện tại: **21 test passed**. Tauri/Rust có thêm 2 test validation cho evidence và trạng thái unresolved.

## 9. Thay đổi liên quan đến meeting note

Ngoài ASR, app đã được cập nhật để:

- lưu toàn bộ lịch sử các bản tóm tắt realtime thay vì chỉ giữ bản cuối;
- thêm nút **Tóm tắt đoạn này** để người dùng chốt một đoạn quan trọng giữa cuộc họp;
- dùng cursor riêng cho tóm tắt tự động và thủ công;
- lưu các snapshot vào meeting note với thời gian và nhãn `THỦ CÔNG`/`TỰ ĐỘNG`;
- thêm demo “Review khảo sát người dùng” với transcript, số liệu, quyết định và action item tương ứng.

## 10. Hạn chế và bước tiếp theo

1. Đánh giá hiện tại dùng một file test có sẵn và giọng macOS Linh tổng hợp. Chưa có corpus giọng nói thật nhiều người, nhiều vùng miền và nhiều mức nhiễu.
2. Chưa có WER/CER định lượng trên tập dữ liệu gán nhãn. Kết luận hiện tại dựa trên regression test và so sánh transcript cụ thể.
3. Groq cần Internet, API key và chịu rate limit/chi phí. Fallback local vẫn có warm-up PhoWhisper khoảng 10–11 giây.
4. Post-correction “khảo sát chưa…” cố ý rất hẹp. Nếu có thêm thuật ngữ chuyên ngành, nên chuyển sang glossary có cấu hình và test positive/negative cho từng mục.
5. Nên thu ít nhất 20–50 đoạn họp thật gồm câu ngắn, nói nhỏ, ngắt quãng, nhiều speaker và noise để đo recall, false positive và latency percentile.

## 11. Các file chính đã thay đổi

- `asr/install_phowhisper.py`: tải, xác minh và chuyển đổi PhoWhisper.
- `asr/server.py`: Groq Whisper Large V3, fallback local, context decoder, filter và trạng thái model.
- `asr/audio_buffer.py`: adaptive VAD, lọc hallucination và chuẩn hoá thuật ngữ.
- `tests/test_pipeline.py`: regression test ASR.
- `src/hooks/useAppModel.ts`: trạng thái PhoWhisper, transcript và lịch sử tóm tắt.
- `src-tauri/src/lib.rs`: structured meeting summary và kiểm tra evidence.
- `src/pages/NotesPage.tsx`: meeting note, transcript và điều hướng evidence.
- `README.md`: hướng dẫn cấu hình Groq, fallback local và mô tả pipeline.

# VietNote — Báo cáo Acceptance Test chi tiết (v1.1)

## 1. Mục tiêu

Đánh giá VietNote trên luồng thực tế: nhận âm thanh → ASR → transcript → meeting summary. Mục tiêu là đo được **đã thử bao nhiêu câu, đúng bao nhiêu câu và sai ở đâu**, thay vì chỉ kết luận chung là “chạy tốt”.

## 2. Cấu hình và phạm vi chạy

| Hạng mục | Giá trị |
|---|---|
| Bộ câu | `tests/vietnote_acceptance_cases.json` v1.1-simple-language |
| Số case | 20 |
| Ngôn ngữ | Tiếng Việt, có chêm English phổ thông |
| Nguồn audio ghi nhận | System audio |
| Backend/model ASR | Chưa được export cùng kết quả — cần ghi ở lần chạy sau |
| Đầu ra được chấm | Transcript và final structured summary |
| Không đo được | p50/p95 latency, vì bản export không có log latency |

Lưu ý: VN17 yêu cầu kiểm tra tách Microphone/System audio. Phiên này toàn bộ transcript mang nhãn `System audio`, nên case đó không chứng minh được chức năng tách nguồn.

## 3. Quy tắc chấm

Một case được tính **ĐẠT** khi:

1. Transcript giữ đúng ý chính, số liệu, phủ định, owner, deadline và từ quan trọng.
2. Summary phân loại đúng: decision, tentative decision, unresolved, action item hoặc deferred.
3. Không bịa thông tin; các mục cần evidence phải trỏ được về segment đúng.

Các lỗi nghiêm trọng: đổi số/ngày, đảo phủ định, gán sai owner, biến câu chưa chốt thành quyết định (hoặc ngược lại), sai credential, hoặc không chứng minh được evidence/source theo yêu cầu case.

## 4. Kịch bản và kết quả từng case

| ID | Kịch bản | Kỳ vọng chính | Quan sát thực tế | Đánh giá |
|---|---|---|---|---|
| VN01 | Quyết định phát hành | Phát hành thứ Ba tuần sau | Transcript và decision giữ đúng | ĐẠT |
| VN02 | Số liệu phản hồi | 86/120, thiếu 34 | Giữ đúng cả hai số | ĐẠT |
| VN03 | Owner + deadline | Lan, báo cáo, trước 10h thứ Sáu | Action item giữ đúng | ĐẠT |
| VN04 | Chưa chốt A/B | Không chọn A hay B | Unresolved có A/B, `No final decision` | ĐẠT |
| VN05 | Câu hỏi mở | Chưa biết ai phê duyệt gia hạn | Unresolved, không tự bịa owner | ĐẠT |
| VN06 | Tech phổ thông | web app, API, database | Key points giữ đúng | ĐẠT |
| VN07 | English phổ thông | MVP nhỏ, test lại tuần sau | Summary giữ được ý thử lại; wording transcript chưa tự nhiên nhưng không đổi ý | ĐẠT |
| VN08 | Đề xuất ≠ quyết định | Microphone là đề xuất, chưa chốt | Được xếp tentative decision | ĐẠT |
| VN09 | Ba action item | Minh desktop; Huy microphone; Mai README | `README` thành `file with me` | TRƯỢT |
| VN10 | Đổi ngày review | 12 → 15/10/2026 | Decision giữ đúng ngày mới | ĐẠT |
| VN11 | Số + đơn vị | <800 ms; 1,2 giây | Transcript và summary giữ đúng | ĐẠT |
| VN12 | Phủ định | Không TTS; không gửi audio local | Giữ đúng hai phủ định | ĐẠT |
| VN13 | API key | Groq, `gsk`, không commit Git | `Groq/gsk` thành `gốc/jfk` | TRƯỢT · nghiêm trọng |
| VN14 | Chưa biết tính năng MVP | Tách lời từng người chưa chốt | Unresolved giữ đúng ý | ĐẠT |
| VN15 | Nhiễu và giờ bắt đầu | Bỏ nhiễu, giữ 9 giờ | Không hallucination; giữ 9 giờ | ĐẠT |
| VN16 | Câu ngắn/phủ định | Khảo sát chưa hoàn tất | Transcript lỗi chính tả `Hảo sát chưa hàn tất`, nhưng summary giữ đúng ý; chấp nhận theo chấm ngữ nghĩa | ĐẠT có lưu ý |
| VN17 | Tách nguồn audio | Mic: tiếng Việt; System: VietNote | Không có transcript Mic riêng; summary tự gán nguồn | TRƯỢT · chưa hợp lệ |
| VN18 | Deferred | Quý sau; không làm sprint này | `sprint` thành `screen` ở transcript và summary | TRƯỢT |
| VN19 | Decision + evidence | Decision về phạm vi; evidence timestamp | Bị đưa vào tentative; export không có evidence timestamp | TRƯỢT · nghiêm trọng |
| VN20 | Tổng kết nhiều ý | Lan/thứ Sáu; chưa chốt dữ liệu; 15/10/2026 | Giữ được ba ý chính trong TL;DR | ĐẠT |

## 5. Tổng hợp điểm

| Chỉ số | Kết quả |
|---|---:|
| Tổng case | 20 |
| Đạt | **15** |
| Trượt | **5** |
| Tỷ lệ đạt | **75%** |
| Lỗi nghiêm trọng | **2** (VN13, VN19) |
| Case chưa hợp lệ do setup | **1** (VN17) |
| Verdict theo ngưỡng dự án | **CHƯA ĐẠT** |

Ngưỡng dự án yêu cầu tối thiểu 16/20 **và không có lỗi nghiêm trọng**. Vì đạt 15/20, có 2 lỗi nghiêm trọng và 1 case chưa được test đúng nguồn audio, kết quả này không nên được báo là “đạt MVP hoàn toàn”.

## 6. Điểm tốt

- Nhận đúng dữ liệu định lượng và đơn vị quan trọng: `86/120`, `34`, `<800 ms`, `1,2 giây`.
- Phân biệt tốt quyết định, đề xuất và vấn đề chưa chốt trong phần lớn case.
- Action item cơ bản giữ đúng owner và deadline.
- Không xuất hiện hallucination quảng cáo dù có câu có tiếng quạt.
- Final summary gom được ý chính của cả phiên, đặc biệt VN01–VN12 và VN20.

## 7. Lỗi và nguyên nhân khả dĩ

| Ưu tiên | Lỗi | Ảnh hưởng | Hướng xử lý |
|---|---|---|---|
| P0 | `Groq/gsk` → `gốc/jfk` | Có thể làm cấu hình credential sai | Không đưa credential vào meeting note; dùng glossary cứng cho `Groq`, `gsk`, `API key`, đồng thời xác thực format `gsk_` ở UI. |
| P0 | Decision bị thành tentative và thiếu evidence | Meeting note không đáng tin để audit | Prompt/validator: từ “Quyết định” phải ưu tiên decision; không hiển thị item quan trọng nếu thiếu evidence ID/timestamp. |
| P1 | Mic/System không tách được | Không biết nguồn của câu nói | Chạy VN17 bằng `Both`; kiểm tra quyền capture và UI phải hiển thị source thật, không suy diễn. |
| P1 | `README` → `file with me` | Action item không thực thi được | Thêm `README` vào glossary; test tiếng Anh ngắn ở âm lượng/giọng khác nhau. |
| P2 | `sprint` → `screen` | Ý deferred bị lệch | Thêm cặp correction hẹp `screen này` → `sprint này` chỉ khi có ngữ cảnh kế hoạch/công việc; thêm regression test. |
| P2 | Lỗi chính tả câu ngắn | Giảm độ tin cậy transcript | Giữ raw text, glossary hẹp cho `khảo sát chưa hoàn tất`; đo lại với cả Mic và System. |

## 8. Kế hoạch test lại

1. Sửa P0 trước; không coi kết quả credential/evidence là chấp nhận được nếu chưa sửa.
2. Chạy lại VN09, VN13, VN18, VN19 bằng cùng nguồn System audio để xác nhận regression.
3. Chạy VN17 với Audio Input = `Both`: đọc câu Mic bằng microphone và phát câu System từ loa/app khác. Kiểm tra hai label tách biệt.
4. Chạy lại toàn bộ 20 câu, lưu `backend/model`, ngày, p50/p95 ASR latency, transcript và screenshot evidence timestamp.
5. Chỉ báo PASS khi ≥16/20, 0 lỗi P0 và VN17 có dữ liệu hợp lệ.

## 9. Câu trả lời dùng cho form

**Đã thử bao nhiêu lần?** 20 câu test trong một phiên System audio; cần thêm một phiên Both cho case tách nguồn.

**Trong đó bao nhiêu lần đạt?** 15/20 (75%).

**Chuẩn “đạt” của nhóm là gì?** Transcript đúng ý chính, số liệu, phủ định, owner và deadline; summary phân loại đúng; không bịa; các decision/action quan trọng có evidence timestamp đúng. Ngưỡng release: tối thiểu 16/20 và không có lỗi nghiêm trọng.

**Những lần chưa đạt sai ở đâu?** VN09 sai `README`; VN13 sai `Groq/gsk`; VN17 không có Mic source thực để kiểm chứng; VN18 sai `sprint`; VN19 xếp decision thành tentative và thiếu evidence timestamp.

**Link video thao tác 30 giây:** Cần người test cung cấp link Google Drive/YouTube public; report này không thể tự tạo hoặc suy ra link video.

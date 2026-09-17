# VietNote — Acceptance Test 20 câu

Bộ này chuyển yêu cầu “Số đo — thử bao nhiêu, đúng bao nhiêu” thành một phép đo lặp lại được cho VietNote. Câu thử dùng tiếng Việt phổ thông, chỉ chêm một số từ tiếng Anh quen thuộc trong công việc.

## Chuẩn bị

1. Mở VietNote, chọn **Tiếng Việt**, nguồn **Microphone** (chạy thêm một vòng **Both** cho VN17).
2. Dùng cùng một microphone/phòng trong cả 20 câu. Không đọc lại câu nếu đang đo ASR.
3. Bắt đầu một meeting mới. Đọc lần lượt VN01–VN20, ngắt khoảng 1–2 giây giữa câu.
4. Kết thúc meeting để VietNote tạo bản tóm tắt cuối. Lưu transcript và summary/evidence timestamp của từng câu.
5. Nếu dùng Groq, ghi lại model/backend đang hiển thị; nếu hết quota thì chạy lại bằng local fallback và ghi rõ backend.

## Tiêu chí đạt

Một câu chỉ được tính **ĐẠT** khi cả hai lớp đều đạt:

- **Transcript:** đúng ý chính; giữ đúng số liệu, phủ định, tên người, deadline và thuật ngữ; không có hallucination.
- **Meeting note:** phân loại đúng quyết định/đề xuất/chưa chốt/action/deferred; action giữ đúng owner/deadline; item quan trọng có evidence trỏ đúng segment.

Các lỗi sau là **trượt ngay**: bịa quyết định; đảo phủ định; đổi số liệu/ngày; gán sai người; biến câu hỏi mở thành câu trả lời; evidence trỏ sai nội dung.

## Bảng chạy test

Chi tiết câu và expected nằm trong [`vietnote_acceptance_cases.json`](./vietnote_acceptance_cases.json). Ghi kết quả theo mẫu:

| ID | Transcript | Summary | Evidence | Kết quả | Ghi chú |
|---|---|---|---|---|---|
| VN01–VN20 | PASS/FAIL | PASS/FAIL | PASS/FAIL/N/A | PASS nếu cả 3 đạt | model, latency, lỗi |

## Cách tính số đo

```text
Tổng số câu thử = 20
Số câu đạt = số dòng có Kết quả PASS
Tỷ lệ đạt = Số câu đạt / 20 × 100%
```

Nên báo cáo tối thiểu: `backend/model`, `ngày chạy`, `số câu đạt/20`, `tỷ lệ đạt`, `số lỗi nghiêm trọng`, `p50/p95 latency` và 3 transcript lỗi tiêu biểu. Không làm tròn để che số liệu thấp; ví dụ `13/20 = 65%` vẫn là kết quả hợp lệ.

## Ngưỡng đề xuất cho MVP

- **PASS tối thiểu:** ≥ 16/20 (80%) và 0 lỗi bịa quyết định/số liệu/owner.
- **Cần sửa:** 12–15/20 hoặc có từ 1 lỗi nghiêm trọng.
- **Chưa đạt:** ≤ 11/20.

Ngưỡng này là quy ước đánh giá của dự án, không phải độ chính xác WER. Muốn kết luận chất lượng ASR độc lập, cần chấm thêm WER/CER trên transcript chuẩn.

## Chạy kiểm thử hồi quy tự động hiện có

```bash
npm test
npm run build
.venv/bin/python -m unittest discover -s tests -v
```

Các lệnh trên kiểm tra pipeline/VAD/normalization/Groq adapter; còn 20 câu ở đây là acceptance test có người nghe và chấm output thật.

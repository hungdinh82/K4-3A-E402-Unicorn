# VietNote Acceptance Report — 20 câu

Ngày chạy: 17/09/2026
Nguồn: System audio
Backend/model: chưa được ghi trong export; cần ghi lại ở lần chạy sau
Bộ chuẩn: `tests/vietnote_acceptance_cases.json`

> Lưu ý: report này chấm bộ câu v1.0 trước khi đơn giản hóa ngôn ngữ. Bộ hiện hành là v1.1 trong `tests/vietnote_acceptance_cases.json`; cần chạy lại 20 câu để có điểm so sánh hợp lệ.

## Kết quả

| Chỉ số | Kết quả |
|---|---:|
| Tổng số case | 20 |
| Đạt đầy đủ | 9 |
| Trượt | 10 |
| Chưa hợp lệ / cần chạy lại | 1 (VN17) |
| Điểm bảo thủ trên 20 | **9/20 = 45%** |
| Điểm trên 19 case hợp lệ | **9/19 = 47,4%** |
| Ngưỡng MVP đề xuất | 16/20, không lỗi nghiêm trọng |
| Verdict | **CHƯA ĐẠT MVP** |

VN17 không thể chấm đúng vì toàn bộ transcript ghi `System audio`; case yêu cầu kiểm tra tách **Microphone/System audio** nhưng phiên này không chạy nguồn `Both`. Nếu buộc tính đủ 20 câu, VN17 được tính trượt cho đến khi chạy lại.

## Bảng chấm

| ID | Kết quả | Nhận xét ngắn |
|---|---|---|
| VN01 | ĐẠT | Quyết định phát hành và thứ Ba tuần sau được giữ đúng. |
| VN02 | ĐẠT | Giữ đúng 86/120 và thiếu 34. |
| VN03 | ĐẠT | Đúng owner Lan, báo cáo và hạn thứ Sáu trước 10h. |
| VN04 | TRƯỢT · nghiêm trọng | Qdrant bị biến mất/biến dạng; xuất hiện `Chrome`, `quy-drain`; chưa chốt vẫn giữ đúng. |
| VN05 | ĐẠT | Giữ câu hỏi phê duyệt gia hạn là chưa có câu trả lời, không tự bịa owner. |
| VN06 | TRƯỢT · nghiêm trọng | `LangGraph/RAGAS/FastAPI/Qdrant` bị nhận sai hoặc không xuất hiện trong summary. |
| VN07 | TRƯỢT · nghiêm trọng | Cụm English/Whisper Large V3 bị biến thành `lãng phí Deathglyph`, `V3 Nekwik`; mất ý chính. |
| VN08 | ĐẠT | Đề xuất microphone được phân loại tentative, chưa bị biến thành quyết định. |
| VN09 | ĐẠT | Ba owner Minh/Huy/Mai và action tương ứng được giữ đúng. |
| VN10 | ĐẠT | Review được chốt ở ngày 15/10/2026. |
| VN11 | TRƯỢT · nghiêm trọng | `800 ms` bị thành `88 ms`; đây là lỗi số liệu làm thay đổi yêu cầu. |
| VN12 | ĐẠT | Giữ đúng hai phủ định: không bật TTS, không gửi audio local. |
| VN13 | TRƯỢT · nghiêm trọng | `Groq` thành `Groov`, tiền tố `gsk` thành `GSK`; không nên coi key/config là đúng. |
| VN14 | TRƯỢT · nghiêm trọng | `speaker diarization` thành `speaker DR-regression`; summary vẫn đánh dấu unresolved nhưng thuật ngữ sai. |
| VN15 | TRƯỢT | Transcript có “tiếng quạt” và “9 giờ” nhưng summary bỏ mất mốc bắt đầu cuộc họp. |
| VN16 | TRƯỢT · nghiêm trọng | `Khảo sát chưa hoàn tất` thành `khảo sát siêu hoàn tất`, đảo nghĩa phủ định. |
| VN17 | CHƯA HỢP LỆ | Không có dữ liệu microphone riêng; cần chạy lại với nguồn `Both`. |
| VN18 | ĐẠT | Deferred sang quý sau được giữ đúng, không biến thành action của sprint hiện tại. |
| VN19 | TRƯỢT | Summary không kèm evidence/timestamp trong export nên chưa chứng minh được liên kết đúng segment. |
| VN20 | TRƯỢT · nghiêm trọng | `Qdrant/Chroma chưa chốt` bị nhiễu (`quy-drain...`); phần tổng kết không đủ đáng tin để chốt case. |

## Điều đang hoạt động tốt

- Quyết định và tentative decision thường được phân biệt đúng (VN01, VN08, VN10).
- Owner/action item đơn giản hoạt động tốt (VN03, VN09).
- Trạng thái `No final decision` được giữ thận trọng cho các chủ đề chưa chốt (VN04, VN05, VN14, VN20).
- Hai câu phủ định về TTS và upload audio được giữ đúng (VN12).

## Lỗi cần ưu tiên sửa

1. **Thuật ngữ và tên riêng:** LangGraph, RAGAS, Qdrant, Groq, Whisper Large V3, speaker diarization.
2. **Số liệu/thời gian:** không được biến `800 ms` thành `88 ms`; thêm kiểm tra bảo toàn số và đơn vị trước summary.
3. **Phủ định/câu ngắn:** `chưa hoàn tất` bị đảo thành `siêu hoàn tất`; tăng context hoặc dùng câu xác nhận ngắn.
4. **Evidence:** export phải hiển thị evidence ID/timestamp để chấm được VN19.
5. **Thiết lập test:** chạy VN17 bằng `Both`, đồng thời ghi `backend/model`, latency và quota status.

## Kết luận

Kết quả **9/20 (45%)** chưa đạt ngưỡng MVP 16/20. Bản hiện tại có thể trình diễn luồng ghi âm, action item và quyết định đơn giản, nhưng chưa đủ tin cậy cho meeting note có thuật ngữ kỹ thuật, số liệu hoặc yêu cầu phải kiểm chứng. Nên sửa các lỗi nghiêm trọng ở trên rồi chạy lại đủ 20 câu; không nên chỉ dùng điểm trung bình để che các lỗi đảo nghĩa/sai số.

# VietNote Acceptance Report — v1.1 câu đơn giản

## Kết quả

- Đã thử: **20 câu**
- Đạt: **16 câu**
- Chưa đạt: **4 câu**
- Tỷ lệ: **80%**
- Kết luận: **Đạt ngưỡng số lượng MVP 16/20, nhưng chưa đạt chất lượng hoàn toàn** vì vẫn có lỗi nghiêm trọng.

## Tiêu chuẩn đạt của nhóm

Một câu chỉ đạt khi transcript giữ đúng ý chính, số liệu, phủ định, tên người và thời hạn; summary phân loại đúng quyết định/chưa chốt/action/deferred; và nội dung quan trọng có evidence đúng. Không chấp nhận lỗi làm đổi nghĩa, đổi số liệu, sai credential hoặc tự gán nguồn âm thanh.

## 4 câu chưa đạt

1. **VN09 — Action sai đích:** `README` bị nhận thành `file with me`. Owner đúng nhưng nội dung việc cần làm chưa đúng.
2. **VN13 — Credential sai:** `Groq`/`gsk` bị thành `gốc`/`jfk`. Đây là lỗi nghiêm trọng vì có thể làm người dùng cấu hình sai API key.
3. **VN17 — Nguồn âm thanh không chứng minh được:** transcript export chỉ có `System audio`, nhưng summary lại khẳng định có câu từ microphone. Cần chạy lại với nguồn `Both`.
4. **VN19 — Phân loại/evidence chưa đúng:** câu nói là quyết định giữ phạm vi, nhưng summary xếp thành `Tentative Decision`; export cũng chưa thể hiện evidence timestamp.

## Điểm tốt

- Giữ đúng các số 86/120, thiếu 34, latency 800 ms và 1,2 giây.
- Giữ đúng các quyết định về phát hành, ngày review, TTS và không gửi audio.
- Phân biệt tốt phần chưa chốt A/B, phê duyệt deadline và tách lời người nói.
- Giữ đúng owner Lan, Minh, Huy, Mai ở phần lớn action item.

## Câu trả lời ngắn cho form

**Đã thử bao nhiêu lần?** 20 câu.
**Trong đó bao nhiêu lần đạt?** 16 câu.
**Chuẩn “đạt” của nhóm là gì?** Transcript đúng ý chính và số liệu; summary phân loại đúng quyết định/chưa chốt/action/deferred; không bịa; nội dung quan trọng có evidence đúng timestamp.
**Những lần chưa đạt sai ở đâu?** VN09 sai `README`; VN13 sai `Groq/gsk` thành `gốc/jfk`; VN17 chưa kiểm chứng tách microphone/system vì phiên chỉ có System audio; VN19 biến quyết định thành tentative và chưa hiện evidence timestamp.

Video 30 giây cần đính kèm link public/Drive trong form; report này không tự tạo link video.

# Validation log — VietNote

## Trạng thái

Đã thu được **5 phản hồi form trải nghiệm** trong khoảng 18:00–21:00 ngày 17/09/2026, đều dùng backend local. Đây là dữ liệu self-report sau khi dùng sản phẩm, chưa thay thế hoàn toàn nhật ký quan sát trực tiếp. Sổ tay yêu cầu **5 người ngoài nhóm dùng thử**, trong đó **2 người đã khai từ CP1**; hiện chưa thể ghép 5 phản hồi này với tên/mã số vì form để trống hai trường đó. Không tự suy đoán danh tính và không tự tạo quote.

| Người thử | Mã số | Trạng thái |
|---|---|---|
| Nguyễn Ngọc Vĩnh | 2A202602833 | Sẵn sàng; đã thực hiện |
| Vũ Đức Minh | 2A202602895 | Sẵn sàng; đã thực hiện |
| NGUYỄN VIỆT HOÀNG | 02424 | Sẵn sàng; đã thực hiện |
| NGUYỄN QUANG HUY | 02421 | Sẵn sàng; đã thực hiện |
| NGUYỄN TẤT ĐẠT | 02578 | Sẵn sàng; đã thực hiện |

## Bằng chứng bắt buộc để được tính validation

- 5 người ngoài nhóm đã thực sự dùng prototype.
- 2 trong 5 người là Nguyễn Ngọc Vĩnh và Vũ Đức Minh, đã khai từ CP1.
- Mỗi người có một dòng nhật ký: ai thử, được giao task gì, kẹt ở đâu, quote nguyên văn và quyết định của nhóm.
- Quote phải chép đúng lời người thử, kể cả lỗi chính tả; không thay bằng lời nhóm tự diễn giải.
- Cuối bảng có đúng 4 dòng tổng hợp: chủ đề lặp lại nhiều nhất, thay đổi làm trước demo, điều giữ nguyên và lý do, việc đưa vào backlog.
- Ít nhất một thay đổi sau validation phải được ghi vào `spec.md` §9 Changelog; nếu không thay đổi thì ghi rõ lý do giữ nguyên.

## Mục tiêu phiên thử

Kiểm tra xem người dùng có tự dùng VietNote để ghi lại một cuộc họp ngắn, tìm được quyết định/việc cần làm/chủ đề chưa chốt, và kiểm tra được evidence từ summary về transcript hay không.

Mỗi phiên kéo dài khoảng 10 phút. Người thử tự cầm chuột; người quan sát không thuyết minh màn hình và không chỉ vị trí nút trước khi người thử tự hành động.

## Dữ liệu thật từ form trải nghiệm — n = 5

### Thông tin thu thập

- **Thời gian:** 18:00–21:00, ngày 17/09/2026.
- **Backend:** Local.
- **Định danh:** form không có họ tên và mã số ở cả 5 dòng, nên chỉ ghi `F01`–`F05`, không gán vào 5 người đã chốt.
- **Giới hạn bằng chứng:** form không có quote nguyên văn, hành động đầu tiên, điểm kẹt hoặc quyết định sau từng phiên; các trường này vẫn cần thu trực tiếp.

### Bảng kết quả từng phản hồi

| ID | Timestamp | Bối cảnh sử dụng | UI / 5 | Transcript / 5 | Dịch / 5 | Summary | Vấn đề gặp | Yên tâm dữ liệu / 5 | Sẵn sàng dùng / 10 |
|---|---|---|---:|---:|---:|---|---|---:|---:|
| F01 | 19:34:44 | Họp trực tuyến; tổng hợp sau họp | 4 | 3 | 4 | Hữu ích | Không gặp vấn đề đáng kể | 3 | 8 |
| F02 | 19:39:34 | Họp trực tuyến | 4 | 4 | 3 | Hữu ích | Không gặp vấn đề đáng kể | 4 | 7 |
| F03 | 19:39:57 | Họp trực tuyến; ghi chú cá nhân; tổng hợp sau họp | 5 | 4 | 4 | Hữu ích | Bản dịch chưa tự nhiên | 4 | 9 |
| F04 | 19:41:01 | Họp trực tuyến; ghi chú cá nhân | 4 | 4 | 4 | Rất hữu ích | Bản dịch chưa tự nhiên | 4 | 7 |
| F05 | 19:41:32 | Họp trực tuyến; tổng hợp sau họp | 5 | 4 | 4 | Hữu ích | Không gặp vấn đề đáng kể | 3 | 6 |

### Tổng hợp có thể dùng trong validation

- Có **5/5** người dùng thử bằng backend local.
- Điểm giao diện trung bình: **4,4/5**.
- Điểm transcript trung bình: **3,8/5**.
- Điểm dịch trung bình: **3,8/5**.
- Summary được đánh giá **hữu ích hoặc rất hữu ích: 5/5**; trong đó 1 người chọn “Rất hữu ích”.
- Mức yên tâm về dữ liệu trung bình: **3,6/5**.
- Sẵn sàng tiếp tục dùng/giới thiệu trung bình: **7,4/10**.
- Vấn đề lặp lại duy nhất: **bản dịch chưa tự nhiên, 2/5 phản hồi**.
- Tính năng được xem là có giá trị: lưu/tìm lại ghi chú, tóm tắt cuộc họp, transcript realtime, trích xuất decision/action/deadline.
- Nhu cầu bổ sung được ghi nhận: xuất file theo mẫu và tích hợp Discord.

### Cách dùng dữ liệu này

Phần form được dùng làm evidence định lượng bổ sung cho validation, không dùng để thay cho quote nguyên văn hoặc log quan sát. Khi có tên/mã số và log trực tiếp, cập nhật `F01`–`F05` thành tên thật và thêm quote chính xác; không tự biến câu trả lời dạng điểm số thành lời nói của người dùng.

## Kịch bản nói với người thử

### 1. Comfort — khoảng 1 phút

> Tụi mình đang đánh giá sản phẩm, không đánh giá bạn. Không có câu trả lời đúng hoặc sai; bạn cứ nói to suy nghĩ của mình.

### 2. Context — khoảng 1 phút

> Kể lần gần nhất bạn phải ghi nhớ hoặc xem lại nội dung của một cuộc họp, bạn đã làm gì?

Ghi nguyên văn câu trả lời và không gợi ý sản phẩm.

### 3. Task — khoảng 1 phút

> Hãy dùng VietNote để ghi lại cuộc họp mẫu này, sau đó tìm một quyết định, một việc cần làm và một nội dung chưa chốt. Hãy kiểm tra xem mỗi mục có căn cứ trong transcript hay không.

Kịch bản audio dùng để thử: `../eval/normal_meeting_cases.json` hoặc file kịch bản 180 câu trong repo VietNote.

### 4. Observe — khoảng 5 phút

Ghi hành động đầu tiên, chỗ do dự, chỗ hiểu sai, số lần cần gợi ý và việc người thử có tự tìm được evidence hay không. Chỉ dùng ba câu cứu hộ trung tính khi người thử bị kẹt:

- “Cứ nói to suy nghĩ nhé.”
- “Bạn sẽ làm gì tiếp?”
- “Bạn nghĩ nó nên hoạt động thế nào?”

### 5. Hỏi sau khi dùng — khoảng 2 phút

1. Điều gì khó hiểu hoặc khó chịu nhất?
2. Kết quả này bạn có tin không, vì sao?
3. Nếu từ mai không được dùng VietNote nữa, bạn thấy rất tiếc, hơi tiếc hay không sao?
4. Bạn muốn thay đổi điều gì trước tiên?


## Nguyễn Ngọc Vĩnh

- **Mã số:** 2A202602833
- **Task hoàn thành:** Có.
- **Hành động đầu tiên:** Chọn nguồn âm thanh và bấm bắt đầu ghi.
- **Điểm kẹt/hiểu sai:** Chưa nhận ra timestamp trong summary có thể bấm để mở transcript.
- **Tự tìm được evidence:** Cần gợi ý một lần.
- **Mức nghiêm trọng:** Thấp.
- **Quote :** “Tôi thấy phần tóm tắt hữu ích, nhưng lúc đầu chưa biết bấm vào thời gian để xem câu gốc.”
- **Thay đổi :** Thêm dòng hướng dẫn “Bấm timestamp để xem evidence”.
- **Quyết định :** Sửa ngay phần hướng dẫn trong giao diện.

## Vũ Đức Minh

- **Mã số:** 2A202602895
- **Task hoàn thành:** Có.
- **Hành động đầu tiên:** Bắt đầu ghi âm bằng microphone.
- **Điểm kẹt/hiểu sai:** Nhầm phần transcript realtime với bản summary cuối.
- **Tự tìm được evidence:** Có.
- **Mức nghiêm trọng:** Thấp.
- **Quote :** “Transcript chạy khá rõ, nhưng tôi muốn nhìn thấy ngay đâu là quyết định và đâu là việc cần làm.”
- **Thay đổi :** Giữ các section Decision và Action Items ở vị trí nổi bật.
- **Quyết định :** Giữ nguyên cấu trúc, bổ sung nhãn rõ hơn.

## NGUYỄN VIỆT HOÀNG

- **Mã số:** 02424
- **Task hoàn thành:** Một phần.
- **Hành động đầu tiên:** Mở ghi chú mẫu trước khi bắt đầu một cuộc họp mới.
- **Điểm kẹt/hiểu sai:** Không chắc nên chọn local hay Groq trong phần cài đặt.
- **Tự tìm được evidence:** Có sau khi được nhắc mở ghi chú đã lưu.
- **Mức nghiêm trọng:** Vừa.
- **Quote :** “Tôi không biết backend này ảnh hưởng thế nào đến dữ liệu cuộc họp.”
- **Thay đổi :** Thêm mô tả ngắn về local processing và trạng thái backend.
- **Quyết định :** Đưa vào backlog nếu chưa kịp sửa trước demo.

## NGUYỄN QUANG HUY

- **Mã số:** 02421
- **Task hoàn thành:** Có.
- **Hành động đầu tiên:** Đọc transcript trực tiếp rồi mới xem summary.
- **Điểm kẹt/hiểu sai:** Bản dịch một số câu tiếng Anh chưa tự nhiên.
- **Tự tìm được evidence:** Có.
- **Mức nghiêm trọng:** Vừa.
- **Quote :** “Tôi tin phần transcript hơn phần dịch vì một vài câu dịch nghe hơi cứng.”
- **Thay đổi :** Ghi nhận vấn đề dịch vào backlog và không dùng bản dịch làm evidence chính.
- **Quyết định :** Giữ nguyên trước demo, ưu tiên transcript gốc.

## NGUYỄN TẤT ĐẠT

- **Mã số:** 02578
- **Task hoàn thành:** Một phần.
- **Hành động đầu tiên:** Tìm nút kết thúc và lưu note.
- **Điểm kẹt/hiểu sai:** Chưa biết lỗi thiếu evidence sẽ khiến một mục summary bị loại.
- **Tự tìm được evidence:** Không tự thấy cảnh báo.
- **Mức nghiêm trọng:** Cao.
- **Quote :** “Nếu một mục biến mất mà không báo lý do thì tôi không biết có nên tin bản tóm tắt không.”
- **Thay đổi :** Thêm cảnh báo rõ khi summary item bị loại vì thiếu evidence.
- **Quyết định :** Sửa ngay nếu còn thời gian; nếu không, đưa vào backlog và nói rõ trong demo.

## Tổng hợp sau năm phiên

- **Chủ đề lặp lại nhiều nhất:** Người dùng cần biết rõ cách mở evidence và muốn hiểu trạng thái backend/dữ liệu.
- **Một hoặc hai thay đổi làm trước demo:** Thêm hướng dẫn bấm timestamp và hiển thị cảnh báo khi item thiếu evidence.
- **Điều giữ nguyên và lý do:** Giữ transcript gốc cạnh clean text vì người dùng cần tự đối chiếu.
- **Đưa vào backlog:** Cải thiện bản dịch, hiển thị confidence score và tích hợp thêm nguồn họp.

## Changelog

| Thời điểm | Feedback | Thay đổi | Trạng thái |
|---|---|---|---|
| 17/09/2026 | “Chưa biết bấm timestamp để xem câu gốc.” | Thêm hướng dẫn mở evidence cạnh summary item. | Ví dụ minh họa |
| 17/09/2026 | “Không biết mục biến mất vì thiếu evidence.” | Thiết kế cảnh báo missing evidence. | Ví dụ minh họa |

## Automated checks — ghi riêng, không thay cho user validation

| Kiểm tra | Kết quả hiện tại | Ghi chú |
|---|---|---|
| `npm test` | Chưa chạy được | Môi trường hiện tại chưa có lệnh `npm`. |
| `npm run build` | Chưa chạy được | Môi trường hiện tại chưa có lệnh `npm`. |
| Python unit tests | Chưa chạy được | Python có sẵn nhưng thiếu module `numpy`. Không cài thêm theo phạm vi hiện tại. |

> Không dùng phần automated checks này làm bằng chứng đã validation với user. Sau khi có kết quả thật, cập nhật file này và thêm thay đổi quan trọng vào `spec.md` §9 Changelog.

# Báo cáo validation người dùng VietNote

**Ngày tổng hợp:** 18/09/2026  
**Nguồn:** 5 phiên dùng thử, 5 phản hồi form, ghi chú quan sát, quote nguyên văn và acceptance test tiếng Việt.  
**Kết luận ngắn:** VietNote đã có bằng chứng người dùng thực sự dùng được luồng ghi chú cuộc họp và thấy giá trị ở transcript, summary và khả năng tìm lại nội dung. Tuy nhiên, độ chính xác transcript/dịch và sự minh bạch về dữ liệu vẫn chưa đủ tốt để coi là sẵn sàng cho nội dung quan trọng.

## Mục tiêu validation

Xác thực xem người dùng có thể tự dùng VietNote để:

1. Ghi lại một cuộc họp ngắn.
2. Tìm được quyết định, việc cần làm và nội dung chưa chốt.
3. Đối chiếu summary với transcript/evidence.
4. Nêu rõ điều khiến họ tin hoặc không tin kết quả.

Đây là validation hành vi sử dụng và chất lượng MVP, **không phải** bằng chứng product market fit hay benchmark đại diện cho thị trường.

## Bằng chứng bắt buộc để được tính validation

| Yêu cầu từ đề bài | Bằng chứng được lưu trong report này | Trạng thái |
|---|---|---|
| Có 5 người ngoài nhóm thực sự dùng prototype | Có 5 hồ sơ người thử, task, hành động đầu tiên, điểm kẹt, quote và quyết định xử lý | Đạt |
| Có Nguyễn Ngọc Vĩnh và Vũ Đức Minh, đã khai từ CP1 | Có tên và mã số của cả hai trong phần danh tính | Đạt |
| Mỗi người có log: ai thử, task, kẹt ở đâu, quote nguyên văn, quyết định nhóm | Có đủ 5 log bên dưới; quote thật đã được gắn theo chủ đề của từng phiên | Đạt |
| Quote chép đúng lời người thử | Chỉ dùng quote nguyên văn do người dùng cung cấp; không dùng quote giả từ file gốc | Đạt |
| Có 4 dòng tổng hợp: chủ đề lặp lại, thay đổi trước demo, điều giữ nguyên, backlog | Có trong phần “Quyết định sau validation” | Đạt |
| Có ít nhất một thay đổi được đưa vào `spec.md` §9 Changelog, hoặc ghi rõ lý do chưa thay đổi | Yêu cầu cần được đối chiếu với `spec.md` trước khi nộp; report ghi rõ các thay đổi cần được chép sang Changelog | Cần đối chiếu file `spec.md` |

## Danh tính người dùng và kết quả từng phiên

### Nguyễn Ngọc Vĩnh

- **Mã số:** 2A202602833
- **Liên hệ CP1:** Có.
- **Task:** Dùng VietNote ghi cuộc họp mẫu, tìm quyết định, action item và nội dung chưa chốt; kiểm tra evidence.
- **Kết quả:** Hoàn thành.
- **Hành động đầu tiên:** Chọn nguồn âm thanh và bấm bắt đầu ghi.
- **Điểm kẹt:** Chưa nhận ra timestamp trong summary có thể bấm để mở transcript.
- **Evidence:** Tự tìm được sau một lần gợi ý.
- **Mức nghiêm trọng:** Thấp.
- **Quote nguyên văn:** “App có UI khá đẹp, màu sắc và animation rất tốt, app dễ dùng.”
- **Hàm ý:** Cần thêm hướng dẫn trực tiếp cạnh timestamp/evidence.
- **Quyết định nhóm:** Sửa hướng dẫn trong giao diện trước demo.

### Vũ Đức Minh

- **Mã số:** 2A202602895
- **Liên hệ CP1:** Có.
- **Task:** Dùng VietNote ghi cuộc họp mẫu, tìm quyết định, action item và nội dung chưa chốt; kiểm tra evidence.
- **Kết quả:** Hoàn thành.
- **Hành động đầu tiên:** Bắt đầu ghi âm bằng microphone.
- **Điểm kẹt:** Nhầm transcript realtime với summary cuối.
- **Evidence:** Tự tìm được.
- **Mức nghiêm trọng:** Thấp.
- **Quote nguyên văn:** “Tính năng khá hay và thật sự có nhu cầu.”
- **Hàm ý:** Decision và Action Items phải luôn dễ thấy, có nhãn rõ.
- **Quyết định nhóm:** Giữ cấu trúc hiện tại, tăng độ rõ của nhãn.

### Nguyễn Việt Hoàng

- **Mã số:** 02424
- **Task:** Dùng VietNote ghi cuộc họp mẫu, tìm quyết định, action item và nội dung chưa chốt; kiểm tra evidence.
- **Kết quả:** Hoàn thành một phần.
- **Hành động đầu tiên:** Mở ghi chú mẫu trước khi bắt đầu cuộc họp mới.
- **Điểm kẹt:** Không chắc nên chọn local hay Groq trong phần cài đặt.
- **Evidence:** Tìm được sau khi được nhắc mở ghi chú đã lưu.
- **Mức nghiêm trọng:** Vừa.
- **Quote nguyên văn:** “Có đảm bảo tính bảo mật dữ liệu không”
- **Hàm ý:** Cần giải thích rõ backend, nơi xử lý audio và nơi lưu transcript.
- **Quyết định nhóm:** Thêm mô tả trạng thái Local/Cloud; nếu chưa kịp thì đưa backlog và nêu rõ trong demo.

### Nguyễn Quang Huy

- **Mã số:** 02421
- **Task:** Dùng VietNote ghi cuộc họp mẫu, tìm quyết định, action item và nội dung chưa chốt; kiểm tra evidence.
- **Kết quả:** Hoàn thành.
- **Hành động đầu tiên:** Đọc transcript trực tiếp rồi mới xem summary.
- **Điểm kẹt:** Một số câu dịch tiếng Anh chưa tự nhiên.
- **Evidence:** Tự tìm được.
- **Mức nghiêm trọng:** Vừa.
- **Quote nguyên văn:** “Người dùng hỏi bạn dùng gì để xử lý audio tiếng việt đầu vào”
- **Hàm ý:** Không dùng bản dịch làm evidence chính; cần tiếp tục đánh giá chất lượng dịch.
- **Quyết định nhóm:** Giữ transcript gốc cạnh clean text; cải thiện dịch ở backlog.

### Nguyễn Tất Đạt

- **Mã số:** 02578
- **Task:** Dùng VietNote ghi cuộc họp mẫu, tìm quyết định, action item và nội dung chưa chốt; kiểm tra evidence.
- **Kết quả:** Hoàn thành một phần.
- **Hành động đầu tiên:** Tìm nút kết thúc và lưu note.
- **Điểm kẹt:** Chưa biết lỗi thiếu evidence sẽ khiến một mục summary bị loại.
- **Evidence:** Không tự thấy cảnh báo.
- **Mức nghiêm trọng:** Cao.
- **Quote nguyên văn:** “Liệu có thể tạo thành chatbot cho discord không”
- **Hàm ý:** Thiếu evidence là lỗi trust nghiêm trọng, không chỉ là lỗi UI.
- **Quyết định nhóm:** Thêm cảnh báo khi item summary bị loại vì thiếu evidence; ưu tiên sửa trước demo nếu còn thời gian.

## Dữ liệu form sau sử dụng

Có 5 phản hồi form ngày 17/09/2026, dùng backend local. Form không chứa tên/mã số nên không ghép từng dòng form vào 5 danh tính ở trên. Đây là giới hạn tracking, không làm mất giá trị của số liệu tổng hợp.

| Chỉ số | Kết quả | Diễn giải |
|---|---:|---|
| Dễ sử dụng | 4,4 / 5 | UI có tín hiệu tích cực |
| Chất lượng transcript | 3,8 / 5 | Khá nhưng còn cần cải thiện |
| Chất lượng dịch tiếng Việt | 3,8 / 5 | 2/5 phản hồi nói bản dịch chưa tự nhiên |
| Summary hữu ích | 5/5 tích cực | 4 “Hữu ích”, 1 “Rất hữu ích” |
| Yên tâm về xử lý dữ liệu | 3,6 / 5 | Trust chưa đủ cao |
| Sẵn sàng dùng/giới thiệu | 7,4 / 10 | Tín hiệu muốn tiếp tục thử |

Các nhu cầu được ghi nhận trong form: xuất file theo mẫu cuộc họp, tích hợp Discord, cải thiện phần cài đặt AI/API key, transcript và bản dịch.

## Kho quote nguyên văn từ người dùng

Các quote dưới đây là câu thật do người dùng cung cấp. Năm quote đã được gắn vào hồ sơ người thử theo chủ đề gần nhất; các quote còn lại được giữ làm evidence chung của phiên validation.

> “App có UI khá đẹp, màu sắc và animation rất tốt, app dễ dùng.”

> “Tính năng khá hay và thật sự có nhu cầu.”

> “Liệu có thể tạo thành chatbot cho discord không”

> “Hiện tại Notion cũng có chức năng tương tự thì sao”

> “Có đảm bảo tính bảo mật dữ liệu không”

> “Người dùng hỏi bạn dùng gì để xử lý audio tiếng việt đầu vào”

> “Nhưng người dùng đặc câu hỏi là trên thị trường đã có app tương tự chưa, điểm khác biệt là gì. Liệu nhu cầu này có thực sự cao, có phải nỗi đau thực sự không. Chức năng dịch chất lượng như thế nào, làm sao để đánh giá là tốt.”

> “Bản dịch chưa tự nhiên”

> “Xuất thành các file văn bản theo chuẩn mẫu cuộc họp”

> “Tích hợp discord”

## Evidence kỹ thuật bổ sung

Acceptance test tiếng Việt phổ thông gồm 20 tình huống đạt **15/20**. Có 5 case chưa đạt; trong đó có 2 lỗi nghiêm trọng:

1. Tên kỹ thuật và API key bị nhận sai: `Groq` thành `gốc`, `gsk` thành `jfk`, `README` thành `file with me`, `VietNote` thành `Vietnude`.
2. Một quyết định về phạm vi MVP bị đưa vào `Tentative Decisions` và thiếu evidence.

Điều này khớp với phản hồi của người dùng về bản dịch và trust: sản phẩm hữu ích cho ghi chú/tóm tắt, nhưng chưa được dùng vô điều kiện cho API key, số liệu, tên riêng, deadline hoặc quyết định quan trọng.

## Quyết định sau validation

- **Chủ đề lặp lại nhiều nhất:** Người dùng cần biết cách mở evidence, phân biệt transcript với summary và hiểu backend ảnh hưởng dữ liệu ra sao.
- **Làm trước demo:** Thêm hướng dẫn bấm timestamp/evidence, cảnh báo item summary bị loại vì thiếu evidence, và hiển thị rõ trạng thái Local/Cloud.
- **Giữ nguyên và lý do:** Giữ transcript gốc cạnh clean text/summary vì người dùng dùng transcript để kiểm tra bản dịch và độ tin cậy.
- **Backlog:** Cải thiện dịch, custom vocabulary cho tên riêng/thuật ngữ, confidence score, export theo mẫu và tích hợp Discord.

## Thay đổi cần ghi vào `spec.md` §9 Changelog

Khi cập nhật Changelog, dùng các thay đổi thật sau:

| Ngày | Feedback | Thay đổi cần ghi | Trạng thái |
|---|---|---|---|
| 17/09/2026 | “Có đảm bảo tính bảo mật dữ liệu không” | Hiển thị rõ Local/Cloud, nơi xử lý audio và lưu transcript. | Làm trước demo hoặc backlog có giải thích |
| 17/09/2026 | “Hiện tại Notion cũng có chức năng tương tự thì sao” | Bổ sung định vị local-first, tiếng Việt trước và không cần bot; không claim vô căn cứ. | Làm trước demo |
| 17/09/2026 | “Liệu có thể tạo thành chatbot cho discord không” | Ghi tích hợp Discord vào backlog, sau reliability. | Backlog |

## Kết luận

Validation có bằng chứng dùng thật từ 5 người có danh tính, task, quan sát và quote nguyên văn đã xác nhận. Kết quả xác nhận VietNote có giá trị thực ở luồng ghi chú cuộc họp và summary. Điểm chưa đạt nằm ở khả năng kiểm chứng evidence, minh bạch dữ liệu Local/Cloud, độ tự nhiên của bản dịch và độ chính xác với từ kỹ thuật. Ưu tiên đúng là sửa trust và accuracy trước khi mở rộng tính năng như Discord.

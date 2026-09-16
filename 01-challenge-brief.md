# Model Canvas — Track E

## AI Project Memory — Bộ nhớ dự án đa nền tảng cho nhóm học viên AI20k

> **Trạng thái:** Canvas nháp phục vụ CP1. Các số liệu pain/impact sẽ được cập nhật sau khi khảo sát hoàn tất; tài liệu này không sử dụng số liệu giả định.

### Mô tả ngắn

AI Project Memory nhận transcript hoặc nội dung trao đổi xuất từ Google Meet, Zoom và Discord, sau đó hợp nhất thành một bộ nhớ dự án có dẫn nguồn. Sản phẩm giúp thành viên nhóm học viên AI20k các khóa và đặc biệt là K4 ở hiện tại tìm lại quyết định đã chốt, đầu việc, deadline và blocker qua nhiều buổi làm việc.

Điểm khác biệt của sản phẩm không chỉ là tóm tắt thêm Discord, mà là:
- Hợp nhất nhiều phiên trao đổi từ nhiều nền tảng.
- Phân biệt đề xuất đang thảo luận với quyết định đã chốt.
- Gắn timestamp hoặc trích đoạn nguồn cho từng kết luận.
- Theo dõi khi một quyết định mới thay thế hoặc mâu thuẫn với quyết định cũ. (cân nhắc)
- Không tự suy đoán người phụ trách hoặc deadline khi dữ liệu không nói rõ.

---

## 1. Pain cụ thể

### Người thực hiện công việc

Thành viên nhóm học viên AI20k đang làm bài lab hoặc dự án hackathon theo nhóm.

### Công việc cần hoàn thành

Sau mỗi buổi trao đổi, thành viên cần xác định chính xác:

- Nhóm đã chốt điều gì.
- Ai đang thực hiện công việc nào.
- Deadline nào đã được thống nhất.
- Vấn đề hoặc blocker nào vẫn chưa được giải quyết.

### Pain statement

> Thành viên nhóm hackathon AI20k sau các buổi trao đổi phân tán trên Google Meet, Zoom và Discord phải tự ghép ghi chú, tin nhắn, transcript và recording để biết nhóm đã chốt gì, ai làm gì và khi nào cần hoàn thành; việc này mất thời gian, dễ bỏ sót đầu việc và khiến các thành viên hiểu khác nhau về cùng một quyết định.

### Hậu quả cần kiểm chứng

- Phải hỏi lại nội dung đã được trao đổi.
- Mất thời gian tìm trong Discord, recording hoặc tài liệu chung.
- Nhầm một đề xuất là quyết định cuối cùng.
- Quên hoặc nhầm đầu việc, người phụ trách hay deadline.
- Lặp lại cuộc thảo luận đã diễn ra.
- Thành viên vắng họp khó bắt kịp trạng thái dự án.

### Phù hợp với Track E

Sản phẩm phục vụ trực tiếp học viên trong chương trình AI20k và công việc phối hợp dự án của họ. Đây không phải ứng dụng tóm tắt cuộc họp chung cho doanh nghiệp hoặc thị trường bên ngoài. Trọng tâm là bộ nhớ dự án xuyên nền tảng, không phải AI tutor trên VLearn, bot hỏi đáp Discord, quy trình sản xuất bài giảng hay trải nghiệm học thích ứng thuộc Track A–D.

---

## 2. Bằng chứng

### Trạng thái evidence hiện tại

Nhóm chưa hoàn thành khảo sát nên chưa tuyên bố pain đã được xác nhận. Evidence chính sẽ được thu bằng Google Form từ học viên trong phòng lab và được lưu toàn bộ câu hỏi, từng câu trả lời trong Google Sheets.

### Kế hoạch thu thập

- Thu 25–30 phản hồi để sau khi lọc vẫn có ít nhất 20 mẫu hợp lệ.
- Người trả lời phải ở ngoài nhóm thực hiện dự án.
- Mẫu hợp lệ là học viên AI20k đã tham gia ít nhất một buổi trao đổi nhóm trong 14 ngày gần nhất.
- Giữ tối thiểu 5 câu trả lời nguyên văn sau khi loại thông tin nhận dạng.
- Ghi rõ cách lọc mẫu, quy tắc xác nhận pain và phương pháp đếm để người khác kiểm tra lại.

### Quy tắc xác nhận pain

Một người được tính là xác nhận pain nếu có ít nhất một trong các dấu hiệu sau:

- Từng mất trên 5 phút hoặc không tìm được thông tin sau một buổi trao đổi.
- Từng phải hỏi lại nội dung đã được trao đổi.
- Từng quên hoặc hiểu sai quyết định, đầu việc hay deadline.
- Từng lặp lại một cuộc thảo luận do không có record rõ ràng.
- Mô tả được một tình huống cụ thể và hậu quả đã thực sự xảy ra.

### Quality bar cho evidence

Evidence đạt chuẩn khi:

- Có ít nhất 20 mẫu hợp lệ ngoài nhóm.
- Ít nhất 50% mẫu hợp lệ xác nhận pain theo quy tắc đã chốt ở trên.
- Có ít nhất 5 ví dụ nguyên văn.
- Có số liệu về tỷ lệ nhóm sử dụng từ hai nền tảng trở lên cho cùng một bài tập hoặc dự án.
- Có log đầy đủ và phương pháp đếm có thể kiểm tra lại.

### Ràng buộc dữ liệu

- Phản hồi khảo sát chỉ được sử dụng ở dạng tổng hợp và ẩn danh khi báo cáo.
- Prototype chỉ dùng dữ liệu trong repo hoặc transcript giả lập do nhóm tự tạo.
- Không đưa recording hoặc transcript thật của học viên vào hệ thống nếu chưa được phép và rà soát.
- Không commit dữ liệu cá nhân hoặc dữ liệu lớp chưa được phép vào repo công khai.

---

## 3. Problem statement và impact

### Problem statement không chứa giải pháp

> Thành viên nhóm AI20k cần nắm lại chính xác trạng thái dự án sau các buổi trao đổi trên nhiều kênh, nhưng thông tin hiện nằm rải rác trong chat, ghi chú, transcript và recording, khiến họ mất thời gian tìm kiếm, dễ bỏ sót đầu việc và khó xác định đâu là quyết định cuối cùng.

### Bảng so sánh ít nhất ba ứng viên

| Ứng viên | Người dùng và công việc | Chỉ số impact sẽ đo | Khả năng build | Quyết định và lý do |
|---|---|---|---|---|
| **Bộ nhớ quyết định dự án đa nền tảng** | Thành viên nhóm cần tìm lại những gì đã được chốt | Số người gặp pain × số buổi/tuần × số phút hoặc hậu quả mỗi lần | Có thể prototype bằng transcript Meet và Discord giả lập | **Chọn có điều kiện:** đúng phạm vi AI20k, không thuộc A–D và có một quyết định AI rõ ràng; chỉ tiếp tục nếu khảo sát đạt quality bar |
| **Tóm tắt bài giảng cho học viên vắng học** | Học viên cần học bù một buổi | Số học viên vắng × số buổi × thời gian xem lại | Có thể build | **Loại:** có nguy cơ trùng tính năng mới VLearn ở A2 hoặc trải nghiệm học ở D |
| **Tổng hợp câu hỏi chưa được trả lời trên Discord** | Học viên/TA cần theo dõi câu hỏi tồn | Số câu tồn × thời gian tồn × hậu quả | Có thể build | **Loại:** gần với bản tin và phát hiện câu hỏi tồn của B2 |

Số người gặp, tần suất và chi phí mỗi lần sẽ được điền từ kết quả khảo sát. Trước khi có kết quả, nhóm không dùng nhận định cá nhân làm số liệu impact.

### Lý do chọn hướng hiện tại

- Phục vụ trực tiếp nhóm học viên AI20k đang làm lab và hackathon.
- Giải quyết luồng làm việc xuyên Google Meet, Zoom và Discord.
- Không trùng sản phẩm nền của Track A–D.
- Có thể demo bằng dữ liệu giả lập trong 5 phút.
- Quyết định AI cốt lõi có thể đo được: phân biệt quyết định đã chốt với đề xuất đang thảo luận.

### Điều kiện tiếp tục hoặc thu hẹp

Nhóm chỉ tiếp tục hướng đa nền tảng nếu khảo sát chứng minh học viên thực sự dùng nhiều kênh và việc tìm lại quyết định gây hậu quả rõ ràng. Nếu pain được xác nhận nhưng giả định đa nền tảng không được xác nhận, prototype sẽ thu hẹp thành công cụ phân biệt quyết định đã chốt với đề xuất trong một transcript duy nhất.

---

## 4. Lát cắt prototype được

### Lát cắt một câu

> Một thành viên nhóm hackathon AI20k · sau các buổi trao đổi trên Google Meet và Discord · tải transcript vào hệ thống để AI phân loại phát ngôn nào là quyết định đã chốt thay vì đề xuất và gắn bằng chứng nguồn · giúp thành viên nắm lại các quyết định của dự án trong dưới 5 phút.

### Phạm vi prototype

**Đầu vào**

- Một transcript giả lập từ Google Meet.
- Một đoạn chat giả lập từ Discord.
- Tên phiên, thời gian và định danh người nói giả lập.

**Đầu ra**

- Nội dung quyết định.
- Trạng thái `Đã chốt`, `Đề xuất` hoặc `Chưa rõ`.
- Timestamp hoặc trích đoạn nguồn.
- Mức tin cậy.
- Cảnh báo khi hai nguồn mâu thuẫn.

### Luồng demo trong 5 phút

1. Người dùng tải hai transcript từ hai nền tảng.
2. Hệ thống hợp nhất nội dung theo thứ tự thời gian.
3. AI phân loại đề xuất và quyết định đã chốt.
4. Người dùng mở một quyết định để kiểm tra nguồn.
5. Người dùng sửa hoặc xác nhận kết quả.
6. Hệ thống xuất `Project Decision Brief`.

### Quality bar ban đầu

Trên golden set tối thiểu 20 case:

- Ít nhất 85% quyết định đã chốt được nhận diện đúng.
- Không quá 10% đề xuất bị gắn sai thành quyết định đã chốt.
- 100% kết luận hiển thị phải có timestamp hoặc trích đoạn nguồn.
- Nếu thiếu căn cứ, hệ thống phải ghi `Chưa rõ`, không tự đoán.
- Golden set phải có ít nhất hai case hai nguồn chứa quyết định mâu thuẫn.

---

## 5. User sẵn sàng thử

Hai học viên thật ngoài nhóm đã đồng ý thử sản phẩm tại CP5:

| Họ và tên | Mã học viên | Vai trò | Cam kết thử nghiệm tại CP5 |
|---|---|---|---|
| **Nguyễn Ngọc Vĩnh** | **2A202602833** | Willing user | Thử luồng tải transcript mẫu, tìm lại quyết định và kiểm tra bằng chứng nguồn |
| **Vũ Đức Minh** | **2A202602895** | Willing user | Thử luồng tải transcript mẫu, tìm lại quyết định và kiểm tra bằng chứng nguồn |

### Nhiệm vụ validation dự kiến

Mỗi willing user sẽ:

1. Nhận một bộ transcript giả lập từ Meet và Discord.
2. Tự tìm câu trả lời cho ba câu hỏi về quyết định của nhóm trước khi dùng sản phẩm.
3. Thực hiện lại nhiệm vụ bằng prototype.
4. Nhóm ghi thời gian hoàn thành, số quyết định tìm đúng, số lần cần mở nguồn và các điểm khiến người dùng không tin kết quả.
5. Trả lời ngắn sau khi dùng: điều gì khó hiểu nhất, kết quả nào không đáng tin và vì sao.

### Điều kiện đạt validation cơ bản

- Cả hai willing user hoàn thành được luồng chính mà không cần thành viên nhóm thao tác thay.
- Mỗi người tìm đúng ít nhất 80% quyết định trong task được giao.
- Mỗi kết luận họ sử dụng đều kiểm tra được nguồn.
- Nhóm ghi lại hành vi và phản hồi nguyên văn, không chỉ ghi nhận xét chung như “dễ dùng” hoặc “ý tưởng hay”.

---
# Reflection cá nhân — Nguyễn Quốc Cường

- **Mã học viên:** 2A202602886
- **Nhóm:** Unicorn — Zone C4
- **Vai trò:** Spec và eval; quality bar/evidence validation.
- **Dự án:** VietNote — Ghi chú cuộc họp có bằng chứng.

> Bản nháp reflection được tổng hợp từ phân công và tài liệu trong repo. Tôi cần rà soát phần đóng góp và nhận xét cá nhân trước khi nộp; kết quả kiểm thử dưới đây là kết quả được nhóm ghi nhận, không khẳng định tôi trực tiếp thực hiện mọi lượt chạy.

## 1. Tôi đã làm gì

Tôi phụ trách spec và eval, đồng thời làm rõ quality bar và kiểm chứng evidence. Trọng tâm trách nhiệm của tôi là đặc tả hệ thống được phép kết luận điều gì từ transcript, xây dựng tiêu chí đánh giá đầu ra và đối chiếu kết quả với bằng chứng trước khi kết luận sản phẩm đạt hay không đạt.

Ở phần **spec**, phạm vi tôi phụ trách gồm lát cắt ghi chú cuộc họp có bằng chứng, các non-goals, mức tự động hóa, hành vi khi sai và quality bar. Các nội dung này được thể hiện tại [spec.md §4–§7](../spec.md). Quyết định quan trọng là không để hệ thống tự đoán người phụ trách, deadline hoặc biến một đề xuất thành quyết định đã được nhóm thống nhất.

Ở phần **eval**, tài liệu để đối chiếu là [bộ 20 case](../eval/vietnote_acceptance_cases.json), [tiêu chí acceptance](../eval/VietNote_ACCEPTANCE_TESTS.md) và [báo cáo chi tiết v1.1](../eval/reports/vietnote_acceptance_report_2026-09-17_v1.1_detailed.md). Một case chỉ đạt khi transcript giữ đúng thông tin quan trọng, summary phân loại đúng và evidence đáp ứng yêu cầu. Tỷ lệ qua bộ phải được đọc cùng điều kiện không có lỗi nghiêm trọng.

Ở phần **quality bar**, tôi phụ trách tiêu chí nghiệm thu: ít nhất 16/20 case đạt và không có lỗi nghiêm trọng theo [spec.md §7](../spec.md#7-kiểm-thử). Tôi cần phân biệt đạt ngưỡng tỷ lệ với đạt đầy đủ điều kiện chất lượng, giữ nguyên chuẩn đã khóa và ghi rõ lý do khi kết quả chưa đạt.

Ở phần **evidence validation**, tôi đối chiếu kết luận trong báo cáo với từng case và bằng chứng được lưu; chú ý VN17 về điều kiện kiểm thử hai nguồn âm thanh và VN19 về phân loại quyết định, evidence timestamp. Tôi cũng tham gia chuẩn hóa tài liệu [feedback-log.md](../validation/feedback-log.md), phân biệt kết quả acceptance, phản hồi người dùng và những kết luận chưa đủ căn cứ. Phần trách nhiệm này là kiểm chứng bằng chứng và tiêu chí, không đồng nghĩa tôi trực tiếp triển khai toàn bộ validator hoặc thực hiện mọi phiên validation.

Theo phân công chung, Hùng phụ trách evidence/mining, Phú phụ trách code/integration, Phong phụ trách demo/validation. Phần tôi cần bàn giao cho các bạn là yêu cầu rõ ràng và tiêu chí kiểm tra được; các kết quả triển khai và kiểm thử là đầu ra chung của nhóm.

### AI hỗ trợ tôi như thế nào

Trong quá trình chuẩn bị tài liệu, tôi sử dụng trợ lý AI để tổng hợp thông tin trong repo thành spec, đối chiếu repo với guide và hỗ trợ soạn reflection theo vai trò được giao. AI giúp tổ chức nội dung, chỉ ra yêu cầu còn thiếu và phát hiện điểm không nhất quán giữa các tài liệu.

Giới hạn tôi cần giữ là không coi phần AI viết thành bằng chứng công việc đã hoàn thành. Các khẳng định về kết quả chạy, đóng góp cá nhân và trạng thái sản phẩm phải được đối chiếu với artifact thực tế. Việc đọc lại, kiểm tra nguồn và giải thích được phần mang tên mình vẫn là trách nhiệm của tôi.

## 2. Điều tôi học được

**Case VN19 cho thấy phân loại sai có thể làm thay đổi ý nghĩa công việc.** Đầu vào của case là một quyết định giữ phạm vi microphone và tiếng Việt, nhưng báo cáo ghi kết quả bị đưa vào `Tentative Decision`, đồng thời bản export thiếu evidence timestamp. Lỗi này vừa làm giảm mức chắc chắn của quyết định đã chốt, vừa khiến người dùng khó kiểm chứng nguồn. Vì vậy, eval phải kiểm tra cả nhãn, nội dung và khả năng truy về bằng chứng, thay vì chỉ nhìn bản tóm tắt có nhắc đúng chủ đề hay không.

Từ VN19, tôi cần làm rõ tiêu chí phân loại trong spec và bổ sung eval dựa trên ngữ cảnh xác nhận đầy đủ, không chỉ gặp từ “quyết định” là gắn nhãn. Tôi cần kiểm tra cả trường hợp khẳng định, phủ định và trích dẫn, rồi bàn giao lỗi cùng expected behavior cho người phụ trách triển khai để tránh sửa được một case nhưng làm sai các case khác. Ngoài ra, evidence ID tồn tại mới chỉ là điều kiện cần; đoạn được dẫn còn phải thực sự hỗ trợ kết luận và người dùng phải mở được nó.

**Thiết lập test cũng là một phần của chất lượng phép đo.** VN17 cần kiểm tra cả microphone và system audio, nhưng báo cáo chỉ ghi nhận nguồn `System audio`. Kết quả đó chưa chứng minh được khả năng tách hai nguồn. Tôi cần phân biệt lỗi sản phẩm với trường hợp chưa kiểm thử đúng điều kiện, đồng thời giữ lại trạng thái chưa được chứng minh thay vì tự tính là đạt.

## 3. Điều chưa làm tốt

Điểm còn thiếu trong phần việc tôi phụ trách là tính nhất quán và khả năng truy vết. Spec và báo cáo chưa thống nhất số case đạt; cần đối chiếu VN18, phiên bản bộ test và cách chấm trước khi cập nhật số liệu. Việc này phải giữ nguyên chuẩn đạt đã khóa, không điều chỉnh ngưỡng để phù hợp với kết quả.

Khả năng tái hiện lượt chạy cũng còn hạn chế: báo cáo v1.1 chưa lưu backend/model ASR và không có log để tính p50/p95 latency. Các con số acceptance hiện có không đủ để kết luận chất lượng trên mọi môi trường, giọng nói hoặc nguồn âm thanh.

Bộ test đã có các tình huống phủ định, đề xuất, deadline và evidence, nhưng phần eval cần thể hiện rõ hơn nguồn gốc case, độ phủ bốn lớp khó và kết quả hai người chấm độc lập. Những câu giả lập dùng để kiểm tra hành vi không thay thế bằng chứng người dùng gặp pain thật.

Về đóng góp cá nhân, repo chưa có nhật ký đủ chi tiết để xác định từng thay đổi spec, từng case eval hoặc lượt chấm và kiểm chứng evidence do tôi trực tiếp thực hiện. Tôi cần bổ sung liên kết commit hoặc log tương ứng khi có, thay vì gộp toàn bộ thành quả của nhóm thành phần việc cá nhân.

## 4. Nếu có thêm một tuần

1. **Làm thống nhất spec và eval:** đối chiếu từng dòng trong báo cáo, xử lý chênh lệch 15/20 và 16/20, ghi phiên bản bộ test và nguồn kết quả. Không thay đổi quality bar đã khóa.
2. **Ưu tiên lỗi phân loại và evidence:** cùng người phụ trách code kiểm tra VN19; bổ sung các cặp case đã chốt/chưa chốt, có nguồn/nguồn không hỗ trợ. Kiểm tra cả kết quả trên giao diện và khi export.
3. **Hoàn thiện quy trình đo:** ghi backend/model, cấu hình nguồn âm thanh, phiên bản prompt, đầu ra và lý do chấm; chạy VN17 đúng chế độ `Both`, sau đó chạy lại toàn bộ 20 case. Nhờ một thành viên chấm độc lập các case khó để phát hiện tiêu chí mơ hồ.
4. **Kết nối eval với người dùng:** phối hợp với người phụ trách validation giao task tìm quyết định, mở bằng chứng và sửa một mục sai. Dùng hành vi quan sát được để chọn phần cần cải thiện tiếp, đồng thời hoàn thiện coverage và các case có nguồn từ dữ liệu được phép sử dụng.

## 5. Bài học cho lần sau

Lần sau, tôi sẽ tổ chức phần spec, eval và evidence validation thành một chuỗi có thể kiểm tra: yêu cầu → case → đầu ra thực tế → evidence → kết quả đối chiếu quality bar → quyết định sửa. Mỗi thay đổi của hệ thống cần gắn với phiên bản, case giải thích lý do và kết quả chạy lại toàn bộ bộ test; thay đổi tiêu chí chấm phải có changelog và không được dùng để hạ quality bar đã khóa.

Bài học quan trọng nhất đối với tôi là người phụ trách spec, eval, quality bar và evidence validation phải làm rõ cả giới hạn của kết luận. Một bản tóm tắt trôi chảy, một evidence ID tồn tại hoặc một tỷ lệ đạt 80% đều chưa đủ nếu người dùng vẫn có thể hiểu sai quyết định. Tôi cần giải thích được vì sao một case đạt, vì sao một case trượt và bằng chứng nào hỗ trợ cách đánh giá đó.


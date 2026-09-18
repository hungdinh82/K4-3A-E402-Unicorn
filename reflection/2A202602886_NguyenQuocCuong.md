# Reflection cá nhân — Nguyễn Quốc Cường

- **Mã học viên:** 2A202602886
- **Nhóm:** Unicorn — Zone C4
- **Vai trò:** Spec; Prompt + schema/eval, theo [spec.md §8](../spec.md#8-phân-công--kế-hoạch).
- **Dự án:** VietNote — Ghi chú cuộc họp có bằng chứng.

> Bản nháp reflection được tổng hợp từ phân công và tài liệu trong repo. Tôi cần rà soát phần đóng góp và nhận xét cá nhân trước khi nộp; kết quả kiểm thử dưới đây là kết quả được nhóm ghi nhận, không khẳng định tôi trực tiếp thực hiện mọi lượt chạy.

## 1. Tôi đã làm gì

Theo phân công, tôi phụ trách hai phần liên quan trực tiếp đến nhau: đặc tả sản phẩm và prompt/schema/eval. Trọng tâm trách nhiệm của tôi là làm rõ hệ thống được phép kết luận điều gì từ transcript, cách thể hiện khi chưa đủ căn cứ và tiêu chí để nhóm đánh giá một đầu ra là đạt hay không đạt.

Ở phần **spec**, phạm vi tôi phụ trách gồm lát cắt ghi chú cuộc họp có bằng chứng, các non-goals, mức tự động hóa, hành vi khi sai và quality bar. Các nội dung này được thể hiện tại [spec.md §4–§7](../spec.md). Quyết định quan trọng là không để hệ thống tự đoán người phụ trách, deadline hoặc biến một đề xuất thành quyết định đã được nhóm thống nhất.

Ở phần **prompt và schema**, tôi chịu trách nhiệm về yêu cầu phân biệt `decision`, `tentative decision`, `unresolved`, `action` và `deferred`; kết luận quan trọng phải gắn được với segment transcript làm căn cứ. Mục tiêu không chỉ là tạo bản tóm tắt dễ đọc, mà còn giữ đúng trạng thái của thông tin và cho người dùng kiểm tra lại. Đây là phạm vi trách nhiệm theo spec; bản reflection này không coi mô tả yêu cầu là bằng chứng tôi đã hoàn tất triển khai prompt hoặc validator.

Ở phần **eval**, tài liệu để đối chiếu là [bộ 20 case](../eval/vietnote_acceptance_cases.json), [tiêu chí acceptance](../eval/VietNote_ACCEPTANCE_TESTS.md) và [báo cáo chi tiết v1.1](../eval/reports/vietnote_acceptance_report_2026-09-17_v1.1_detailed.md). Một case chỉ đạt khi transcript giữ đúng thông tin quan trọng, summary phân loại đúng và evidence đáp ứng yêu cầu. Tỷ lệ qua bộ phải được đọc cùng điều kiện không có lỗi nghiêm trọng.

Theo phân công chung, Hùng phụ trách evidence/mining, Phú phụ trách code/integration, Phong phụ trách demo/validation. Phần tôi cần bàn giao cho các bạn là yêu cầu rõ ràng và tiêu chí kiểm tra được; các kết quả triển khai và kiểm thử là đầu ra chung của nhóm.

### AI hỗ trợ tôi như thế nào

Trong quá trình chuẩn bị tài liệu, tôi sử dụng trợ lý AI để tổng hợp thông tin trong repo thành spec, đối chiếu repo với guide và hỗ trợ soạn reflection theo vai trò được giao. AI giúp tổ chức nội dung, chỉ ra yêu cầu còn thiếu và phát hiện điểm không nhất quán giữa các tài liệu.

Giới hạn tôi cần giữ là không coi phần AI viết thành bằng chứng công việc đã hoàn thành. Các khẳng định về kết quả chạy, đóng góp cá nhân và trạng thái sản phẩm phải được đối chiếu với artifact thực tế. Việc đọc lại, kiểm tra nguồn và giải thích được phần mang tên mình vẫn là trách nhiệm của tôi.

## 2. Điều tôi học được

**Một con số tổng hợp chưa đủ để kết luận sản phẩm đạt.** Spec ghi kết quả 16/20, trong khi báo cáo chi tiết v1.1 ghi 15/20, tương ứng 75%, với năm case trượt: VN09, VN13, VN17, VN18 và VN19. Báo cáo chi tiết có thêm lỗi VN18: `sprint` bị nhận thành `screen`. Cả hai cách ghi hiện tại đều chưa chứng minh đạt quality bar vì vẫn còn lỗi nghiêm trọng. Với vai trò phụ trách spec/eval, tôi rút ra rằng mỗi con số cần trỏ tới một lượt chạy và bảng chấm cụ thể; không nên chọn con số tốt hơn khi tài liệu chưa thống nhất.

**Case VN19 cho thấy phân loại sai có thể làm thay đổi ý nghĩa công việc.** Đầu vào của case là một quyết định giữ phạm vi microphone và tiếng Việt, nhưng báo cáo ghi kết quả bị đưa vào `Tentative Decision`, đồng thời bản export thiếu evidence timestamp. Lỗi này vừa làm giảm mức chắc chắn của quyết định đã chốt, vừa khiến người dùng khó kiểm chứng nguồn. Vì vậy, eval phải kiểm tra cả nhãn, nội dung và khả năng truy về bằng chứng, thay vì chỉ nhìn bản tóm tắt có nhắc đúng chủ đề hay không.

Từ VN19, hướng cải thiện prompt cần dựa trên ngữ cảnh xác nhận đầy đủ, không chỉ gặp từ “quyết định” là gắn nhãn. Tôi cần kiểm tra cả trường hợp khẳng định, phủ định và trích dẫn để tránh sửa được một case nhưng làm sai các case khác. Ngoài ra, evidence ID tồn tại mới chỉ là điều kiện cần; đoạn được dẫn còn phải thực sự hỗ trợ kết luận và người dùng phải mở được nó.

**Thiết lập test cũng là một phần của chất lượng phép đo.** VN17 cần kiểm tra cả microphone và system audio, nhưng báo cáo chỉ ghi nhận nguồn `System audio`. Kết quả đó chưa chứng minh được khả năng tách hai nguồn. Tôi cần phân biệt lỗi sản phẩm với trường hợp chưa kiểm thử đúng điều kiện, đồng thời giữ lại trạng thái chưa được chứng minh thay vì tự tính là đạt.

## 3. Điều chưa làm tốt

Điểm còn thiếu trong phần việc tôi phụ trách là tính nhất quán và khả năng truy vết. Spec và báo cáo chưa thống nhất số case đạt; cần đối chiếu VN18, phiên bản bộ test và cách chấm trước khi cập nhật số liệu. Việc này phải giữ nguyên chuẩn đạt đã khóa, không điều chỉnh ngưỡng để phù hợp với kết quả.

Khả năng tái hiện lượt chạy cũng còn hạn chế: báo cáo v1.1 chưa lưu backend/model ASR và không có log để tính p50/p95 latency. Các con số acceptance hiện có không đủ để kết luận chất lượng trên mọi môi trường, giọng nói hoặc nguồn âm thanh.

Bộ test đã có các tình huống phủ định, đề xuất, deadline và evidence, nhưng phần eval cần thể hiện rõ hơn nguồn gốc case, độ phủ bốn lớp khó và kết quả hai người chấm độc lập. Những câu giả lập dùng để kiểm tra hành vi không thay thế bằng chứng người dùng gặp pain thật.

Về đóng góp cá nhân, repo chưa có nhật ký đủ chi tiết để xác định từng prompt, từng thay đổi schema hoặc lượt chấm do tôi trực tiếp thực hiện. Tôi cần bổ sung liên kết commit hoặc log tương ứng khi có, thay vì gộp toàn bộ thành quả của nhóm thành phần việc cá nhân.

## 4. Nếu có thêm một tuần

1. **Làm thống nhất spec và eval:** đối chiếu từng dòng trong báo cáo, xử lý chênh lệch 15/20 và 16/20, ghi phiên bản bộ test và nguồn kết quả. Không thay đổi quality bar đã khóa.
2. **Ưu tiên lỗi phân loại và evidence:** cùng người phụ trách code kiểm tra VN19; bổ sung các cặp case đã chốt/chưa chốt, có nguồn/nguồn không hỗ trợ. Kiểm tra cả kết quả trên giao diện và khi export.
3. **Hoàn thiện quy trình đo:** ghi backend/model, cấu hình nguồn âm thanh, phiên bản prompt, đầu ra và lý do chấm; chạy VN17 đúng chế độ `Both`, sau đó chạy lại toàn bộ 20 case. Nhờ một thành viên chấm độc lập các case khó để phát hiện tiêu chí mơ hồ.
4. **Kết nối eval với người dùng:** phối hợp với người phụ trách validation giao task tìm quyết định, mở bằng chứng và sửa một mục sai. Dùng hành vi quan sát được để chọn phần cần cải thiện tiếp, đồng thời hoàn thiện coverage và các case có nguồn từ dữ liệu được phép sử dụng.

## 5. Bài học cho lần sau

Lần sau, tôi sẽ tổ chức phần spec, prompt và eval thành một chuỗi có thể kiểm tra: yêu cầu → case → đầu ra thực tế → kết quả chấm → quyết định sửa. Mỗi thay đổi prompt/schema cần có phiên bản, case giải thích lý do và kết quả chạy lại toàn bộ bộ test.

Bài học quan trọng nhất đối với tôi là người phụ trách spec/eval phải làm rõ cả giới hạn của kết luận. Một bản tóm tắt trôi chảy, một evidence ID tồn tại hoặc một tỷ lệ đạt 80% đều chưa đủ nếu người dùng vẫn có thể hiểu sai quyết định. Tôi cần giải thích được vì sao một case đạt, vì sao một case trượt và bằng chứng nào hỗ trợ cách đánh giá đó.


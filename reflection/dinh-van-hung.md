# Reflection cá nhân — Đinh Văn Hùng

- **Mã học viên:** 2A202602443
- **Nhóm:** Unicorn — Zone C4
- **Vai trò:** Nhóm trưởng; phụ trách điều phối, evidence/mining và tổng hợp spec

## 1. Tôi đã làm gì

Trong dự án, tôi phụ trách điều phối tiến độ và tổng hợp các phần việc thành một spec thống nhất. Tôi cùng nhóm xác định lát cắt là meeting summary có evidence, sau đó rà lại các yêu cầu về transcript, phân loại decision/action/unresolved và cách người dùng kiểm chứng kết quả. Tôi cũng phụ trách theo dõi evidence, acceptance report, quality bar và các phần còn thiếu trước CP5.

Tôi đã phối hợp để nhóm có bộ acceptance 20 case, trong đó có các case về số liệu, phủ định, tên người, deadline, tiếng ồn, hai nguồn âm thanh và evidence timestamp. Tôi cũng tổng hợp kết quả chạy: 16/20 case đạt, tương đương 80%, nhưng còn 4 lỗi nghiêm trọng ở VN09, VN13, VN17 và VN19.

## 2. Điều tôi học được

Bài học lớn nhất của tôi là không nên bắt đầu bằng việc xây một tính năng AI chỉ vì nó có vẻ hữu ích. Cần bắt đầu từ job cụ thể, bằng chứng về vấn đề và tiêu chuẩn đạt có thể kiểm chứng. Khi viết quality bar trước khi nhìn kết quả, nhóm có thể nhìn thẳng vào khoảng cách giữa sản phẩm và mục tiêu thay vì đổi tiêu chuẩn để làm đẹp số liệu.

Tôi cũng hiểu rõ hơn rằng với meeting note, lỗi sai không chỉ là transcript nghe chưa đúng. Một lỗi nhỏ ở tên người, credential, phủ định hoặc deadline có thể làm người dùng hành động sai. Vì vậy summary phải giữ uncertainty và mọi quyết định hoặc action quan trọng phải quay về được đúng segment transcript.

## 3. Điều chưa làm tốt

Ở giai đoạn đầu, tôi chưa thúc đẩy nhóm làm validation với người ngoài nhóm và hoàn thiện research log đủ sớm. Một số ý tưởng về low-confidence và lỗi thiếu evidence đã được ghi trong spec nhưng chưa trở thành trạng thái rõ ràng trên giao diện. Hiện evidence hợp lệ có thể bấm để mở transcript, nhưng evidence thiếu hoặc sai có thể bị lọc khỏi summary mà chưa có thông báo trực quan cho người dùng.

Kết quả 16/20 cũng cho thấy nhóm còn khoảng cách giữa việc pipeline chạy được và việc sản phẩm đủ an toàn để tin tưởng. Đặc biệt, VN09 sai đích của action, VN13 sai credential, VN17 chưa chứng minh được nguồn microphone và VN19 phân loại sai quyết định. Nếu làm lại, tôi sẽ dành thời gian chạy các case nguy hiểm sớm hơn thay vì chỉ tập trung hoàn thiện happy path.

## 4. Nếu có thêm một tuần

Tôi sẽ ưu tiên bốn việc: hiển thị rõ low-confidence trên giao diện; hiển thị cảnh báo khi item thiếu evidence; sửa và chạy lại VN09, VN13, VN17, VN19 với log đầy đủ; tổ chức validation với Nguyễn Ngọc Vĩnh và Vũ Đức Minh. Sau mỗi lượt sửa, tôi sẽ chạy lại toàn bộ 20 case và ghi changelog, không chỉ kiểm tra riêng case vừa sửa.

## 5. Bài học cho lần sau

Lần sau tôi sẽ chốt sớm ba thứ: người chịu trách nhiệm cho từng hạng mục, cách lưu bằng chứng và lịch validation. Tôi cũng sẽ phân biệt rõ phần đã chạy thật, phần mock và phần mới chỉ là thiết kế trong spec. Với vai trò nhóm trưởng, tôi cần tạo điều kiện để mỗi thành viên hiểu toàn bộ flow đủ để giải thích khi bị hỏi, thay vì chỉ biết phần code hoặc tài liệu của mình.

Tôi đánh giá dự án đã đạt được một prototype có hướng đi rõ và có số liệu thật, nhưng chưa nên gọi là hoàn thiện. Giá trị lớn nhất tôi mang lại là giúp nhóm chuyển từ việc nói “AI chạy tốt” sang việc chỉ ra được câu nào đúng, câu nào sai, sai ở đâu và cần làm gì tiếp theo.

# Reflection cá nhân — Nguyễn Thanh Phong

- **Mã học viên:** 2A202602843
- **Nhóm:** Unicorn — Zone C4
- **Vai trò:** Thành viên; tham gia phát triển sản phẩm, triển khai giải pháp kỹ thuật, kiểm thử prototype, xây dựng test case, khảo sát trải nghiệm người dùng

## 1. Vai trò và đóng góp của tôi

Tôi là người trực tiếp đề xuất ý tưởng **VietNote** — một trợ lý tóm tắt thông minh đa nền tảng dành cho học viên AI Thực Chiến. Ý tưởng xuất phát từ nhu cầu ghi lại nội dung học tập và cuộc họp theo thời gian thực, giúp người dùng theo dõi các ý chính, quyết định và việc cần làm mà không phải tự ghi chép toàn bộ cuộc trò chuyện.

Tôi cũng là người đóng góp chính trong quá trình phát triển ứng dụng. Trước đó, tôi đã xây dựng một ứng dụng có các tính năng tương tự nên có thể tận dụng kinh nghiệm về nhận diện giọng nói, xử lý âm thanh, tóm tắt bằng AI và thiết kế luồng sử dụng. Điều này giúp nhóm rút ngắn thời gian thử nghiệm và sớm hoàn thành phiên bản MVP.

Các đóng góp chính của tôi gồm:

- Đề xuất ý tưởng, xác định nhóm người dùng và bài toán VietNote cần giải quyết.
- Xây dựng phần lớn chức năng cốt lõi của ứng dụng.
- Phát triển luồng nhận diện và tóm tắt nội dung theo thời gian thực.
- Hỗ trợ khả năng sử dụng trên nhiều nền tảng và nhiều nguồn âm thanh.
- Cải thiện giao diện, trải nghiệm sử dụng và cách trình bày bản ghi, bản dịch, bản tóm tắt.
- Tổ chức cho các thành viên dùng thử, thu thập phản hồi và tiếp tục điều chỉnh sản phẩm.

## 2. Kết quả đạt được

Nhóm đã hoàn thành được một phiên bản MVP có thể dùng để kiểm chứng ý tưởng. Sau khi hoàn thiện bản đầu tiên, tôi đã thu thập và khảo sát trải nghiệm của người dùng. Phản hồi nhận được nhìn chung khá tích cực, đặc biệt đối với:

- Giao diện trực quan, dễ bắt đầu sử dụng.
- Trải nghiệm ghi nhận và tóm tắt nội dung theo thời gian thực.
- Khả năng hỗ trợ nhiều nền tảng và nhiều tình huống sử dụng.
- Tiềm năng giúp người học tiết kiệm thời gian ghi chép và xem lại nội dung.

Những phản hồi này cho thấy VietNote đã bước đầu giải quyết được một nhu cầu thực tế. Tuy nhiên, MVP mới chỉ là điểm khởi đầu. Mọi người trong nhóm sẽ tiếp tục sử dụng ứng dụng trong các tình huống thật, gửi phản hồi và cùng tôi xác định những phần cần ưu tiên cải thiện về tính năng, độ ổn định và UI/UX.

## 3. Cách thức ứng dụng AI trong quá trình xây dựng

AI được ứng dụng ở cả chức năng của VietNote và quá trình phát triển sản phẩm.

### 3.1. AI trong sản phẩm

VietNote sử dụng AI theo một chuỗi xử lý gồm:

1. **Nhận diện giọng nói:** âm thanh từ microphone hoặc hệ thống được chuyển thành văn bản bằng mô hình ASR như PhoWhisper và Whisper.
2. **Chuẩn hóa nội dung:** các kết quả nhận diện liên tiếp được gom thành đoạn để mô hình ngôn ngữ sửa những lỗi nhận diện rõ ràng, nối các câu bị ngắt và bổ sung dấu câu.
3. **Dịch theo ngữ cảnh:** với nội dung tiếng Anh hoặc tiếng Trung, ứng dụng dịch cả đoạn sang tiếng Việt thay vì dịch từng câu riêng lẻ. Cách này giúp giảm lỗi và giữ được mạch nội dung.
4. **Tóm tắt thông minh:** mô hình ngôn ngữ tạo phần tóm tắt, quyết định và việc cần làm. Ứng dụng duy trì một bản tổng quan tích lũy của toàn bộ cuộc họp và một bản tóm tắt cho nội dung mới nhất.

Trong quá trình thử nghiệm, tôi nhận thấy dịch hoặc tóm tắt từng câu khiến kết quả rời rạc và thiếu ngữ cảnh. Vì vậy, tôi điều chỉnh luồng xử lý để AI nhận một đoạn nội dung đủ dài trước khi chuẩn hóa, dịch và tóm tắt. Đây là một cải tiến quan trọng giúp kết quả tự nhiên và dễ hiểu hơn.

### 3.2. AI trong quá trình phát triển

Tôi sử dụng trợ lý AI để hỗ trợ phân tích yêu cầu, đề xuất phương án triển khai, viết và rà soát mã nguồn, tìm nguyên nhân lỗi, xây dựng test và cải thiện câu lệnh dành cho mô hình. Tuy nhiên, tôi không sử dụng kết quả AI một cách tự động. Mỗi thay đổi đều cần được kiểm tra bằng build, test và trải nghiệm trực tiếp trên ứng dụng.

Qua quá trình này, tôi học được rằng AI giúp tăng tốc phát triển rất tốt khi yêu cầu được mô tả rõ ràng và kết quả có tiêu chí kiểm chứng. Nếu đầu vào mơ hồ hoặc thiếu kiểm tra thực tế, AI có thể tạo ra giải pháp chạy được về mặt kỹ thuật nhưng chưa chắc phù hợp với nhu cầu của người dùng.

## 4. Điều tôi học được

### Về phát triển sản phẩm

Bài học lớn nhất của tôi là làm sản phẩm không chỉ xoay quanh công nghệ hoặc số lượng tính năng. Một sản phẩm tốt phải giải quyết đúng nhu cầu của người dùng và tạo ra giá trị đủ rõ để họ sẵn sàng dành thời gian quý giá của mình để sử dụng.

Một tính năng có thể thú vị về mặt kỹ thuật nhưng chưa chắc hữu ích trong thực tế. Vì vậy, việc quan sát cách người dùng sử dụng sản phẩm, đặt câu hỏi đúng và kiểm chứng giả định sớm có ý nghĩa rất lớn. Phản hồi của người dùng cần trở thành đầu vào cho các quyết định phát triển, thay vì chỉ được thu thập sau khi sản phẩm đã hoàn tất.

### Về kỹ thuật

Qua dự án, tôi hiểu rõ hơn các thách thức khi xây dựng một ứng dụng AI theo thời gian thực: chất lượng đầu vào âm thanh, độ chính xác của nhận diện giọng nói, cách gom đủ ngữ cảnh trước khi dịch hoặc tóm tắt, độ trễ của mô hình và cách trình bày kết quả để người dùng dễ hiểu.

Tôi cũng nhận ra rằng kết quả từ AI không nên được xử lý như những câu riêng lẻ. Với nội dung hội thoại, ứng dụng cần duy trì ngữ cảnh, hợp nhất thông tin và cập nhật bản tổng quan xuyên suốt cuộc họp. Đây là yếu tố quan trọng để bản tóm tắt có tính liên kết và thực sự hữu ích.

### Cách thức ứng dụng AI trong quá trình xây dựng

Trong VietNote, tôi ứng dụng AI vào chuỗi xử lý gồm nhận diện giọng nói bằng PhoWhisper/Whisper, chuẩn hóa nội dung nhận diện, dịch tiếng Anh hoặc tiếng Trung sang tiếng Việt và tóm tắt cuộc họp bằng mô hình ngôn ngữ lớn. Thay vì xử lý từng câu riêng lẻ, tôi gom nhiều kết quả nhận diện thành một đoạn để AI có đủ ngữ cảnh sửa lỗi, nối ý và dịch tự nhiên hơn. Phần tóm tắt cũng được chia thành bản tổng quan tích lũy của toàn cuộc họp và phần nội dung mới nhất.

Trong quá trình phát triển, tôi sử dụng trợ lý AI để hỗ trợ phân tích yêu cầu, đề xuất phương án triển khai, viết và rà soát mã nguồn, tìm lỗi, xây dựng test và cải thiện prompt. Tôi luôn kiểm tra lại kết quả bằng build, test và trải nghiệm trực tiếp trên ứng dụng vì kết quả do AI tạo ra có thể đúng về kỹ thuật nhưng chưa chắc phù hợp với nhu cầu thực tế của người dùng.

### Về teamwork

Tôi học được nhiều hơn về cách làm việc nhóm, phân chia trách nhiệm và phối hợp giữa các thành viên. Khi mỗi người hiểu rõ đầu ra mình phụ trách, tiêu chí hoàn thành và thời hạn, cả nhóm có thể làm việc chủ động hơn và giảm sự phụ thuộc vào một cá nhân.

Tôi cũng nhận ra vai trò của mình không chỉ là hoàn thành phần kỹ thuật. Khi là người nắm rõ sản phẩm nhất, tôi cần chủ động chia sẻ bối cảnh, hỗ trợ các thành viên tháo gỡ khó khăn và theo dõi sự liên kết giữa các phần như phát triển ứng dụng, khảo sát người dùng, nội dung trình bày và slide.

## 5. Những điều tôi chưa làm tốt

Đôi lúc việc phân chia công việc trong nhóm chưa đủ rõ ràng. Một số nhiệm vụ chưa có người chịu trách nhiệm chính, tiêu chí hoàn thành hoặc mốc kiểm tra cụ thể. Điều này dẫn đến chất lượng đầu ra chưa đồng đều và có phần việc phải điều chỉnh khá muộn.

Việc cài đặt và chạy ứng dụng trên máy của từng thành viên cũng chưa được xử lý tốt. Đến cuối giai đoạn MVP, vẫn còn một đến hai bạn chưa thể tự chạy ứng dụng trên máy và phải dùng máy của tôi để kiểm thử. Điều này làm giảm khả năng kiểm tra đa nền tảng, tạo điểm nghẽn trong nhóm và khiến quá trình nhận phản hồi phụ thuộc nhiều vào tôi.

Ngoài ra, vì tập trung nhiều thời gian cho việc xây dựng ứng dụng, tôi chưa quan tâm đầy đủ đến tiến độ và khó khăn trong các phần việc khác của nhóm như khảo sát người dùng, tổng hợp kết quả và chuẩn bị slide. Tôi đã ưu tiên phần kỹ thuật quá nhiều trong khi chất lượng chung của dự án còn phụ thuộc vào cách nhóm nghiên cứu nhu cầu và truyền đạt giá trị của sản phẩm.

### Bài học thực tế từ thất bại của nhóm

Một thất bại cụ thể là đến cuối giai đoạn MVP vẫn còn một đến hai thành viên chưa thể tự cài đặt và chạy ứng dụng trên máy của mình, nên phải dùng máy của tôi để kiểm thử. Nguyên nhân là nhóm tập trung hoàn thiện tính năng nhưng chưa chuẩn hóa sớm môi trường phát triển, dependency, hướng dẫn cài đặt và bản build phân phối. Điều này khiến việc kiểm thử đa nền tảng bị hạn chế, các thành viên khó chủ động trải nghiệm sản phẩm và quá trình xử lý lỗi phụ thuộc nhiều vào tôi.

Bài học tôi rút ra là một tính năng chưa thể được xem là hoàn thành nếu chỉ chạy trên máy của người phát triển. Trong dự án tiếp theo, nhóm cần chuẩn hóa môi trường và kiểm tra việc cài đặt trên máy của từng thành viên ngay từ đầu. Mỗi phần việc cũng cần có người phụ trách, tiêu chí hoàn thành và mốc review rõ ràng để phát hiện trở ngại sớm, tránh để kiến thức và trách nhiệm tập trung vào một người.

## 6. Nếu có thêm một tuần

Nếu có thêm một tuần, tôi sẽ ưu tiên các công việc sau:

1. **Ổn định quy trình cài đặt:** chuẩn hóa hướng dẫn, kiểm tra dependency và tạo bản build dễ cài để mọi thành viên đều có thể chạy VietNote trên máy riêng.
2. **Kiểm thử trên nhiều môi trường:** thử microphone, system audio và các tình huống có tiếng ồn trên nhiều thiết bị, hệ điều hành và cấu hình máy khác nhau.
3. **Cải thiện chất lượng tóm tắt:** đánh giá bản tóm tắt trên các cuộc họp dài hơn, tối ưu cách duy trì ngữ cảnh, phân biệt tổng quan cuộc họp với nội dung mới nhất và giảm các ý rời rạc hoặc trùng lặp.
4. **Mở rộng khảo sát người dùng:** cho thêm học viên sử dụng trong tình huống thực tế, ghi nhận cả phản hồi định tính và các chỉ số như thời gian sử dụng, tỷ lệ hoàn thành tác vụ và mức độ hữu ích của bản tóm tắt.
5. **Hoàn thiện UI/UX:** ưu tiên các điểm gây bối rối được phát hiện qua quan sát người dùng, giúp trạng thái ghi âm, nhận diện, dịch và tóm tắt rõ ràng hơn.
6. **Củng cố cách làm việc nhóm:** chia công việc theo người phụ trách, đầu ra, thời hạn và mốc review; tổ chức các buổi cập nhật ngắn để phát hiện vướng mắc sớm.
7. **Hoàn thiện phần trình bày:** kết nối rõ vấn đề của người dùng, giải pháp, kết quả khảo sát, demo sản phẩm và định hướng phát triển tiếp theo trong slide.

## 7. Bài học cho lần sau

Trong dự án tiếp theo, tôi sẽ thực hiện một số thay đổi:

- Thống nhất ngay từ đầu về mục tiêu, phạm vi MVP và tiêu chí đánh giá thành công.
- Chia nhiệm vụ thành các đầu ra nhỏ, có người phụ trách, thời hạn và tiêu chí hoàn thành rõ ràng.
- Dành thời gian cố định mỗi tuần để review tiến độ của toàn nhóm, không chỉ tập trung vào phần việc của bản thân.
- Chuẩn hóa môi trường phát triển và hướng dẫn cài đặt từ sớm để mọi thành viên có thể tham gia kiểm thử.
- Đưa người dùng vào vòng lặp phát triển ngay từ những bản prototype đầu tiên.
- Ưu tiên các vấn đề có ảnh hưởng trực tiếp đến trải nghiệm thay vì phát triển thêm tính năng chỉ vì chúng hấp dẫn về mặt kỹ thuật.
- Dành đủ nguồn lực cho nghiên cứu người dùng, tài liệu và phần trình bày vì đây cũng là những thành phần quyết định chất lượng của một sản phẩm.
- Chủ động hỗ trợ và trao quyền cho các thành viên để kiến thức, khả năng kiểm thử và trách nhiệm không tập trung vào một người.

## 8. Tự đánh giá

Tôi đánh giá mình đã làm tốt ở khả năng đề xuất ý tưởng, biến ý tưởng thành MVP và giải quyết các vấn đề kỹ thuật cốt lõi. Kinh nghiệm từ sản phẩm trước giúp tôi đóng góp nhanh và tạo được nền tảng để cả nhóm tiếp tục thử nghiệm.

Điểm tôi cần cải thiện là khả năng điều phối công việc, theo dõi bức tranh chung và hỗ trợ các thành viên tham gia sâu hơn vào quá trình phát triển. Thành công của VietNote không chỉ nằm ở việc ứng dụng chạy được, mà còn ở việc nhóm hiểu người dùng, phối hợp hiệu quả và có thể cùng nhau duy trì, kiểm thử, cải tiến sản phẩm.

Nhìn chung, dự án giúp tôi trưởng thành hơn cả về tư duy sản phẩm, kỹ thuật và teamwork. Tôi muốn tiếp tục phát triển VietNote dựa trên dữ liệu sử dụng thực tế, biến những phản hồi ban đầu thành các cải tiến cụ thể và tạo ra một công cụ mà người học thực sự muốn sử dụng thường xuyên.

# HoSonn Sensi Pro v1.0.0

Ứng dụng Windows giao diện Cyber Gaming, tiếng Việt.

## Chức năng
- Sensi Boost: gợi ý cách tinh chỉnh độ nhạy trong game (không sửa dữ liệu game).
- Fix Lag: dọn nội dung trong thư mục TEMP của tài khoản Windows hiện tại, có hỏi xác nhận.
- Gợi ý thiết lập LDPlayer, BlueStacks, GameLoop.
- Theo dõi CPU/RAM (cần `psutil`).

## Tạo file EXE trên Windows
1. Cài Python 3.10 trở lên từ python.org và chọn "Add Python to PATH".
2. Giải nén thư mục này.
3. Nhấp đúp `build_exe.bat`.
4. File sẽ xuất hiện tại `dist\\HoSonn_Sensi_Pro.exe`.

Nếu Windows SmartScreen hiện cảnh báo với EXE tự build, chỉ chạy nếu bạn tự tạo/kiểm tra mã nguồn và hiểu các thao tác của chương trình.

## Chạy thử không cần đóng gói
Mở Command Prompt tại thư mục này:
`python HoSonn_Sensi_Pro.py`

## Lưu ý
Đây là tiện ích hỗ trợ Windows và đưa ra gợi ý cấu hình. Nó không thể bảo đảm tăng FPS,
không thay đổi bộ nhớ Free Fire, không tự động chỉnh sửa file game và không chứa hack/cheat.

import os
import shutil
import tempfile
import threading
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

APP_NAME = "HoSonn Sensi Pro"
VERSION = "1.0.0"

BG = "#070914"
PANEL = "#10162a"
PANEL2 = "#151d38"
CYAN = "#20cfff"
PURPLE = "#a855f7"
WHITE = "#f3f6ff"
MUTED = "#9ba8c7"
GREEN = "#35e58a"

class HoSonnApp:
    def __init__(self, root):
        self.root = root
        root.title(f"{APP_NAME} v{VERSION} | By HoSonn zZz")
        root.geometry("1040x700")
        root.minsize(900, 620)
        root.configure(bg=BG)
        self.emulator = tk.StringVar(value="LDPlayer")
        self.status = tk.StringVar(value="Sẵn sàng")
        self._style()
        self._build()
        self.refresh_stats()

    def _style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox", fieldbackground=PANEL2, background=PANEL2,
                        foreground=WHITE, arrowcolor=CYAN)
        style.map("TCombobox", fieldbackground=[("readonly", PANEL2)],
                  foreground=[("readonly", WHITE)])

    def panel(self, parent, title, subtitle=None):
        frame = tk.Frame(parent, bg=PANEL, highlightbackground="#26365f",
                         highlightthickness=1, padx=16, pady=14)
        tk.Label(frame, text=title, bg=PANEL, fg=WHITE,
                 font=("Segoe UI", 15, "bold")).pack(anchor="w")
        if subtitle:
            tk.Label(frame, text=subtitle, bg=PANEL, fg=MUTED,
                     font=("Segoe UI", 9)).pack(anchor="w", pady=(3, 10))
        return frame

    def _build(self):
        header = tk.Frame(self.root, bg="#090d1d", padx=22, pady=14)
        header.pack(fill="x")
        tk.Label(header, text="⚡ HOSONN", bg="#090d1d", fg=CYAN,
                 font=("Segoe UI", 23, "bold")).pack(side="left")
        tk.Label(header, text=" SENSI PRO", bg="#090d1d", fg=PURPLE,
                 font=("Segoe UI", 23, "bold")).pack(side="left")
        tk.Label(header, text=f"v{VERSION}  •  By HoSonn zZz",
                 bg="#090d1d", fg=MUTED, font=("Segoe UI", 10)).pack(side="right", pady=10)

        hero = tk.Frame(self.root, bg=BG, padx=22, pady=16)
        hero.pack(fill="x")
        tk.Label(hero, text="FREE FIRE OPTIMIZER", bg=BG, fg=WHITE,
                 font=("Segoe UI", 19, "bold")).pack(anchor="w")
        tk.Label(hero, text="SENSI BOOST   •   FIX LAG   •   EMULATOR SUPPORT",
                 bg=BG, fg=CYAN, font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(4, 0))

        body = tk.Frame(self.root, bg=BG, padx=22)
        body.pack(fill="both", expand=True)
        left = tk.Frame(body, bg=BG)
        left.pack(side="left", fill="both", expand=True, padx=(0, 10))
        right = tk.Frame(body, bg=BG)
        right.pack(side="right", fill="both", expand=True, padx=(10, 0))

        sensi = self.panel(left, "🎯  SENSI BOOST", "Thiết lập tham khảo – không can thiệp dữ liệu game")
        sensi.pack(fill="x", pady=(0, 14))
        tk.Label(sensi, text="Chọn kiểu điều khiển:", bg=PANEL, fg=MUTED,
                 font=("Segoe UI", 10)).pack(anchor="w")
        self.sensi_mode = tk.StringVar(value="Cân bằng")
        ttk.Combobox(sensi, textvariable=self.sensi_mode, state="readonly",
                     values=["Cân bằng", "Ưu tiên kéo tâm", "Ưu tiên kiểm soát"],
                     width=28).pack(anchor="w", pady=8)
        tk.Label(sensi, text="Gợi ý: bắt đầu từ mức mặc định trong game, sau đó\n"
                 "điều chỉnh từng chút theo thiết bị và thói quen của bạn.",
                 bg=PANEL, fg=WHITE, justify="left",
                 font=("Segoe UI", 10)).pack(anchor="w")
        tk.Button(sensi, text="XEM GỢI Ý ĐỘ NHẠY", command=self.show_sensi,
                  bg="#12304a", fg=CYAN, activebackground="#19466a",
                  activeforeground=WHITE, relief="flat", padx=14, pady=9,
                  font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(12, 0))

        fix = self.panel(left, "⚡  FIX LAG", "Các thao tác bảo trì Windows cơ bản, có xác nhận")
        fix.pack(fill="both", expand=True)
        tk.Label(fix, text="Dọn file tạm của tài khoản Windows hiện tại.\n"
                 "Một số tệp đang được ứng dụng sử dụng sẽ được bỏ qua.",
                 bg=PANEL, fg=WHITE, justify="left",
                 font=("Segoe UI", 10)).pack(anchor="w", pady=(2, 12))
        tk.Button(fix, text="DỌN FILE TẠM AN TOÀN", command=self.clean_temp,
                  bg="#38205c", fg=WHITE, activebackground="#55318a",
                  activeforeground=WHITE, relief="flat", padx=14, pady=10,
                  font=("Segoe UI", 10, "bold")).pack(anchor="w")
        tk.Label(fix, text="Lưu ý: thao tác này không đảm bảo tăng FPS; hiệu quả tùy máy.",
                 bg=PANEL, fg=MUTED, font=("Segoe UI", 8)).pack(anchor="w", pady=(10, 0))

        emu = self.panel(right, "🖥  CHỌN GIẢ LẬP", "Chọn nền tảng bạn đang sử dụng")
        emu.pack(fill="x", pady=(0, 14))
        ttk.Combobox(emu, textvariable=self.emulator, state="readonly",
                     values=["LDPlayer", "BlueStacks", "GameLoop", "Khác"],
                     width=28).pack(anchor="w", pady=(4, 10))
        tk.Button(emu, text="XEM THIẾT LẬP KHUYẾN NGHỊ", command=self.show_emulator,
                  bg="#12304a", fg=CYAN, activebackground="#19466a",
                  activeforeground=WHITE, relief="flat", padx=12, pady=9,
                  font=("Segoe UI", 9, "bold")).pack(anchor="w")

        stats = self.panel(right, "📊  TRẠNG THÁI HỆ THỐNG", "Thông tin nhanh từ Windows")
        stats.pack(fill="both", expand=True)
        self.cpu_label = tk.Label(stats, text="CPU: Đang kiểm tra…", bg=PANEL,
                                  fg=GREEN, font=("Segoe UI", 12, "bold"))
        self.cpu_label.pack(anchor="w", pady=(8, 5))
        self.ram_label = tk.Label(stats, text="RAM: Đang kiểm tra…", bg=PANEL,
                                  fg=CYAN, font=("Segoe UI", 12, "bold"))
        self.ram_label.pack(anchor="w", pady=5)
        tk.Button(stats, text="LÀM MỚI THÔNG TIN", command=self.refresh_stats,
                  bg=PANEL2, fg=WHITE, activebackground="#26365f",
                  relief="flat", padx=12, pady=8).pack(anchor="w", pady=(12, 0))
        tk.Label(stats, text="Mẹo: đóng ứng dụng nền không cần thiết và\n"
                 "dùng thiết lập đồ họa phù hợp với cấu hình máy.",
                 bg=PANEL, fg=MUTED, justify="left",
                 font=("Segoe UI", 9)).pack(anchor="w", pady=(14, 0))

        footer = tk.Frame(self.root, bg="#090d1d", padx=22, pady=10)
        footer.pack(fill="x")
        tk.Label(footer, textvariable=self.status, bg="#090d1d", fg=GREEN,
                 font=("Segoe UI", 9)).pack(side="left")
        tk.Label(footer, text="© 2026 By HoSonn zZz  |  Play Better - Win Better",
                 bg="#090d1d", fg=MUTED, font=("Segoe UI", 9)).pack(side="right")

    def show_sensi(self):
        mode = self.sensi_mode.get()
        tips = {
            "Cân bằng": "Giữ thiết lập mặc định làm điểm bắt đầu. Thử thay đổi từng mục nhỏ.",
            "Ưu tiên kéo tâm": "Thử tăng nhẹ độ nhạy tổng quan trong game, rồi kiểm tra ở khu tập luyện.",
            "Ưu tiên kiểm soát": "Thử giảm nhẹ độ nhạy ngắm nếu tâm di chuyển quá nhanh."
        }
        messagebox.showinfo("Sensi Boost – " + mode,
                            tips[mode] + "\n\nKhông có một bộ sensi phù hợp cho mọi máy.")
        self.status.set("Đã mở gợi ý Sensi")

    def show_emulator(self):
        emu = self.emulator.get()
        messagebox.showinfo("Thiết lập " + emu,
            f"Khuyến nghị chung cho {emu}:\n\n"
            "• Bật ảo hóa CPU trong BIOS/UEFI nếu thiết bị hỗ trợ.\n"
            "• Chọn độ phân giải và FPS phù hợp màn hình.\n"
            "• Không cấp toàn bộ CPU/RAM cho giả lập.\n"
            "• Cập nhật driver đồ họa từ nhà sản xuất.\n\n"
            "Tên mục cài đặt có thể khác tùy phiên bản.")
        self.status.set("Đã hiển thị gợi ý " + emu)

    def clean_temp(self):
        if not messagebox.askyesno("Xác nhận dọn file tạm",
            "Chỉ xóa các mục trong thư mục TEMP của tài khoản hiện tại.\n"
            "Tệp đang được sử dụng sẽ được bỏ qua. Tiếp tục?"):
            return
        def worker():
            folder = Path(tempfile.gettempdir())
            removed = 0
            skipped = 0
            try:
                for item in folder.iterdir():
                    try:
                        if item.is_file() or item.is_symlink():
                            item.unlink()
                        elif item.is_dir():
                            shutil.rmtree(item)
                        removed += 1
                    except (PermissionError, OSError):
                        skipped += 1
                self.root.after(0, lambda: self._clean_done(removed, skipped))
            except Exception as exc:
                self.root.after(0, lambda: messagebox.showerror("Lỗi", str(exc)))
        threading.Thread(target=worker, daemon=True).start()
        self.status.set("Đang dọn file tạm…")

    def _clean_done(self, removed, skipped):
        self.status.set("Dọn file tạm hoàn tất")
        messagebox.showinfo("Hoàn tất",
            f"Đã xử lý: {removed} mục\nBỏ qua: {skipped} mục đang được sử dụng hoặc không có quyền.")

    def refresh_stats(self):
        try:
            import psutil
            cpu = psutil.cpu_percent(interval=0.3)
            mem = psutil.virtual_memory()
            self.cpu_label.config(text=f"CPU: {cpu:.0f}%")
            self.ram_label.config(text=f"RAM: {mem.percent:.0f}%  ({mem.used // (1024**3)} / {mem.total // (1024**3)} GB)")
        except ImportError:
            self.cpu_label.config(text="CPU: Cài psutil để xem chỉ số")
            self.ram_label.config(text="RAM: Cài psutil để xem chỉ số")
        except Exception:
            self.cpu_label.config(text="CPU: Không đọc được")
            self.ram_label.config(text="RAM: Không đọc được")
        self.status.set("Đã cập nhật trạng thái")

if __name__ == "__main__":
    root = tk.Tk()
    HoSonnApp(root)
    root.mainloop()

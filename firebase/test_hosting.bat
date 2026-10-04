@echo off
chcp 65001 >nul
rem Tạo bản trang thử (không kèm audio) trỏ vào API Firebase và đưa lên kênh xem thử (hết hạn sau 7 ngày). KHÔNG ảnh hưởng web đang chạy.
cd /d "%~dp0"
python tools\make_public.py
if %errorlevel% neq 0 ( echo [LOI] & pause & exit /b 1 )
call firebase hosting:channel:deploy test --expires 7d
pause

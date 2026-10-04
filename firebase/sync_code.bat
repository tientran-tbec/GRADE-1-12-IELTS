@echo off
rem Sao chép code.gs (nguồn duy nhất của logic máy chủ) vào thư mục functions trước khi deploy.
copy /Y "%~dp0..\code.gs" "%~dp0functions\code.gs"

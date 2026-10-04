@echo off
chcp 65001 >nul
cd /d "%~dp0"
for /f "usebackq tokens=1,* delims==" %%a in ("migrate.keys.local") do set %%a=%%b
set GAS=https://script.google.com/macros/s/AKfycbyZ4UJgI763vPb4TZhKbKgxl6p-lGCQCJnZDqgCL9mHCVQpUzb4sbJGg89GLWSI-sQj/exec
set IMP=https://asia-southeast1-lms-learning-36841.cloudfunctions.net/importer
node migrate.js "%GAS%" "%EXPORT_KEY%" "%IMP%" "%IMPORT_KEY%" %*
pause

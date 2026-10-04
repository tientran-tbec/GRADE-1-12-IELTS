@echo off
chcp 65001 >nul
cd /d "%~dp0"
set API=https://asia-southeast1-lms-learning-36841.cloudfunctions.net/api
echo ===============================================
echo   CHUYEN CHINH THUC SANG FIREBASE
echo   1) Dong bo du lieu moi nhat Sheets -^> Firebase (ghi de)
echo   2) Doi link may chu trong build.py -^> Firebase
echo   3) Build + day len GitHub Pages
echo ===============================================
echo Chi lam khi KHONG co hoc sinh dang lam bai.
set /p OK=Go CHUYEN de tiep tuc, phim khac de huy: 
if /i not "%OK%"=="CHUYEN" ( echo Da huy. & pause & exit /b 0 )
echo.
echo === 1/3 Dong bo du lieu ===
cd /d "%~dp0tools"
for /f "usebackq tokens=1,* delims==" %%a in ("migrate.keys.local") do set %%a=%%b
set GAS=https://script.google.com/macros/s/AKfycbyZ4UJgI763vPb4TZhKbKgxl6p-lGCQCJnZDqgCL9mHCVQpUzb4sbJGg89GLWSI-sQj/exec
set IMP=https://asia-southeast1-lms-learning-36841.cloudfunctions.net/importer
node migrate.js "%GAS%" "%EXPORT_KEY%" "%IMP%" "%IMPORT_KEY%"
if %errorlevel% neq 0 ( echo [LOI] Dong bo that bai - DUNG LAI, web cu van chay binh thuong. & pause & exit /b 1 )
cd /d "%~dp0"
echo.
echo === 2/3 Doi link may chu ===
if not exist ..\build.py.bak_apps copy ..\build.py ..\build.py.bak_apps >nul
python tools\set_api.py "%API%"
if %errorlevel% neq 0 ( pause & exit /b 1 )
echo.
echo === 3/3 Build + push GitHub ===
call ..\push_github.bat run

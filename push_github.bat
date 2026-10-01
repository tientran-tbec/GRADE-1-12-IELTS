@echo off
chcp 65001 >nul
cd /d %~dp0
setlocal enabledelayedexpansion
echo ===============================================
echo   BUILD + PUSH LEN GITHUB  (1 file duy nhat)
echo ===============================================

rem --- 1. Lan dau: hoi link repo GitHub, luu vao file .repo_url ---
if not exist .repo_url (
  echo Dan link repo GitHub MOI, vi du: https://github.com/tientran-tbec/TEN-REPO.git
  set /p REPO=Link repo: 
  echo !REPO!> .repo_url
)
set /p REPO=<.repo_url

rem --- 2. Build lai web ---
python update_links.py
if %errorlevel% neq 0 (
  echo [LOI] Build that bai - xem thong bao phia tren.
  pause & exit /b 1
)

rem --- 3. Git: khoi tao + gan remote ---
if not exist .git (
  git init
  git branch -M main
)
git remote remove origin >nul 2>&1
git remote add origin %REPO%

rem --- 4. Commit + push ---
git add -A
git commit -m "Cap nhat %date% %time%" >nul 2>&1
git push -u origin main
if %errorlevel% neq 0 (
  echo.
  echo Push bi tu choi (repo moi co the co noi dung khac). Ghi de bang ban nay?
  set /p OK=Go Y de ghi de, phim khac de huy: 
  if /i "!OK!"=="Y" git push -u origin main --force
)

rem --- 5. Suy ra link web + kiem tra trang that da co link Apps Script moi ---
set U=%REPO:https://github.com/=%
for /f "tokens=1,2 delims=/" %%a in ("%U%") do (set OWNER=%%a& set NAME=%%b)
set NAME=%NAME:.git=%
set WEB=https://%OWNER%.github.io/%NAME%/
echo.
echo Cho GitHub Pages cap nhat (~60 giay)...
timeout /t 60 /nobreak >nul
set LIVE=%WEB%WebBaiTap/Lop11/Unit2/botro/doc.html
curl -s -L "%LIVE%" | findstr /c:"sI-sQj" >nul
if %errorlevel%==0 (
  echo [OK] Trang that DA dung link Apps Script moi.
) else (
  echo [CHUA] Trang that chua co link moi - doi them 1-2 phut roi Ctrl+F5, hoac kiem tra Settings ^> Pages ^(Branch main / root^).
)
echo ===============================================
echo   Link web: %WEB%
echo ===============================================
start "" "%WEB%"
pause

@echo off
chcp 65001 >nul
cd /d %~dp0
echo ===============================================
echo   TU DONG TAO APPS SCRIPT MOI + NOI VAO WEB
echo ===============================================
where node >nul 2>nul
if %errorlevel% neq 0 (
  echo [LOI] May chua cai Node.js. Cai ban LTS tai https://nodejs.org roi chay lai file nay.
  start https://nodejs.org
  pause
  exit /b 1
)
echo.
echo BUOC 0 (chi lam 1 lan): bat "Google Apps Script API" tai trang sap mo ra (gat sang ON).
echo Neu da bat roi thi bo qua.
start https://script.google.com/home/usersettings
pause
if not exist "%USERPROFILE%\.clasprc.json" (
  echo Dang nhap Google - trinh duyet se mo, chon tai khoan tien.tbec...
  call npx -y @google/clasp@2.4.2 login
)
cd apps_script
if not exist .clasp.json (
  call npx -y @google/clasp@2.4.2 create --type standalone --title "GRADE-6-12 ket qua" --rootDir .
)
call npx -y @google/clasp@2.4.2 push -f
if %errorlevel% neq 0 ( echo [LOI] push that bai & pause & exit /b 1 )
for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "$o = (npx -y @google/clasp@2.4.2 deploy --description 'web' 2>&1 | Out-String); if ($o -match '- (AKfy[\w-]+)') { $matches[1] }"`) do set DEPID=%%i
cd ..
if "%DEPID%"=="" (
  echo [LOI] Khong lay duoc ma deploy. Mo Apps Script ^> Deploy ^> New deployment ^> Web app, roi dan link /exec vao: python update_links.py "link"
  pause
  exit /b 1
)
set URL=https://script.google.com/macros/s/%DEPID%/exec
echo Link Apps Script moi: %URL%
python update_links.py "%URL%"
echo.
echo CUOI CUNG (chi 1 lan): trinh duyet se mo link /exec. Neu Google hoi cap quyen thi bam
echo "Advanced" ^> "Go to ... (unsafe)" ^> Allow. Trang hien chu "ignored" la thanh cong.
start %URL%
echo.
echo Xong. Gio chay push_github.bat de dua web len GitHub.
pause

@echo off
chcp 65001 >nul
cd /d %~dp0
echo ===============================================
echo   BUILD + PUSH LEN GITHUB (tientran-tbec/GRADE-6-12)
echo ===============================================
python update_links.py
if %errorlevel% neq 0 (
  echo [CANH BAO] Build loi - kiem tra lai truoc khi push.
  pause
  exit /b 1
)
if not exist .git (
  git init
  git branch -M main
  git remote add origin https://github.com/tientran-tbec/GRADE-6-12.git
)
git add -A
git commit -m "Cap nhat %date% %time%"
if %errorlevel% neq 0 (
  echo (Khong co gi thay doi de commit)
)
git push -u origin main
echo ===============================================
echo   XONG. Link web: https://tientran-tbec.github.io/GRADE-6-12/
echo   (Lan dau: vao GitHub repo ^> Settings ^> Pages ^> Branch main / root)
echo ===============================================
pause

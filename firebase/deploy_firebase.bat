@echo off
chcp 65001 >nul
rem Build trang → public/, sao chép code.gs → functions/, rồi deploy lên Firebase.
cd /d "%~dp0"
call sync_code.bat
if not exist public mkdir public
echo === Build trang web ===
cd /d "%~dp0.."
python build.py
cd /d "%~dp0"
echo === Sao chép trang vào public ===
robocopy "%~dp0.." "%~dp0public" /MIR /XD firebase _backup_truoc_thuthach .git node_modules tests __pycache__ WebBaiTap /XF *.py *.bat *.zip code.gs tt_server.gs /NFL /NDL /NJH /NJS
call firebase deploy
pause

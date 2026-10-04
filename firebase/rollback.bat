@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo QUAY LAI Apps Script cu (build.py.bak_apps). Du lieu ghi tren Firebase tu luc chuyen se KHONG tu dong ve Sheets.
set /p OK=Go QUAYLAI de tiep tuc, phim khac de huy: 
if /i not "%OK%"=="QUAYLAI" ( echo Da huy. & pause & exit /b 0 )
if not exist ..\build.py.bak_apps ( echo Khong co ban sao luu build.py.bak_apps & pause & exit /b 1 )
copy /Y ..\build.py.bak_apps ..\build.py
call ..\push_github.bat run

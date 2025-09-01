@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion
cls

:: تعريف الألوان
for %%A in (31 32 33 34 35 36 37) do (
    set "color[%%A]=[%%A;1m"
)
set "color[0]=[0m"

:: الواجهة
echo ┏───────────────────────────────────┓
echo ┃ !color[31]!●!color[0]! !color[33]!●!color[0]! !color[32]!●!color[0]!                             ┃
echo ┣────────────┳──────────────────────┫
echo ┃ Developer  ^| Mohammed Al-Baqer    ┃
echo ┃ Copyright  ^| Copyright (c) 2025   ┃
echo ┗────────────┻──────────────────────┛ !color[0]!
echo.

:: تثبيت المكتبات
set PYTHON_CMD=python

if exist requirements.txt (
    echo !color[32]![INFO]!color[0]! Installing from requirements.txt...
    %PYTHON_CMD% -m pip install -r requirements.txt || goto install_default
) else (
    goto install_default
)

goto end

:install_default
echo !color[31]![ERROR]!color[0]! requirements.txt not found or error occurred.
echo !color[32]![INFO]!color[0]! Installing default libraries...
%PYTHON_CMD% -m pip install Cython keyboard

:end
echo.
echo !color[32]![INFO]!color[0]! All done successfully.
pause

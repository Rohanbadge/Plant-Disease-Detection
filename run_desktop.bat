@echo off
title Plant Disease Detector - Desktop GUI
cd /d "%~dp0"
python gui_desktop.py
if errorlevel 1 (
    echo.
    echo An error occurred. Press any key to exit.
    pause >nul
)


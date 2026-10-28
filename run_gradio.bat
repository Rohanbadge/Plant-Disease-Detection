@echo off
title Plant Disease Detector - Gradio Web App
cd /d "%~dp0"
python gradio_app.py
if errorlevel 1 (
    echo.
    echo An error occurred. Press any key to exit.
    pause >nul
)


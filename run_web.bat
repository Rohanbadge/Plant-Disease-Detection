@echo off
title Plant Disease Detector - Streamlit Web App
cd /d "%~dp0"
python -m streamlit run app.py
if errorlevel 1 (
    echo.
    echo An error occurred. Press any key to exit.
    pause >nul
)


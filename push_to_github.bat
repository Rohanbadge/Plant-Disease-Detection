@echo off
title Push Project to GitHub
cd /d "%~dp0"
echo ==============================================
echo Pushing Plant Disease Detection to GitHub...
echo ==============================================
git push -u origin main
if errorlevel 1 (
    echo.
    echo ==============================================
    echo If push failed:
    echo 1. Ensure you created the repository 'Plant-Disease-Detection'
    echo    at: https://github.com/new
    echo 2. Check your GitHub login credentials if prompted.
    echo ==============================================
) else (
    echo.
    echo ==============================================
    echo Project successfully pushed to GitHub!
    echo View at: https://github.com/Rohanbadge/Plant-Disease-Detection
    echo ==============================================
)
pause

@echo off
title SmartAssistant - FastAPI Server

echo =========================================
echo   SmartAssistant - FastAPI Server
echo =========================================
echo.

REM Get project directory
set "PROJECT_DIR=%~dp0"
set "PROJECT_DIR=%PROJECT_DIR:~0,-1%"

echo [INFO] Activating SmartAssistant environment...
call "%PROJECT_DIR%\activate_environment.bat"

if not exist "%PROJECT_DIR%\venv\Scripts\python.exe" (
    echo [ERROR] Virtual environment not found
    echo [INFO] Please run setup_environment.bat first
    pause
    exit /b 1
)

echo [INFO] Starting FastAPI server...
echo [INFO] Server will be available at: http://localhost:8000
echo [INFO] Press Ctrl+C to stop the server
echo.

"%PROJECT_DIR%\venv\Scripts\python.exe" "%PROJECT_DIR%\run.py"

pause

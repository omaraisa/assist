@echo off
title Progent - FastAPI Server

echo =========================================
echo   Progent - FastAPI
echo =========================================
echo.

REM Get the directory of this script
set "PROJECT_DIR=%~dp0Progent"

echo [INFO] Project Directory: %PROJECT_DIR%

REM Check if our self-contained environment exists
if exist "%PROJECT_DIR%\activate_environment.bat" (
    echo [INFO] Using self-contained environment...
    call "%PROJECT_DIR%\activate_environment.bat"
) else (
    echo [INFO] Using virtual environment...
    if exist "%PROJECT_DIR%\venv\Scripts\activate.bat" (
        call "%PROJECT_DIR%\venv\Scripts\activate.bat"
    ) else (
        echo [ERROR] No Python environment found!
        echo [INFO] Please run setup_environment.bat first to create a self-contained environment
        echo [INFO] Or manually create a virtual environment:
        echo [INFO]   python -m venv venv
        echo [INFO]   call venv\Scripts\activate.bat
        echo [INFO]   pip install -r requirements.txt
        pause
        exit /b 1
    )
)

echo [INFO] Environment activated successfully
echo.

REM Verify Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found in environment
    echo [INFO] Please check your environment setup
    pause
    exit /b 1
)

echo [INFO] Python version:
python --version
echo.

echo [INFO] Starting FastAPI server...
echo [INFO] Server will be available at: http://localhost:6060
echo [INFO] Press Ctrl+C to stop the server
echo.

REM Use the Python from our environment
if exist "%PROJECT_DIR%\venv\Scripts\python.exe" (
    "%PROJECT_DIR%\venv\Scripts\python.exe" "%PROJECT_DIR%\run.py"
) else (
    python "%PROJECT_DIR%\run.py"
)

echo.
echo [INFO] Server stopped
pause


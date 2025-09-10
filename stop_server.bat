@echo off
title ArcGIS Pro Smart Assistant - Stop Server

echo =========================================
echo   ArcGIS Pro Smart Assistant - Stop
echo =========================================
echo.

echo [INFO] Searching for running FastAPI server processes...

REM Find and kill Python processes running the FastAPI server
for /f "tokens=2" %%i in ('tasklist /fi "imagename eq python.exe" /fo csv ^| findstr "python.exe"') do (
    echo [INFO] Found Python process: %%i
    echo [INFO] Checking if it's running the FastAPI server...
    
    REM Check if this process is running our server by looking at the command line
    for /f "tokens=*" %%j in ('wmic process where "processid=%%~i" get commandline /value 2^>nul ^| findstr "run.py"') do (
        echo [INFO] Found FastAPI server process: %%i
        echo [INFO] Terminating process...
        taskkill /pid %%i /f >nul 2>&1
        if not errorlevel 1 (
            echo [SUCCESS] FastAPI server stopped successfully
        ) else (
            echo [WARNING] Failed to stop process %%i
        )
    )
)

REM Also try to kill by port (if the process is listening on port 6060)
echo [INFO] Checking for processes using port 6060...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":6060"') do (
    echo [INFO] Found process using port 6060: %%a
    taskkill /pid %%a /f >nul 2>&1
    if not errorlevel 1 (
        echo [SUCCESS] Process on port 6060 terminated
    ) else (
        echo [WARNING] Failed to terminate process %%a
    )
)

REM Alternative method: Kill by window title (if the server was started with a title)
echo [INFO] Looking for FastAPI server windows...
taskkill /f /fi "windowtitle eq Progent - FastAPI Server" >nul 2>&1
if not errorlevel 1 (
    echo [SUCCESS] FastAPI server window closed
)

echo.
echo [INFO] Server termination complete
echo [INFO] You can now safely restart the server if needed
echo.

pause

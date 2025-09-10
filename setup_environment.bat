@echo off
title Progent - Environment Setup
setlocal enabledelayedexpansion

set "TOTAL_STEPS=20"
set "CURRENT_STEP=0"

goto :main

:ProgressBar
set "PERCENT=%~1"
set "STEP=%~2"
powershell.exe -Command "& { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; $percent = [int]$env:PERCENT; $step = $env:STEP; Clear-Host; $fullBlocks = [math]::Floor($percent / 2); $hasPartial = $percent %% 2; $partialChar = if ($hasPartial) { '▌' } else { '' }; $empty = 50 - $fullBlocks - $hasPartial; $bar = ('█' * $fullBlocks) + $partialChar + ('░' * $empty); Write-Host '  ██████╗ ██████╗  ██████╗  ██████╗ ███████╗███╗   ██╗████████╗' -ForegroundColor Cyan; Write-Host '  ██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝' -ForegroundColor Cyan; Write-Host '  ██████╔╝██████╔╝██║   ██║██║  ███╗█████╗  ██╔██╗ ██║   ██║' -ForegroundColor Cyan; Write-Host '  ██╔═══╝ ██╔══██╗██║   ██║██║   ██║██╔══╝  ██║╚██╗██║   ██║' -ForegroundColor Cyan; Write-Host '  ██║     ██║  ██║╚██████╔╝╚██████╔╝███████╗██║ ╚████║   ██║' -ForegroundColor Cyan; Write-Host '  ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝' -ForegroundColor Cyan; Write-Host ''; Write-Host '==========================================' -ForegroundColor Cyan; Write-Host '  Environment Setup' -ForegroundColor Cyan; Write-Host '==========================================' -ForegroundColor Cyan; Write-Host ''; Write-Host \"Progress: [$bar] $percent%%\" -ForegroundColor Green; Write-Host ''; Write-Host \"Current step: $step\" -ForegroundColor Yellow; }"
goto :eof

:main
echo ==========================================
echo   Progent Environment Setup
echo ==========================================
echo.

REM Get the directory of this script
set "PROJECT_DIR=%~dp0Progent"

echo [INFO] Project Directory: %PROJECT_DIR%
echo.

set /a "CURRENT_STEP+=3"
set /a "PERCENTAGE=(CURRENT_STEP*100)/TOTAL_STEPS"
call :ProgressBar !PERCENTAGE! "Checking Python environment..."

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo [INFO] Please install Python 3.8 or higher from https://python.org
    pause
    exit /b 1
)

echo [INFO] Found Python version:
python --version

REM Check Python version (minimum 3.8)
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
for /f "tokens=1,2 delims=." %%a in ("%PYTHON_VERSION%") do (
    set MAJOR=%%a
    set MINOR=%%b
)

if %MAJOR% lss 3 (
    echo [ERROR] Python version must be 3.8 or higher
    pause
    exit /b 1
)
if %MAJOR% equ 3 if %MINOR% lss 8 (
    echo [ERROR] Python version must be 3.8 or higher
    pause
    exit /b 1
)

echo [INFO] Python version is compatible
echo.

REM Backup old virtual environment if it exists
if exist "%PROJECT_DIR%\venv" (
    echo [INFO] Backing up existing virtual environment...
    if exist "%PROJECT_DIR%\venv_backup" (
        rmdir /s /q "%PROJECT_DIR%\venv_backup" 2>nul
    )
    move "%PROJECT_DIR%\venv" "%PROJECT_DIR%\venv_backup" >nul 2>&1
    echo [INFO] Old environment backed up to venv_backup
    echo.
)

REM Create new virtual environment with system Python
set /a "CURRENT_STEP+=2"
set /a "PERCENTAGE=(CURRENT_STEP*100)/TOTAL_STEPS"
call :ProgressBar !PERCENTAGE! "Creating Python virtual environment..."
python -m venv "%PROJECT_DIR%\venv"

if errorlevel 1 (
    echo [ERROR] Failed to create virtual environment
    echo [INFO] Make sure you have the 'venv' module installed
    echo [INFO] Try: python -m pip install --user virtualenv
    pause
    exit /b 1
)

echo [INFO] Virtual environment created successfully
echo.

REM Activate the new environment
echo [INFO] Activating virtual environment...
call "%PROJECT_DIR%\venv\Scripts\activate.bat"

if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment
    pause
    exit /b 1
)

echo [INFO] Virtual environment activated
echo.

REM Upgrade pip
set /a "CURRENT_STEP+=2"
set /a "PERCENTAGE=(CURRENT_STEP*100)/TOTAL_STEPS"
call :ProgressBar !PERCENTAGE! "Upgrading pip package manager..."
python -m pip install --upgrade pip

REM Install requirements
set /a "CURRENT_STEP+=3"
set /a "PERCENTAGE=(CURRENT_STEP*100)/TOTAL_STEPS"
call :ProgressBar !PERCENTAGE! "Installing required Python packages..."
set "INSTALL_SUCCESS=0"

if exist "%PROJECT_DIR%\requirements.txt" (
    echo [INFO] Found requirements.txt, installing packages...
    echo [INFO] Attempting to install with pre-compiled binaries only...
    pip install -r "%PROJECT_DIR%\requirements.txt" --only-binary=:all: --no-cache-dir
    if not errorlevel 1 (
        set "INSTALL_SUCCESS=1"
        echo [SUCCESS] Requirements installed successfully with pre-compiled binaries
    ) else (
        echo [WARNING] Pre-compiled installation failed, trying with fallback strategy...
        pip install -r "%PROJECT_DIR%\requirements.txt" --prefer-binary --no-cache-dir
        if not errorlevel 1 (
            set "INSTALL_SUCCESS=1"
            echo [SUCCESS] Requirements installed successfully with fallback strategy
        ) else (
            echo [WARNING] Requirements installation had issues
            echo.
            echo [ERROR]    Some of the system required libraries failed to install automatically.
            echo [WHY]      This commonly happens when using a very recent Python version.
            echo            Developers of these open source libraries may not have released compatible versions for new Python releases,
            echo.
            echo [RECOMMENDATION] Please install an earlier version of Python and re-run this setup. This will use prebuilt wheels
            echo              and avoid lengthy/failed builds. Simple steps for non-experts:
            echo.
            echo    1 Download and install Python 3.11 from: https://www.python.org/downloads/release/python-311/
            echo    2 Re-run the setup using the 3.11 launcher:  py -3.11 setup_environment.bat
            echo.
            pause
        )
    )
) else (
    echo [WARNING] requirements.txt not found
)

REM Install core packages explicitly if requirements failed or doesn't exist
if "%INSTALL_SUCCESS%"=="0" (
    echo [INFO] Installing core packages explicitly...
    echo [INFO] Installing FastAPI...
    pip install fastapi
    if errorlevel 1 (
        echo [ERROR] Failed to install FastAPI
        pause
        exit /b 1
    )
    
    echo [INFO] Installing Uvicorn...
    pip install uvicorn[standard]
    if errorlevel 1 (
        echo [ERROR] Failed to install Uvicorn
        pause
        exit /b 1
    )
    
    echo [INFO] Installing additional packages...
    echo [INFO] Trying to install packages with pre-compiled binaries...
    pip install python-multipart jinja2 aiofiles pydantic-settings --only-binary=:all: --no-cache-dir
    
    echo [INFO] Installing aiohttp with fallback strategy...
    pip install aiohttp --only-binary=:all: --no-cache-dir
    if errorlevel 1 (
        echo [WARNING] Pre-compiled aiohttp failed, trying compatible version...
        pip install aiohttp==3.10.11 --only-binary=:all: --no-cache-dir
        if errorlevel 1 (
            echo [WARNING] Trying older stable version...
            pip install aiohttp==3.6.2 --only-binary=:all: --no-cache-dir
            if errorlevel 1 (
                echo [WARNING] Installing aiohttp without binary restriction...
                pip install aiohttp --prefer-binary --no-cache-dir
                if errorlevel 1 (
                    echo [WARNING] aiohttp installation failed, skipping...
                )
            )
        )
    )
    
    echo [SUCCESS] Core packages installed
)

REM Verify critical packages are available
set /a "CURRENT_STEP+=3"
set /a "PERCENTAGE=(CURRENT_STEP*100)/TOTAL_STEPS"
call :ProgressBar !PERCENTAGE! "Verifying core package installations..."
python -c "import fastapi; print('FastAPI: OK')" 2>nul
if errorlevel 1 (
    echo [ERROR] FastAPI not available after installation
    echo [INFO] Attempting to reinstall FastAPI...
    pip install --force-reinstall fastapi
)

python -c "import uvicorn; print('Uvicorn: OK')" 2>nul
if errorlevel 1 (
    echo [ERROR] Uvicorn not available after installation
    echo [INFO] Attempting to reinstall Uvicorn...
    pip install --force-reinstall uvicorn[standard]
)

REM Verify aiohttp is available
python -c "import aiohttp; print('aiohttp: OK')" 2>nul
if errorlevel 1 (
    echo [WARNING] aiohttp not available, attempting to install...
    pip install aiohttp --only-binary=:all: --no-cache-dir 2>nul
    if errorlevel 1 (
        echo [INFO] Trying aiohttp with compatible version...
        pip install aiohttp==3.10.11 --only-binary=:all: --no-cache-dir 2>nul
        if errorlevel 1 (
            echo [INFO] Trying older stable version...
            pip install aiohttp==3.6.2 --only-binary=:all: --no-cache-dir 2>nul
            if errorlevel 1 (
                echo [WARNING] aiohttp installation failed - some features may be limited
            )
        )
    )
)

REM Verify pydantic-settings is available
python -c "import pydantic_settings; print('pydantic-settings: OK')" 2>nul
if errorlevel 1 (
    echo [WARNING] pydantic-settings not available, attempting to install...
    pip install pydantic-settings --only-binary=:all: --no-cache-dir 2>nul
    if errorlevel 1 (
        echo [INFO] Trying pydantic-settings without binary restriction...
        pip install pydantic-settings --prefer-binary --no-cache-dir 2>nul
        if errorlevel 1 (
            echo [WARNING] pydantic-settings installation failed - configuration features may be limited
        )
    )
)

echo.

echo.

REM Create/update environment activation script
set /a "CURRENT_STEP+=2"
set /a "PERCENTAGE=(CURRENT_STEP*100)/TOTAL_STEPS"
call :ProgressBar !PERCENTAGE! "Creating activation script..."

(
echo @echo off
echo REM Progent Environment Activation Script
echo REM This script ensures the project uses its own Python environment
echo.
echo set "PROJECT_DIR=%PROJECT_DIR%"
echo set "OLD_PATH=%%PATH%%"
echo set "OLD_PYTHONPATH=%%PYTHONPATH%%"
echo.

REM Set environment variables for this project
echo set "PATH=%%PROJECT_DIR%%\venv\Scripts;%%PROJECT_DIR%%\venv;%%PATH%%"
echo set "PYTHONPATH=%%PROJECT_DIR%%;%%PROJECT_DIR%%\app;%%PYTHONPATH%%"
echo set "VIRTUAL_ENV=%%PROJECT_DIR%%\venv"
echo set "VIRTUAL_ENV_PROMPT=^(Progent^) "
echo.

REM Update command prompt
echo if not defined PROMPT set PROMPT=$P$G
echo if defined _OLD_VIRTUAL_PROMPT set PROMPT=%%_OLD_VIRTUAL_PROMPT%%
echo set "_OLD_VIRTUAL_PROMPT=%%PROMPT%%"
echo set "PROMPT=^(Progent^) %%PROMPT%%"
echo.
echo echo Progent Environment Activated
echo echo Project Directory: %%PROJECT_DIR%%
echo echo Python: %%PROJECT_DIR%%\venv\Scripts\python.exe
echo.
) > "%PROJECT_DIR%\activate_environment.bat"

echo [SUCCESS] Enhanced activation script created: activate_environment.bat
echo.

REM Create a startup script for the server
set /a "CURRENT_STEP+=2"
set /a "PERCENTAGE=(CURRENT_STEP*100)/TOTAL_STEPS"
call :ProgressBar !PERCENTAGE! "Creating server startup script..."

(
echo @echo off
echo title Progent - FastAPI Server
echo.
echo echo ==========================================
echo echo   Progent - FastAPI Server
echo echo ==========================================
echo echo.
echo.
echo REM Get project directory
echo set "PROJECT_DIR=%%~dp0"
echo set "PROJECT_DIR=%%PROJECT_DIR:~0,-1%%"
echo.
echo echo [INFO] Activating Progent environment...
echo call "%%PROJECT_DIR%%\activate_environment.bat"
echo.
echo if not exist "%%PROJECT_DIR%%\venv\Scripts\python.exe" ^(
echo     echo [ERROR] Virtual environment not found!
echo     echo [INFO] Please run setup_environment.bat first
echo     pause
echo     exit /b 1
echo ^)
echo.
echo echo [INFO] Starting FastAPI server...
echo echo [INFO] Server will be available at: http://localhost:6060
echo echo [INFO] Press Ctrl+C to stop the server
echo echo.
echo.
echo "%%PROJECT_DIR%%\venv\Scripts\python.exe" "%%PROJECT_DIR%%\run.py"
echo.
echo pause
) > "%PROJECT_DIR%\start_progent.bat"

echo [SUCCESS] Server startup script created: start_progent.bat
echo.

REM Create project information file
echo [INFO] Creating project information file...

(
echo # Progent Environment Information
echo # Generated on %date% %time%
echo.

echo PROJECT_DIR=%PROJECT_DIR%
echo PYTHON_VERSION=%PYTHON_VERSION%
echo VIRTUAL_ENV=%PROJECT_DIR%\venv
echo.

REM To activate this environment:
REM call activate_environment.bat

REM To start the server:
REM call start_progent.bat  

REM This environment is now independent of system Python installation
) > "%PROJECT_DIR%\environment_info.txt"

echo [SUCCESS] Project information saved to: environment_info.txt
echo.

REM Test the installation
set /a "CURRENT_STEP+=3"
set /a "PERCENTAGE=(CURRENT_STEP*100)/TOTAL_STEPS"
call :ProgressBar !PERCENTAGE! "Finalizing and testing installation..."
echo.

python -c "import sys; print('Python executable:', sys.executable)"
python -c "import sys; print('Python version:', sys.version)"

python -c "import fastapi; print('FastAPI: Available -', fastapi.__version__)" 2>nul || echo FastAPI: NOT AVAILABLE - Installation failed!

python -c "import uvicorn; print('Uvicorn: Available -', uvicorn.__version__)" 2>nul || echo Uvicorn: NOT AVAILABLE - Installation failed!

python -c "import aiohttp; print('aiohttp: Available -', aiohttp.__version__)" 2>nul || echo aiohttp: NOT AVAILABLE - Some features may be limited

python -c "import pydantic_settings; print('pydantic-settings: Available -', pydantic_settings.__version__)" 2>nul || echo pydantic-settings: NOT AVAILABLE - Configuration features may be limited

REM Check if core packages are missing and provide guidance
python -c "import fastapi, uvicorn; print('\nSUCCESS: All critical packages are available')" 2>nul
if errorlevel 1 (
    echo.
    echo [ERROR] Critical packages are missing!
    echo [INFO] Please run the following command manually:
    echo [INFO] %PROJECT_DIR%\venv\Scripts\activate.bat
    echo [INFO] pip install fastapi uvicorn[standard] python-multipart
    echo.
    pause
    exit /b 1
)
    echo [INFO] pip install fastapi uvicorn[standard] python-multipart
    echo.
    pause
    exit /b 1
)

echo.

echo   ██████╗ ██████╗  ██████╗  ██████╗ ███████╗███╗   ██╗████████╗
echo   ██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝
echo   ██████╔╝██████╔╝██║   ██║██║  ███╗█████╗  ██╔██╗ ██║   ██║
echo   ██╔═══╝ ██╔══██╗██║   ██║██║   ██║██╔══╝  ██║╚██╗██║   ██║
echo   ██║     ██║  ██║╚██████╔╝╚██████╔╝███████╗██║ ╚████║   ██║
echo   ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝
echo.
echo =========================================
echo   Installation Complete!
echo =========================================
echo.
echo You can now run the server using the start_server.bat script.
echo.
echo Press any key to exit...
pause >nul


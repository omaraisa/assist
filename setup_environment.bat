@echo off
title SmartAssistant - Environment Setup
setlocal enabledelayedexpansion

echo =========================================
echo   SmartAssistant Environment Setup
echo =========================================
echo.

REM Get the directory of this script
set "PROJECT_DIR=%~dp0"
set "PROJECT_DIR=%PROJECT_DIR:~0,-1%"

echo [INFO] Project Directory: %PROJECT_DIR%
echo.

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
echo [INFO] Creating new virtual environment with system Python...
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
echo [INFO] Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo [INFO] Installing project requirements...
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
    )      echo [INFO] Installing additional packages...
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
echo [INFO] Verifying package installation...
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

REM Try to install arcpy if available
echo [INFO] Attempting to install ArcPy support...
echo [INFO] Note: ArcPy requires ArcGIS Pro to be installed on the system

REM Check if ArcGIS Pro is installed by looking for common installation paths
set "ARCGIS_PRO_PATH="
if exist "C:\Program Files\ArcGIS\Pro\bin\Python\Scripts\propy.bat" (
    set "ARCGIS_PRO_PATH=C:\Program Files\ArcGIS\Pro"
) else if exist "C:\ArcGIS\Pro\bin\Python\Scripts\propy.bat" (
    set "ARCGIS_PRO_PATH=C:\ArcGIS\Pro"
)

if defined ARCGIS_PRO_PATH (
    echo [INFO] Found ArcGIS Pro installation at: %ARCGIS_PRO_PATH%
    echo [INFO] Installing ArcPy package...
    
    REM Try different methods to install arcpy
    pip install arcpy 2>nul
    if errorlevel 1 (
        echo [INFO] Standard arcpy installation failed, trying alternative method...
        REM Try to install from ArcGIS Pro conda environment
        if exist "%ARCGIS_PRO_PATH%\bin\Python\Scripts\conda.exe" (
            "%ARCGIS_PRO_PATH%\bin\Python\Scripts\conda.exe" install -c esri arcpy -y 2>nul
        )
    )
    
    REM Test if arcpy is available
    python -c "import arcpy; print('ArcPy successfully installed')" 2>nul
    if not errorlevel 1 (
        echo [SUCCESS] ArcPy is available in the environment
    ) else (
        echo [WARNING] ArcPy installation may have issues
        echo [INFO] The project will still work, but spatial functions may be limited
        echo [INFO] To use full GIS functionality, run the connector from within ArcGIS Pro
    )
) else (
    echo [WARNING] ArcGIS Pro not found in standard locations
    echo [INFO] The project will work without ArcPy, but spatial functions will be limited
    echo [INFO] To use full GIS functionality, run the connector from within ArcGIS Pro
)

echo.

REM Create/update environment activation script
echo [INFO] Creating enhanced activation script...

(
echo @echo off
echo REM SmartAssistant Environment Activation Script
echo REM This script ensures the project uses its own Python environment
echo.
echo set "PROJECT_DIR=%PROJECT_DIR%"
echo set "OLD_PATH=%%PATH%%"
echo set "OLD_PYTHONPATH=%%PYTHONPATH%%"
echo.
echo REM Set environment variables for this project
echo set "PATH=%%PROJECT_DIR%%\venv\Scripts;%%PROJECT_DIR%%\venv;%%PATH%%"
echo set "PYTHONPATH=%%PROJECT_DIR%%;%%PROJECT_DIR%%\app;%%PYTHONPATH%%"
echo set "VIRTUAL_ENV=%%PROJECT_DIR%%\venv"
echo set "VIRTUAL_ENV_PROMPT=^(SmartAssistant^) "
echo.
echo REM Update command prompt
echo if not defined PROMPT set PROMPT=$P$G
echo if defined _OLD_VIRTUAL_PROMPT set PROMPT=%%_OLD_VIRTUAL_PROMPT%%
echo set "_OLD_VIRTUAL_PROMPT=%%PROMPT%%"
echo set "PROMPT=^(SmartAssistant^) %%PROMPT%%"
echo.
echo echo SmartAssistant Environment Activated
echo echo Project Directory: %%PROJECT_DIR%%
echo echo Python: %%PROJECT_DIR%%\venv\Scripts\python.exe
echo echo.
) > "%PROJECT_DIR%\activate_environment.bat"

echo [SUCCESS] Enhanced activation script created: activate_environment.bat
echo.

REM Create a startup script for the server
echo [INFO] Creating server startup script...

(
echo @echo off
echo title SmartAssistant - FastAPI Server
echo.
echo echo =========================================
echo echo   SmartAssistant - FastAPI Server
echo echo =========================================
echo echo.
echo.
echo REM Get project directory
echo set "PROJECT_DIR=%%~dp0"
echo set "PROJECT_DIR=%%PROJECT_DIR:~0,-1%%"
echo.
echo echo [INFO] Activating SmartAssistant environment...
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
echo echo [INFO] Server will be available at: http://localhost:8000
echo echo [INFO] Press Ctrl+C to stop the server
echo echo.
echo.
echo "%%PROJECT_DIR%%\venv\Scripts\python.exe" "%%PROJECT_DIR%%\run.py"
echo.
echo pause
) > "%PROJECT_DIR%\start_smartassistant.bat"

echo [SUCCESS] Server startup script created: start_smartassistant.bat
echo.

REM Create ArcGIS connector launcher
echo [INFO] Creating ArcGIS Pro connector launcher...

(
echo @echo off
echo title SmartAssistant - ArcGIS Pro Connector
echo.
echo echo =========================================
echo echo   SmartAssistant - ArcGIS Pro Connector  
echo echo =========================================
echo echo.
echo.
echo REM Get project directory
echo set "PROJECT_DIR=%%~dp0"  
echo set "PROJECT_DIR=%%PROJECT_DIR:~0,-1%%"
echo.
echo echo [INFO] This script should be run from within ArcGIS Pro
echo echo [INFO] Copy and paste this command in ArcGIS Pro Python console:
echo echo.
echo echo exec^(open^(r"%%PROJECT_DIR%%\arcgis_connector.py"^).read^(^)^)
echo echo.
echo echo [INFO] Or run this file directly from ArcGIS Pro Python environment
echo echo.
echo.
echo REM Check if we're in ArcGIS Pro environment
echo python -c "import arcpy; print('ArcGIS Pro environment detected')" 2^>nul
echo if not errorlevel 1 ^(
echo     echo [INFO] Running connector...
echo     python "%%PROJECT_DIR%%\arcgis_connector.py"
echo ^) else ^(
echo     echo [WARNING] Not in ArcGIS Pro environment
echo     echo [INFO] Please run from ArcGIS Pro Python console or as a script tool
echo ^)
echo.
echo pause
) > "%PROJECT_DIR%\connect_arcgis.bat"

echo [SUCCESS] ArcGIS Pro connector launcher created: connect_arcgis.bat
echo.

REM Create project information file
echo [INFO] Creating project information file...

(
echo # SmartAssistant Environment Information
echo # Generated on %date% %time%
echo.
echo PROJECT_DIR=%PROJECT_DIR%
echo PYTHON_VERSION=%PYTHON_VERSION%
echo VIRTUAL_ENV=%PROJECT_DIR%\venv
echo.
echo # To activate this environment:
echo # call activate_environment.bat
echo.
echo # To start the server:
echo # call start_smartassistant.bat  
echo.
echo # To connect ArcGIS Pro:
echo # call connect_arcgis.bat
echo.
echo # This environment is now independent of ArcGIS Pro Python installation
) > "%PROJECT_DIR%\environment_info.txt"

echo [SUCCESS] Project information saved to: environment_info.txt
echo.

REM Test the installation
echo [INFO] Testing the installation...
echo.

python -c "
import sys
print('Python executable:', sys.executable)
print('Python version:', sys.version)
print('Virtual environment:', hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

try:
    import fastapi
    print('FastAPI: Available -', fastapi.__version__)
except ImportError:
    print('FastAPI: NOT AVAILABLE - Installation failed!')

try:
    import uvicorn  
    print('Uvicorn: Available -', uvicorn.__version__)
except ImportError:
    print('Uvicorn: NOT AVAILABLE - Installation failed!')

try:
    import aiohttp
    print('aiohttp: Available -', aiohttp.__version__)
except ImportError:
    print('aiohttp: NOT AVAILABLE - Some features may be limited')

try:
    import pydantic_settings
    print('pydantic-settings: Available -', pydantic_settings.__version__)
except ImportError:
    print('pydantic-settings: NOT AVAILABLE - Configuration features may be limited')

try:
    import arcpy
    print('ArcPy: Available')
except ImportError:
    print('ArcPy: Not available (will work with limited functionality)')
"

REM Check if core packages are missing and provide guidance
python -c "
import sys
missing = []
try:
    import fastapi
except ImportError:
    missing.append('fastapi')
try:
    import uvicorn
except ImportError:
    missing.append('uvicorn')

if missing:
    print()
    print('ERROR: Critical packages missing:', ', '.join(missing))
    print('Manual installation command:')
    print('pip install ' + ' '.join(missing))
    sys.exit(1)
else:
    print()
    print('SUCCESS: All critical packages are available')
"

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

echo.
echo =========================================
echo   Setup Complete!
echo =========================================
echo.
echo [SUCCESS] SmartAssistant environment is now self-contained
echo.
echo Next steps:
echo 1. To start the server: call start_smartassistant.bat
echo 2. To connect ArcGIS Pro: call connect_arcgis.bat  
echo 3. To manually activate environment: call activate_environment.bat
echo.
echo The project is now independent of external Python installations
echo and can be copied to other machines with the same setup.
echo.
pause

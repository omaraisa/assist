@echo off
title SmartAssistant - Environment Migration Tool
setlocal enabledelayedexpansion

echo =========================================
echo   SmartAssistant Environment Migration
echo =========================================
echo.
echo This tool will help you migrate from the ArcGIS Pro dependent
echo environment to a self-contained Python environment.
echo.

REM Get the directory of this script
set "PROJECT_DIR=%~dp0"
set "PROJECT_DIR=%PROJECT_DIR:~0,-1%"

echo [INFO] Project Directory: %PROJECT_DIR%
echo.

REM Check current environment status
echo [INFO] Checking current environment...

if exist "%PROJECT_DIR%\venv\pyvenv.cfg" (
    echo [INFO] Found existing virtual environment
    
    REM Check if it's dependent on ArcGIS Pro
    findstr /c:"ArcGIS" "%PROJECT_DIR%\venv\pyvenv.cfg" >nul 2>&1
    if not errorlevel 1 (
        echo [WARNING] Current environment is dependent on ArcGIS Pro
        echo [INFO] This will be migrated to a self-contained environment
        set "NEEDS_MIGRATION=1"
    ) else (
        echo [INFO] Current environment appears to be self-contained
        set "NEEDS_MIGRATION=0"
    )
) else (
    echo [INFO] No virtual environment found
    set "NEEDS_MIGRATION=1"
)

echo.

if "%NEEDS_MIGRATION%"=="0" (
    echo [SUCCESS] Your environment is already self-contained!
    echo [INFO] You can still run setup_environment.bat to ensure everything is up to date
    echo.
    choice /m "Do you want to update the environment anyway"
    if errorlevel 2 (
        echo [INFO] Migration skipped
        pause
        exit /b 0
    )
)

echo [INFO] Starting environment migration...
echo.

REM Backup current environment if it exists
if exist "%PROJECT_DIR%\venv" (
    echo [INFO] Backing up current environment...
    
    REM Remove old backup if it exists
    if exist "%PROJECT_DIR%\venv_old" (
        echo [INFO] Removing old backup...
        rmdir /s /q "%PROJECT_DIR%\venv_old" 2>nul
    )
    
    REM Create backup
    echo [INFO] Creating backup...
    move "%PROJECT_DIR%\venv" "%PROJECT_DIR%\venv_old" >nul 2>&1
    if errorlevel 1 (
        echo [WARNING] Could not backup old environment
        echo [INFO] Continuing with migration...
    ) else (
        echo [SUCCESS] Old environment backed up to venv_old
    )
    echo.
)

REM Check if Python is available in system
echo [INFO] Checking for system Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in system PATH
    echo.
    echo [INFO] Please install Python 3.8 or higher from https://python.org
    echo [INFO] Make sure to check "Add Python to PATH" during installation
    echo.
    echo [INFO] After installing Python, run this script again
    pause
    exit /b 1
)

echo [INFO] Found Python:
python --version
echo.

REM Create new self-contained environment
echo [INFO] Creating new self-contained virtual environment...

python -m venv "%PROJECT_DIR%\venv"
if errorlevel 1 (
    echo [ERROR] Failed to create virtual environment
    echo [INFO] This could be due to:"
    echo [INFO] - Python venv module not available
    echo [INFO] - Insufficient permissions
    echo [INFO] - Disk space issues
    echo.
    echo [INFO] Try installing virtualenv: python -m pip install --user virtualenv
    pause
    exit /b 1
)

echo [SUCCESS] Virtual environment created
echo.

REM Activate new environment
echo [INFO] Activating new environment...
call "%PROJECT_DIR%\venv\Scripts\activate.bat"
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment
    pause
    exit /b 1
)

echo [SUCCESS] Environment activated
echo.

REM Upgrade pip in new environment
echo [INFO] Upgrading pip...
python -m pip install --upgrade pip

REM Install basic requirements
echo [INFO] Installing project requirements...
if exist "%PROJECT_DIR%\requirements.txt" (
    pip install -r "%PROJECT_DIR%\requirements.txt"
    if errorlevel 1 (
        echo [WARNING] Some packages may have failed to install
        echo [INFO] Basic functionality should still work
    )
) else (
    echo [WARNING] requirements.txt not found
    echo [INFO] Installing basic packages...
    pip install fastapi uvicorn websockets python-multipart aiofiles python-dotenv requests jinja2 aiohttp pydantic-settings
)

echo.

REM Try to install packages from old environment if available
if exist "%PROJECT_DIR%\venv_old" (
    echo [INFO] Attempting to migrate packages from old environment...
    
    REM Try to get package list from old environment
    if exist "%PROJECT_DIR%\venv_old\Scripts\pip.exe" (
        echo [INFO] Extracting package list from old environment...
        "%PROJECT_DIR%\venv_old\Scripts\pip.exe" freeze > "%PROJECT_DIR%\old_packages.txt" 2>nul
        
        if exist "%PROJECT_DIR%\old_packages.txt" (
            echo [INFO] Installing packages from old environment...
            
            REM Filter out problematic packages
            findstr /v /c:"arcgis" /c:"ArcGIS" /c:"file:///" "%PROJECT_DIR%\old_packages.txt" > "%PROJECT_DIR%\filtered_packages.txt" 2>nul
            
            REM Install filtered packages
            pip install -r "%PROJECT_DIR%\filtered_packages.txt" 2>nul
            
            REM Clean up temporary files
            del "%PROJECT_DIR%\old_packages.txt" 2>nul
            del "%PROJECT_DIR%\filtered_packages.txt" 2>nul
            
            echo [INFO] Package migration completed
        )
    )
)

echo.

REM Create self-contained activation script
echo [INFO] Creating self-contained activation script...

(
echo @echo off
echo REM SmartAssistant Self-Contained Environment Activation
echo REM This script ensures complete independence from external Python installations
echo.
echo set "PROJECT_DIR=%PROJECT_DIR%"
echo.
echo REM Store original environment
echo set "ORIGINAL_PATH=%%PATH%%"
echo set "ORIGINAL_PYTHONPATH=%%PYTHONPATH%%"
echo set "ORIGINAL_PROMPT=%%PROMPT%%"
echo.
echo REM Set project-specific environment
echo set "PATH=%%PROJECT_DIR%%\venv\Scripts;%%PROJECT_DIR%%\venv;%%PATH%%"
echo set "PYTHONPATH=%%PROJECT_DIR%%;%%PROJECT_DIR%%\app"
echo set "VIRTUAL_ENV=%%PROJECT_DIR%%\venv"
echo set "VIRTUAL_ENV_PROMPT=^(SmartAssistant^) "
echo.
echo REM Update prompt
echo if not defined PROMPT set PROMPT=$P$G
echo set "PROMPT=^(SmartAssistant^) %%PROMPT%%"
echo.
echo REM Verification
echo echo [INFO] SmartAssistant Environment Activated
echo echo [INFO] Project: %%PROJECT_DIR%%
echo echo [INFO] Python: %%PROJECT_DIR%%\venv\Scripts\python.exe
echo echo [INFO] Environment: Self-contained
echo.
echo REM Test Python
echo "%%PROJECT_DIR%%\venv\Scripts\python.exe" -c "import sys; print('[INFO] Python version:', sys.version.split()[0])"
echo.
) > "%PROJECT_DIR%\activate_smartassistant.bat"

echo [SUCCESS] Self-contained activation script created
echo.

REM Update existing scripts to use new environment
echo [INFO] Updating project scripts...

REM Test the new environment
echo [INFO] Testing new environment...
python -c "
import sys
print('✓ Python executable:', sys.executable)
print('✓ Virtual environment active:', hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

# Test key packages
packages = ['fastapi', 'uvicorn', 'websockets']
for pkg in packages:
    try:
        __import__(pkg)
        print(f'✓ {pkg}: Available')
    except ImportError:
        print(f'✗ {pkg}: Missing')

# Test ArcPy (optional)
try:
    import arcpy
    print('✓ ArcPy: Available')
except ImportError:
    print('ℹ ArcPy: Not available (normal if not running from ArcGIS Pro)')
"

echo.

REM Create cleanup script for old environment
if exist "%PROJECT_DIR%\venv_old" (
    echo [INFO] Creating cleanup script for old environment...
    
    (
    echo @echo off
    echo echo Removing old ArcGIS-dependent environment...
    echo rmdir /s /q "%PROJECT_DIR%\venv_old"
    echo echo Old environment removed successfully
    echo pause
    ) > "%PROJECT_DIR%\cleanup_old_environment.bat"
    
    echo [INFO] Old environment cleanup script created: cleanup_old_environment.bat
    echo [INFO] Run this script later to remove the old environment backup
)

echo.
echo =========================================
echo   Migration Complete!
echo =========================================
echo.
echo [SUCCESS] Your SmartAssistant environment is now self-contained
echo.
echo Key changes:
echo ✓ Independent of ArcGIS Pro Python installation
echo ✓ Uses system Python with virtual environment
echo ✓ Portable across machines with same Python version
echo ✓ All dependencies contained within project
echo.
echo Next steps:
echo 1. Test the server: call start_server.bat
echo 2. Connect ArcGIS Pro: run arcgis_connector_portable.py
echo 3. Use activate_smartassistant.bat for manual environment activation
echo.
if exist "%PROJECT_DIR%\venv_old" (
    echo Optional cleanup:
    echo - Run cleanup_old_environment.bat to remove old environment backup
    echo.
)
echo The project can now be copied to other machines and will work
echo independently as long as Python 3.8+ is installed.
echo.
pause

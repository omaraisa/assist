@echo off
REM SmartAssistant Self-Contained Environment Activation
REM This script ensures complete independence from external Python installations

set "PROJECT_DIR=C:\Users\oelhag\Documents\MEGA\ProAI\SmartAssistant\BaseAssistant\SmartAssistantFastAPI"

REM Store original environment
set "ORIGINAL_PATH=%PATH%"
set "ORIGINAL_PYTHONPATH=%PYTHONPATH%"
set "ORIGINAL_PROMPT=%PROMPT%"

REM Set project-specific environment
set "PATH=%PROJECT_DIR%\venv\Scripts;%PROJECT_DIR%\venv;%PATH%"
set "PYTHONPATH=%PROJECT_DIR%;%PROJECT_DIR%\app"
set "VIRTUAL_ENV=%PROJECT_DIR%\venv"
set "VIRTUAL_ENV_PROMPT=^(SmartAssistant^) "

REM Update prompt
if not defined PROMPT set PROMPT=$P$G
set "PROMPT=^(SmartAssistant^) %PROMPT%"

REM Verification
echo [INFO] SmartAssistant Environment Activated
echo [INFO] Project: %PROJECT_DIR%
echo [INFO] Python: %PROJECT_DIR%\venv\Scripts\python.exe
echo [INFO] Environment: Self-contained

REM Test Python
"%PROJECT_DIR%\venv\Scripts\python.exe" -c "import sys; print('[INFO] Python version:', sys.version.split()[0])"


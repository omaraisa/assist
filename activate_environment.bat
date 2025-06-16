@echo off
REM SmartAssistant Environment Activation Script
REM This script ensures the project uses its own Python environment

set "PROJECT_DIR=E:\ai_stage\smart_assistant"
set "OLD_PATH=%PATH%"
set "OLD_PYTHONPATH=%PYTHONPATH%"

REM Set environment variables for this project
set "PATH=%PROJECT_DIR%\venv\Scripts;%PROJECT_DIR%\venv;%PATH%"
set "PYTHONPATH=%PROJECT_DIR%;%PROJECT_DIR%\app;%PYTHONPATH%"
set "VIRTUAL_ENV=%PROJECT_DIR%\venv"
set "VIRTUAL_ENV_PROMPT=^(SmartAssistant^) "

REM Update command prompt
if not defined PROMPT set PROMPT=$P$G
if defined _OLD_VIRTUAL_PROMPT set PROMPT=%_OLD_VIRTUAL_PROMPT%
set "_OLD_VIRTUAL_PROMPT=%PROMPT%"
set "PROMPT=^(SmartAssistant^) %PROMPT%"

echo SmartAssistant Environment Activated
echo Project Directory: %PROJECT_DIR%
echo Python: %PROJECT_DIR%\venv\Scripts\python.exe
echo.

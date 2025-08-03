@echo off
rem This script is designed to be portable and run gemini_cli from its current directory.

rem Get the drive letter and navigate to the script's directory
ECHO Setting current directory...
cd /d "%~dp0"

ECHO Launching gemini...
gemini

ECHO Script finished. Press any key to continue...
pause
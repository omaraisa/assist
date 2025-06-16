@echo off
title SmartAssistant - ArcGIS Pro Connector

echo =========================================
echo   SmartAssistant - ArcGIS Pro Connector  
echo =========================================
echo.

REM Get project directory
set "PROJECT_DIR=%~dp0"  
set "PROJECT_DIR=%PROJECT_DIR:~0,-1%"

echo [INFO] To connect ArcGIS Pro to SmartAssistant:
echo [INFO] Copy and paste this command in ArcGIS Pro Python console:
echo.
echo exec(open(r"%PROJECT_DIR%\arcgis_connector.py").read())
echo.
echo [INFO] Make sure the SmartAssistant server is running first!
echo [INFO] Start server with: start_server.bat
echo.
pause
python -c "import arcpy; print('ArcGIS Pro environment detected')" 2>nul
if not errorlevel 1 (
    echo [INFO] Running connector...
    python "%PROJECT_DIR%\arcgis_connector.py"
) else (
    echo [WARNING] Not in ArcGIS Pro environment
    echo [INFO] Please run from ArcGIS Pro Python console or as a script tool
)

pause

@echo off
echo ================================================================
echo          ArcGIS Pro Smart Assistant - Cache Cleaner
echo ================================================================
echo.
echo This script will clear all Python caches to ensure fresh code execution
echo.

REM Stop any running Python processes (optional - uncomment if needed)
REM echo Stopping Python processes...
REM taskkill /f /im python.exe 2>nul
REM taskkill /f /im pythonw.exe 2>nul

echo Clearing Python cache files...
echo.

REM Clear main app cache
if exist "app\__pycache__" (
    echo [1/4] Clearing app\__pycache__...
    rmdir /s /q "app\__pycache__"
    echo    ✓ Cleared app\__pycache__
) else (
    echo [1/4] app\__pycache__ - No cache found
)

REM Clear ai subdirectory cache
if exist "app\ai\__pycache__" (
    echo [2/4] Clearing app\ai\__pycache__...
    rmdir /s /q "app\ai\__pycache__"
    echo    ✓ Cleared app\ai\__pycache__
) else (
    echo [2/4] app\ai\__pycache__ - No cache found
)

REM Clear any other __pycache__ directories recursively
echo [3/4] Searching for other cache directories...
for /r %%d in (__pycache__) do (
    if exist "%%d" (
        echo    Found: %%d
        rmdir /s /q "%%d" 2>nul
        echo    ✓ Cleared: %%d
    )
)

REM Clear individual .pyc files that might exist outside __pycache__
echo [4/4] Removing standalone .pyc files...
for /r %%f in (*.pyc) do (
    if exist "%%f" (
        echo    Found: %%f
        del "%%f" 2>nul
        echo    ✓ Deleted: %%f
    )
)

echo.
echo ================================================================
echo                        CACHE CLEARED!
echo ================================================================
echo.
echo Next steps:
echo 1. Restart ArcGIS Pro completely (close all instances)
echo 2. Run Progent again
echo.
echo Note: The module reload code in arcgis_connector.py should
echo       handle future cache issues automatically.
echo.
pause

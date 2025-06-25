@echo off
setlocal enabledelayedexpansion

:menu
cls
echo ================================================================
echo           ArcGIS Pro Smart Assistant - Dev Tools
echo ================================================================
echo.
echo Choose an option:
echo.
echo [1] Clear Python Cache (Quick)
echo [2] Clear Cache + Check Git Status
echo [3] Full Reset (Cache + Restart Recommendation)
echo [4] Check Current Cache Status
echo [5] Help / Troubleshooting
echo [0] Exit
echo.
set /p choice="Enter your choice (0-5): "

if "%choice%"=="1" goto clear_cache
if "%choice%"=="2" goto clear_and_git
if "%choice%"=="3" goto full_reset
if "%choice%"=="4" goto check_status
if "%choice%"=="5" goto help
if "%choice%"=="0" goto exit
goto menu

:clear_cache
echo.
echo [CLEARING CACHE...]
call clear_python_cache.bat
echo.
echo Cache cleared! You can now test your changes.
pause
goto menu

:clear_and_git
echo.
echo [CLEARING CACHE + GIT STATUS...]
call clear_python_cache.bat
echo.
echo [GIT STATUS]
git status
echo.
echo Recommended: If you see modified files, commit them before testing.
pause
goto menu

:full_reset
echo.
echo [FULL RESET MODE]
echo.
echo Step 1: Clearing Python cache...
call clear_python_cache.bat
echo.
echo Step 2: Checking for running Python processes...
tasklist | findstr python
echo.
echo ================================================================
echo                    MANUAL STEPS REQUIRED
echo ================================================================
echo.
echo 1. Close ALL ArcGIS Pro windows completely
echo 2. Wait 5 seconds
echo 3. Restart ArcGIS Pro
echo 4. Run Smart Assistant
echo.
echo This ensures a completely clean state.
echo.
pause
goto menu

:check_status
echo.
echo [CHECKING CACHE STATUS...]
echo.
set cache_found=0

if exist "app\__pycache__" (
    echo ✓ Found: app\__pycache__
    dir /b "app\__pycache__" | find /c ".pyc" > temp_count.txt
    set /p count=<temp_count.txt
    echo   - Contains !count! .pyc files
    del temp_count.txt
    set cache_found=1
)

if exist "app\ai\__pycache__" (
    echo ✓ Found: app\ai\__pycache__
    dir /b "app\ai\__pycache__" | find /c ".pyc" > temp_count.txt
    set /p count=<temp_count.txt
    echo   - Contains !count! .pyc files
    del temp_count.txt
    set cache_found=1
)

if "%cache_found%"=="0" (
    echo ✓ No cache directories found - Clean state!
) else (
    echo.
    echo ⚠ Cache files detected. Consider clearing them if you've made code changes.
)

echo.
pause
goto menu

:help
echo.
echo ================================================================
echo                     TROUBLESHOOTING GUIDE
echo ================================================================
echo.
echo PROBLEM: Code changes not taking effect
echo SOLUTION: Use option [1] Clear Python Cache
echo.
echo PROBLEM: Function not found errors  
echo SOLUTION: Use option [3] Full Reset
echo.
echo PROBLEM: After git pull, old behavior persists
echo SOLUTION: Use option [2] Clear Cache + Check Git Status
echo.
echo PROBLEM: Strange errors or crashes
echo SOLUTION: Use option [3] Full Reset + restart ArcGIS Pro
echo.
echo PROBLEM: Module import errors
echo SOLUTION: Check that ArcGIS Pro is closed, then option [3]
echo.
echo ================================================================
echo                        PREVENTION TIPS
echo ================================================================
echo.
echo 1. After any code modification, run option [1]
echo 2. After git pull, always run option [2]
echo 3. If you're unsure, option [3] is safest
echo 4. Keep this tool handy in your taskbar/desktop
echo.
pause
goto menu

:exit
echo.
echo Thanks for using ArcGIS Pro Smart Assistant Dev Tools!
echo.
exit /b 0

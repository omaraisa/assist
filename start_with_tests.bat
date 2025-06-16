@echo off
echo ======================================================
echo ArcGIS Pro Smart Assistant - Quick Test and Start
echo ======================================================

cd /d "f:\MEGA\Shared\ProAI\SmartAssistant\BaseAssistant\SmartAssistantFastAPI"

echo.
echo 🔍 Testing indentation fixes and conversation history...
echo.
python quick_test.py

echo.
echo Checking exit code: %errorlevel%

if %errorlevel% equ 0 (
    echo.
    echo ✅ All tests passed! Starting the server...
    echo.
    echo 🚀 Starting FastAPI server on http://localhost:8000
    echo 📖 Open your browser to http://localhost:8000 to access the assistant
    echo 🛑 Press Ctrl+C to stop the server
    echo.
    timeout /t 3 /nobreak
    echo Starting server now...
    python run.py
) else (
    echo.
    echo ❌ Tests failed. Please check the errors and fix them before starting the server.
    echo.
    echo 🔧 Common issues:
    echo   - Python dependencies not installed: pip install -r requirements.txt
    echo   - Indentation errors in Python files
    echo   - Missing configuration files
    echo.
    echo Press any key to exit...
    pause >nul
)

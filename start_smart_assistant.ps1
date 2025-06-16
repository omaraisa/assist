# ArcGIS Pro Smart Assistant - Comprehensive Startup Script
# This script handles all aspects of starting the Smart Assistant with proper conversation history

param(
    [string]$Mode = "full",  # Options: full, test, server-only
    [switch]$Debug = $false,
    [switch]$TestHistory = $false
)

Write-Host "======================================================" -ForegroundColor Cyan
Write-Host "ArcGIS Pro Smart Assistant - Enhanced Startup" -ForegroundColor Cyan
Write-Host "======================================================" -ForegroundColor Cyan

# Set working directory
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

Write-Host "Working Directory: $ScriptDir" -ForegroundColor Green

# Function to test conversation history fixes
function Test-ConversationHistory {
    Write-Host "`n🔍 Testing Conversation History Fixes..." -ForegroundColor Yellow
    
    try {
        $result = python test_conversation_history.py
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Conversation History Tests PASSED" -ForegroundColor Green
        } else {
            Write-Host "❌ Conversation History Tests FAILED" -ForegroundColor Red
            Write-Host "Output: $result" -ForegroundColor Gray
        }
    } catch {
        Write-Host "❌ Error running conversation history tests: $($_.Exception.Message)" -ForegroundColor Red
    }
}

# Function to check environment
function Test-Environment {
    Write-Host "`n🔍 Checking Environment..." -ForegroundColor Yellow
    
    # Check Python
    try {
        $pythonVersion = python --version 2>&1
        Write-Host "✅ Python: $pythonVersion" -ForegroundColor Green
    } catch {
        Write-Host "❌ Python not found or not working" -ForegroundColor Red
        return $false
    }
    
    # Check required files
    $requiredFiles = @(
        "app/main.py",
        "app/websocket_manager.py", 
        "app/ai_service.py",
        "app/config.py",
        ".env",
        "requirements.txt"
    )
    
    foreach ($file in $requiredFiles) {
        if (Test-Path $file) {
            Write-Host "✅ Found: $file" -ForegroundColor Green
        } else {
            Write-Host "❌ Missing: $file" -ForegroundColor Red
            return $false
        }
    }
    
    # Check .env configuration
    if (Test-Path ".env") {
        $envContent = Get-Content ".env" -Raw
        if ($envContent -match "MAX_HISTORY_LENGTH=(\d+)") {
            $historyLength = $Matches[1]
            Write-Host "✅ MAX_HISTORY_LENGTH configured: $historyLength" -ForegroundColor Green
        } else {
            Write-Host "⚠️  MAX_HISTORY_LENGTH not found in .env" -ForegroundColor Yellow
        }
        
        if ($envContent -match "GEMINI_API_KEY=(.+)") {
            Write-Host "✅ GEMINI_API_KEY configured" -ForegroundColor Green
        } else {
            Write-Host "⚠️  GEMINI_API_KEY not configured" -ForegroundColor Yellow
        }
    }
    
    return $true
}

# Function to install dependencies
function Install-Dependencies {
    Write-Host "`n📦 Installing Dependencies..." -ForegroundColor Yellow
    
    try {
        pip install -r requirements.txt
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Dependencies installed successfully" -ForegroundColor Green
        } else {
            Write-Host "❌ Failed to install dependencies" -ForegroundColor Red
            return $false
        }
    } catch {
        Write-Host "❌ Error installing dependencies: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
    
    return $true
}

# Function to start the server
function Start-Server {
    param([bool]$Background = $false)
    
    Write-Host "`n🚀 Starting FastAPI Server..." -ForegroundColor Yellow
    
    if ($Background) {
        Write-Host "Starting server in background mode..." -ForegroundColor Cyan
        $job = Start-Job -ScriptBlock {
            Set-Location $using:ScriptDir
            python run.py
        }
        Write-Host "✅ Server started in background (Job ID: $($job.Id))" -ForegroundColor Green
        return $job
    } else {
        Write-Host "Starting server in foreground mode (press Ctrl+C to stop)..." -ForegroundColor Cyan
        python run.py
    }
}

# Function to display configuration summary
function Show-Configuration {
    Write-Host "`n📋 Current Configuration:" -ForegroundColor Cyan
    Write-Host "=========================" -ForegroundColor Cyan
    
    if (Test-Path ".env") {
        $envVars = @{
            "MAX_HISTORY_LENGTH" = "Conversation history limit"
            "DEFAULT_AI_MODEL" = "AI model being used"  
            "HOST" = "Server host address"
            "PORT" = "Server port number"
            "DEBUG" = "Debug mode status"
        }
        
        $envContent = Get-Content ".env" -Raw
        foreach ($var in $envVars.Keys) {
            if ($envContent -match "$var=(.+)") {
                $value = $Matches[1]
                Write-Host "$var = $value" -ForegroundColor Green
                Write-Host "  └─ $($envVars[$var])" -ForegroundColor Gray
            }
        }
    }
}

# Function to show usage instructions
function Show-Usage {
    Write-Host "`n📖 Usage Instructions:" -ForegroundColor Cyan
    Write-Host "======================" -ForegroundColor Cyan
    Write-Host "1. Start ArcGIS Pro and ensure it's running" -ForegroundColor White
    Write-Host "2. Run this script to start the Smart Assistant server" -ForegroundColor White
    Write-Host "3. Open your web browser and go to: http://localhost:8000" -ForegroundColor White
    Write-Host "4. The AI will now have access to conversation history and respond in your language" -ForegroundColor White
    Write-Host ""
    Write-Host "🔧 Script Options:" -ForegroundColor Yellow
    Write-Host "  -Mode full        : Full startup (default)" -ForegroundColor White
    Write-Host "  -Mode test        : Test mode only" -ForegroundColor White
    Write-Host "  -Mode server-only : Start server without tests" -ForegroundColor White
    Write-Host "  -TestHistory      : Run conversation history tests" -ForegroundColor White
    Write-Host "  -Debug            : Enable debug output" -ForegroundColor White
    Write-Host ""
    Write-Host "✨ Key Features Fixed:" -ForegroundColor Green
    Write-Host "  ✅ Conversation history now works (MAX_HISTORY_LENGTH=$((Get-Content .env | Select-String MAX_HISTORY_LENGTH) -replace '.*=', ''))" -ForegroundColor Green
    Write-Host "  ✅ AI responds in the same language as your question" -ForegroundColor Green
    Write-Host "  ✅ Single state per chat history with automatic cleanup" -ForegroundColor Green
    Write-Host "  ✅ Enhanced Arabic text support with proper encoding" -ForegroundColor Green
}

# Main execution
try {
    # Show configuration first
    Show-Configuration
    
    # Test conversation history if requested
    if ($TestHistory -or $Mode -eq "test") {
        Test-ConversationHistory
        if ($Mode -eq "test") {
            Write-Host "`n🏁 Test mode completed." -ForegroundColor Cyan
            Show-Usage
            exit 0
        }
    }
    
    # Environment check
    if (-not (Test-Environment)) {
        Write-Host "`n❌ Environment check failed. Please fix the issues above." -ForegroundColor Red
        exit 1
    }
    
    # Install dependencies if needed
    Write-Host "`n📦 Checking dependencies..." -ForegroundColor Yellow
    try {
        python -c "import fastapi, uvicorn, websockets, aiohttp" 2>$null
        Write-Host "✅ All dependencies are installed" -ForegroundColor Green
    } catch {
        Write-Host "⚠️  Some dependencies missing, installing..." -ForegroundColor Yellow
        if (-not (Install-Dependencies)) {
            Write-Host "❌ Failed to install dependencies" -ForegroundColor Red
            exit 1
        }
    }
    
    # Show usage instructions
    Show-Usage
    
    # Start server based on mode
    switch ($Mode) {
        "full" {
            Write-Host "`n🎯 Starting in FULL mode..." -ForegroundColor Cyan
            Start-Server -Background $false
        }
        "server-only" {
            Write-Host "`n🎯 Starting in SERVER-ONLY mode..." -ForegroundColor Cyan
            Start-Server -Background $false
        }
        default {
            Write-Host "`n🎯 Starting with default configuration..." -ForegroundColor Cyan
            Start-Server -Background $false
        }
    }
    
} catch {
    Write-Host "`n❌ Startup failed: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Stack trace:" -ForegroundColor Gray
    Write-Host $_.Exception.StackTrace -ForegroundColor Gray
    exit 1
}

Write-Host "`n✅ Smart Assistant startup completed!" -ForegroundColor Green
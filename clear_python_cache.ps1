# ArcGIS Pro Smart Assistant - Cache Cleaner (PowerShell)
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host "          ArcGIS Pro Smart Assistant - Cache Cleaner" -ForegroundColor Cyan  
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "This script will clear all Python caches to ensure fresh code execution" -ForegroundColor Yellow
Write-Host ""

# Function to remove directory safely
function Remove-DirectorySafe {
    param([string]$Path)
    if (Test-Path $Path) {
        try {
            Remove-Item $Path -Recurse -Force -ErrorAction Stop
            Write-Host "    ✓ Cleared: $Path" -ForegroundColor Green
            return $true
        } catch {
            Write-Host "    ⚠ Failed to clear: $Path - $($_.Exception.Message)" -ForegroundColor Yellow
            return $false
        }
    } else {
        Write-Host "    - No cache found: $Path" -ForegroundColor Gray
        return $true
    }
}

# Stop Python processes (optional)
# Write-Host "Stopping Python processes..." -ForegroundColor Yellow
# Get-Process -Name "python*" -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue

Write-Host "Clearing Python cache files..." -ForegroundColor Yellow
Write-Host ""

# Clear specific cache directories
$cacheCleared = 0
$cacheDirs = @(
    "app\__pycache__",
    "app\ai\__pycache__"
)

for ($i = 0; $i -lt $cacheDirs.Length; $i++) {
    $dir = $cacheDirs[$i]
    Write-Host "[$($i+1)/$($cacheDirs.Length)] Checking $dir..." -ForegroundColor Cyan
    if (Remove-DirectorySafe $dir) { $cacheCleared++ }
}

# Find and clear all other __pycache__ directories recursively
Write-Host "[$($cacheDirs.Length+1)/$($cacheDirs.Length+2)] Searching for other cache directories..." -ForegroundColor Cyan
$otherCaches = Get-ChildItem -Path . -Name "__pycache__" -Recurse -Directory -ErrorAction SilentlyContinue
foreach ($cache in $otherCaches) {
    if (Remove-DirectorySafe $cache) { $cacheCleared++ }
}

# Clear individual .pyc files
Write-Host "[$($cacheDirs.Length+2)/$($cacheDirs.Length+2)] Removing standalone .pyc files..." -ForegroundColor Cyan
$pycFiles = Get-ChildItem -Path . -Name "*.pyc" -Recurse -File -ErrorAction SilentlyContinue
foreach ($file in $pycFiles) {
    try {
        Remove-Item $file -Force -ErrorAction Stop
        Write-Host "    ✓ Deleted: $file" -ForegroundColor Green
        $cacheCleared++
    } catch {
        Write-Host "    ⚠ Failed to delete: $file" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host "                        CACHE CLEARED!" -ForegroundColor Green
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Summary:" -ForegroundColor Yellow
Write-Host "  - Cleared/processed $cacheCleared cache items" -ForegroundColor White
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. Restart ArcGIS Pro completely (close all instances)" -ForegroundColor White
Write-Host "  2. Run your Smart Assistant again" -ForegroundColor White
Write-Host ""
Write-Host "Note: The module reload code in arcgis_connector.py should" -ForegroundColor Gray
Write-Host "      handle future cache issues automatically." -ForegroundColor Gray
Write-Host ""
Read-Host "Press Enter to continue"

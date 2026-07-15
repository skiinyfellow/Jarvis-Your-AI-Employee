# Jarvis Installation Script for Windows
# Run with: powershell -ExecutionPolicy Bypass -File install_windows.ps1

Write-Host "========================================" -ForegroundColor Green
Write-Host "Jarvis: Your AI Employee - Windows Setup" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green

# TODO: Check for Docker
Write-Host "`nChecking prerequisites..." -ForegroundColor Yellow

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "Docker not found. Please install Docker Desktop for Windows." -ForegroundColor Red
    exit 1
}
Write-Host "✓ Docker found" -ForegroundColor Green

# TODO: Check for Python
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python not found. Please install Python 3.10+" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Python found" -ForegroundColor Green

# TODO: Create .env file
Write-Host "`nSetting up configuration..." -ForegroundColor Yellow
if (-not (Test-Path ".env")) {
    Copy-Item ".env.example" ".env"
    Write-Host "✓ Created .env file" -ForegroundColor Green
} else {
    Write-Host "✓ .env file already exists" -ForegroundColor Green
}

# TODO: Install dependencies
Write-Host "`nInstalling Python dependencies..." -ForegroundColor Yellow
python -m pip install -r requirements.txt

# TODO: Start containers
Write-Host "`nStarting Docker containers..." -ForegroundColor Yellow
docker-compose up -d

Write-Host "`n========================================" -ForegroundColor Green
Write-Host "Installation Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Edit .env with your configuration" -ForegroundColor Cyan
Write-Host "2. Run: docker-compose up" -ForegroundColor Cyan
Write-Host "3. Visit: http://localhost:8000" -ForegroundColor Cyan

# Quick Email Setup Script
# This will guide you through setting up email notifications

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  EMAIL SETUP FOR PORTFOLIO WEBSITE" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "This script will help you set up email notifications." -ForegroundColor White
Write-Host "You'll receive an email whenever someone submits the contact form.`n" -ForegroundColor White

Write-Host "STEP 1: Get Gmail App Password" -ForegroundColor Yellow
Write-Host "----------------------------------------" -ForegroundColor Yellow
Write-Host "1. Open: https://myaccount.google.com/apppasswords" -ForegroundColor White
Write-Host "2. If prompted, enable 2-Step Verification first" -ForegroundColor White
Write-Host "3. Select 'Mail' and 'Other (Custom name)'" -ForegroundColor White
Write-Host "4. Enter: 'Portfolio Website'" -ForegroundColor White
Write-Host "5. Click 'Generate'" -ForegroundColor White
Write-Host "6. Copy the 16-character password (remove spaces)`n" -ForegroundColor White

$appPassword = Read-Host "Paste your Gmail App Password here (or press Enter to skip)"

if ($appPassword) {
    # Remove spaces from app password
    $appPassword = $appPassword -replace '\s', ''
    
    # Create .env file
    $envPath = "c:\Users\0174988\Documents\usefulstuff\MyResume\portfolio_website\.env"
    Set-Content -Path $envPath -Value "EMAIL_HOST_PASSWORD=$appPassword"
    
    Write-Host "`n✅ .env file created successfully!" -ForegroundColor Green
    Write-Host "Location: $envPath`n" -ForegroundColor Gray
    
    Write-Host "STEP 2: Test Email Configuration" -ForegroundColor Yellow
    Write-Host "----------------------------------------" -ForegroundColor Yellow
    $test = Read-Host "Would you like to send a test email now? (y/n)"
    
    if ($test -eq 'y' -or $test -eq 'Y') {
        Write-Host "`nSending test email..." -ForegroundColor White
        Set-Location "c:\Users\0174988\Documents\usefulstuff\MyResume\portfolio_website"
        C:/Users/0174988/Documents/usefulstuff/MyResume/.venv/Scripts/python.exe test_email.py
    } else {
        Write-Host "`nYou can test email later by running:" -ForegroundColor White
        Write-Host "  python test_email.py`n" -ForegroundColor Gray
    }
    
} else {
    Write-Host "`n⚠️  Setup skipped. Create .env file manually:" -ForegroundColor Yellow
    Write-Host "1. Create file: c:\Users\0174988\Documents\usefulstuff\MyResume\portfolio_website\.env" -ForegroundColor White
    Write-Host "2. Add line: EMAIL_HOST_PASSWORD=your_app_password_here`n" -ForegroundColor White
}

Write-Host "`nFor detailed instructions, see:" -ForegroundColor Cyan
Write-Host "  EMAIL_SETUP.md`n" -ForegroundColor Gray

Write-Host "========================================`n" -ForegroundColor Cyan

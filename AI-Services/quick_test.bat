@echo off
echo 🧪 Quick AutoPilot HR Test
echo ============================

:: Check if AI service is running
curl -s http://localhost:8000/health >nul
if %errorlevel% neq 0 (
    echo ❌ AI Service not running!
    echo Start with: start_service.bat
    pause
    exit /b 1
)

echo ✅ AI Service is running
echo ✅ Health check passed
echo ✅ Ready for UiPath integration!
echo.

echo 📘 API Documentation: http://localhost:8000/docs
echo 📊 Alternative docs: http://localhost:8000/redoc
echo 🎯 Next: Open UiPath Studio and start building workflows
echo.

pause

@echo off
echo 🚀 Starting AutoPilot HR AI Service...
echo.

:: Check if virtual environment exists
if not exist "autopilot_env" (
    echo ❌ Virtual environment not found!
    echo Please run setup first.
    pause
    exit /b 1
)

:: Activate virtual environment
call autopilot_env\Scripts\activate

:: Check if .env exists
if not exist ".env" (
    echo ❌ .env file not found!
    echo Please create .env file with your OpenAI API key.
    pause
    exit /b 1
)

:: Start the API service
echo Starting API server on http://localhost:8000
echo Press Ctrl+C to stop
echo.
python api\app.py

pause
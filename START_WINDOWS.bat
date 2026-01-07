@echo off
echo ========================================
echo Stock Tracker Web App
echo ========================================
echo.
echo Installing requirements...
pip install flask requests beautifulsoup4 lxml
echo.
echo ========================================
echo Starting web server...
echo ========================================
echo.
echo Your website will be available at:
echo http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.
python web_app.py
pause

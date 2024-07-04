@echo off

REM Check if Python is installed
python --version
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python first.
    exit /b 1
)

REM Go to the src directory
cd src

REM Check if virtual environment exists
IF EXIST venv (
    echo Activating venv
    call venv\Scripts\activate
) ELSE (
    echo Making venv
    python -m venv venv
    call venv\Scripts\activate
)

REM Install dependencies
pip install -r requirements.txt

REM Run the app
python main.py

REM Deactivate venv
deactivate

pause   

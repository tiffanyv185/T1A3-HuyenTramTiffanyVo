@echo off

REM Navigate to the 'src' directory
cd src

REM Check if the virtual environment 'venv' exists
if exist venv (
    echo Activating existing virtual environment.
    call venv\Scripts\activate
) else (
    echo Creating virtual environment.
    python -m venv venv
    call venv\Scripts\activate
)

REM Install dependencies from requirements.txt
if exist requirements.txt (
    pip install -r requirements.txt
) else (
    echo requirements.txt not found. Exiting.
    exit /b 1
)

REM Run the main.py script
if exist main.py (
    python main.py
) else (
    echo main.py not found. Exiting.
    exit /b 1
)

REM Deactivate the virtual environment
deactivate

echo Script completed.
pause

#!/bin/bash

# Function to check if Python is installed
check_python() {
    if command -v python3 &>/dev/null; then
        echo "Python is installed."
    else
        echo "Python is not installed. Installing Python..."
        
        # For macOS, use Homebrew to install Python
        if command -v brew &>/dev/null; then
            brew install python
        else
            echo "Homebrew is not installed. Please install Homebrew first."
            exit 1
        fi
    fi
}

# Navigate to the 'src' directory
cd src

# Check if the virtual environment 'venv' exists
if [ -d "venv" ]; then
    # If 'venv' exists, activate it
    echo "Activating existing virtual environment."
else
    # If 'venv' does not exist, create it
    echo "Creating virtual environment."
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Run the main.py script
python3 main.py

# Deactivate the virtual environment
deactivate

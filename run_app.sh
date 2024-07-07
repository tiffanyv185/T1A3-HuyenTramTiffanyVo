#!/bin/bash

# Navigate to the 'src' directory
cd src

# Check if the virtual environment 'venv' exists
if [ -d "venv" ]; then
    echo "Activating existing virtual environment."
    source venv/bin/activate
else
    echo "Creating virtual environment."
    python3 -m venv venv
    source venv/bin/activate
fi

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Run the main.py script
python3 main.py

# Deactivate the virtual environment
deactivate

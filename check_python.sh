#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed. Installing Python 3..."
    # Install Python 3 (this example uses Homebrew for macOS)
    if command -v brew &> /dev/null
    then
        brew install python
    else
        echo "Homebrew is not installed. Please install Homebrew first."
        exit 1
    fi
else
    echo "Python 3 is already installed."
fi


./run_app.sh

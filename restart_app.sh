#!/bin/bash

# Change to the 'src' directory
cd src

# Delete the file 'user_data.json' if it exists
    rm user_data.json
    echo "Data is has been deleted. App has now been reset."

# Navigate back out of directory.
cd ./..

#Run the application 
./check_python.sh

# T1A3 Terminal Application
## Huyen Tram Tiffany Vo
```

 __ __                       ___            _             ___           
|  \  \ ___ ._ _  ___  _ _  / __> ___  _ _ <_>._ _  ___  | . | ___  ___ 
|     |/ . \| ' |/ ._>| | | \__ \<_> || | || || ' |/ . | |   || . \| . \
|_|_|_|\___/|_|_|\___.`_. | <___/<___||__/ |_||_|_|\_. | |_|_||  _/|  _/
                      <___'                        <___'      |_|  |_|  

```
💸₊˚⊹💲 ♡ Welcome to the Money Saving App! This app is designed to help you effectively manage and track your saving goals. Please [click here](#help-documentation) to get started 💸₊˚⊹💲 ♡

# Table of Contents
* [Help Documentation](#help-documentation)
    * [Installation Instructions](#installation-instructions)
    * [Dependencies](#dependencies)
    * [User Guide](#user-guide)

* [Information](#information)
    * [Github Repository](#github-repository)
    * [Introduction](#introduction)
    * [Overview of Features](#overview-of-features)
    * [Implentation Plan](#implementation-plan)
    * [Code Style Guide](#code-style-guide)

    ---

# Help Documentation

## System/Hardware Requirements:
* <b>Operating System:</b> Windows, MacOS, or Linux
* <b>Python Version: </b> Python 3.6 or higher
* <b>Hardware:</b> Any modern computer

## Installation Instructions
1. Clone the Repository:
    * Open the terminal.
    * Run the following command to clone the repository:

    ``` git clone git@github.com:tiffanyv185/T1A3-HuyenTramTiffanyVo.git ```

2. Navigate to cloned directory:
    
    ``` cd T1A3-HuyenTramTiffanyVo ```

3. Run the script in terminal:
   
   ``` ./run.sh ```
----
<b>OR, FOR A STEP BY STEP GUIDE:</b>


1. Download Python:
    * Go to the [Python Downloads Page](https://www.python.org/downloads/).
    * Choose the latest version and download the installer.

2. Install Python:
    * Run the downloaded installer.
    * Check the box "Add Python to PATH" and then click "Install Now".
    * Follow installation instructions.

3. Verify Installation: 
    * Open a terminal
    * Type ```python --version``` and press Enter. You should see the installed Python version.

4. Clone the Repository:
    * Open the terminal.
    * Run the following command to clone the repository:

    ``` git clone git@github.com:tiffanyv185/T1A3-HuyenTramTiffanyVo.git ```

    * Navigate to cloned directory:

    ```cd T1A3-HuyenTramTiffanyVo```

    ```cd src```

5. Set up Virtual Environment
    * create a vitrual environment:

    ``` python3 -m venv venv ```

    * Activate virtual environment:

    ``` source venv/bin/activate ``` 

6. Install Dependencies:
    * Install the required dependencies using `pip`:

    ``` pip install -r requirements.txt ```

7. Run the Application:
    * In your terminal, type:

    ``` python3 main.py```

## Dependencies
The application requires the following Python packages:
* ```datetime```: For handling dates.
* ``` json```: library modile for JSON encoding and decoding.
* ```prettytable```: library for displaying tabular data in a readable format.
* ```os```: library module for interacting with the operating system
* ```colorama```: library that allows text to displayed in different styles and colours.


# Information

## Github Repository: 
https://github.com/tiffanyv185/T1A3-HuyenTramTiffanyVo

## Introduction
This terminal based application is designed to help users manage their financial goals effectively. Whether they are saving for a holiday, car, house, or any other personal goals, this application will provide a structured way to track their progress, make contributions and stay informed about their milestones and dealines.

## Overview of Features
* <b>Goal Management:</b> Users will be able to easily add, edit, and delete their financial goals. Each goal includes name, target amount, and deadline.

* <b>Contributions:</b> Users will be able to make contributions towards their goals an dtrack how much they have saved over time.
* <b>Progress Tracking:</b> Users can view their progress of each goal and their overall savings at a glance.
* <b>History of Contributions:</b> Users can view a detailed history of their contributions made, allowing them to see how much they've contributed to each goal.
* <b>Monthly Reports:</b> Users can get generated monthly reports to review their savings and contributions for any given month.

## Implementation Plan
1. <b> Identify and understand the requirements:</b>

    The application needs to:
    - Help users manage their saving goals.
    - Allow users to add, edit, and delete saving goals.
    - Enable users to contribute to their saving goals.
    - Track their progress of each goal.
    - Provide a history of contributions.
    - Generate monthly reports of contributions.

2. <b>Designing the Application Structure:</b>

    The application is divided into several modules to seperate concerns and improve maintainability:
    - ```data_manager.py```: Manages loading and saving data.
    - ```goal_manager.py```: Handles adding, editing, deleting and listing goals.
    -```contribution_manager.py```: Manages contributions and viewing contribution history.
    - ```report_manager.py```: Handles monthly contributuions report.
    - ```main.py```: The main entry point of the application, providing the user interface and menu.



## Code Style Guide
This code follows the PEP 8 style guide. the official guide for Python code. PEP 8 provides readable and cosistent conventions for code. 
The following is a summary of PEP 8 Style guide:
* Indentation: Uses 4 spaces per indentation.
* Blank Lines: Surround top-level function and class definitions with two lines. Method definitions are surrounded by a single blanke line.
* Imports: Imports are placed together at the top of the the file.
* Whitespace: Use of whitespace to seperate elements in code, such as operators, commas and semicolons.
* Comments: Inline comments used with space after the ```#``` symbol.
* Naming Conventions: Use descriptive names for variables, functions and classes. functions and variables should be lowercase, with words seperated by underscores ```(snake_case)```

More information can be found [here](https://peps.python.org/pep-0008/).
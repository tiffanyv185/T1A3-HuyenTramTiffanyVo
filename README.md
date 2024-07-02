# T1A3 Terminal Application
## Huyen Tram Tiffany Vo
```

  __  __                     ___           _              ___           _    
 |  \/  |___ _ _  ___ _  _  / __| __ ___ _(_)_ _  __ _   / __|___  __ _| |___
 | |\/| / _ \ ' \/ -_) || | \__ \/ _` \ V / | ' \/ _` | | (_ / _ \/ _` | (_-<
 |_|  |_\___/_||_\___|\_, | |___/\__,_|\_/|_|_||_\__, |  \___\___/\__,_|_/__/
                      |__/                       |___/                       

```
# Help Documentation

## Installation Instructions
1. Clone the Repository:
    * Open the terminal.
    * Run the following command to clone the repository:

    ``` git clone git@github.com:tiffanyv185/T1A3-HuyenTramTiffanyVo.git ```

    * Navigate to cloned directory:

    ``` cd T1A3-HuyenTramTiffanyVo ```

2. Set up Virtual Environment
    * create a vitrual environment:

    ``` python3 -m venv env ```

    * Activate virtual environment:

    ``` source env/bin/activate ``` 

3. Install Dependencies:
    * Install the required dependencies using `pip`:

    ``` pip install -r requirements.txt ```

## Dependencies
The application requires the following Python packages:
* ```datetime```: For handling dates.
* ``` json```: library modile for JSON encoding and decoding.
* ```prettytable```: library for displaying tabular data in a readable format.
* ```os```: library module for interacting with the operating system






















## Github Repository: 
https://github.com/tiffanyv185/T1A3-HuyenTramTiffanyVo

## Introduction
This terminal based application is designed to help users manage their financial goals effectively. Whether they are saving for a holiday, car, house, or any other personal goals, this application will provide a structured way to track their progress, make contributions and stay informed about their milestones and dealines.

## Overview of Features
* <b>Goal Management:</b> Users will be able to easily add, edit, and delete their financial goals. Each goal includes name, target amount, and deadline.

* <b>Contributions:</b> Users will be able to make contributions towards their goals an dtrack how much they have saved over time.
* <b>Progress Tracking:</b> Users can view their progress of each goal and their overall savings at a glance.
* <b>History of Contributions:</b> Users can view a detailed history of their contributions made, allowing them to see how much they've contributed to each goal.
* <b>Receive Notifications:</b> Users will be able to receive notifications when a goal is achieved and alerts for upcoming deadlines, ensurin gthat they stay on track.
* <b>Monthly Reports:</b> Users can get generated monthly reports to review their savings and contributions for any given month.

## Implementation Plan
1. <b> Understanding the requirements</b>
The application needs to:
    - Allow users to add, edit, and delete saving goals.
    - Enable users to contribute to their saving goals.
    - Track their progress of each goal.
    - Provide a history of contributions.
    - Notify the users of milesotones and deadlines.
    - Generate monthly reports of contributions.

2. <b>Designing the Application Structure:</b>
The application is divided into several modules to seperate concerns and improve maintainability:
    - ```data_manager.py```: Manages loading and saving data.
    - ```goal_manager.py```: Handles adding, editing, deleting and listing goals.
    -```contribution_manager.py```: Manages contributions and viewing contribution history.
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
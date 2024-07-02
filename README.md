# T1A3 Terminal Application
## Huyen Tram Tiffany Vo
```

  __  __                     ___           _              ___           _    
 |  \/  |___ _ _  ___ _  _  / __| __ ___ _(_)_ _  __ _   / __|___  __ _| |___
 | |\/| / _ \ ' \/ -_) || | \__ \/ _` \ V / | ' \/ _` | | (_ / _ \/ _` | (_-<
 |_|  |_\___/_||_\___|\_, | |___/\__,_|\_/|_|_||_\__, |  \___\___/\__,_|_/__/
                      |__/                       |___/                       

```

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

## System/Hardware Requirements:
* <b>Operating System:</b> Windows, MacOS, or Linux
* <b>Python Version: </b> Python 3.6 or higher
* <b>Hardware:</b> Any modern computer

## User Guide:
To use the Money Saving Goal application, follow these steps:

1. Run the Application:
    * In your terminal, navate to the application directory 

        ```cd src```
    * Run the main script:

    ``` python3 main.py```

2. Navigate the Menu:
    * You will see a menu with multiple options. Enter the number corresponding to the action you want to perform:
```
Money Saving Application:
1. Add Goal
2. Edit Goal
3. Delete Goal
4. List Goals
5. Contribute to Goal
6. View Contribution History
7. View Monthly Report
8. Send Notifications
9. Exit

Enter your choice:
```

3. Add Goal:
    *  Choose ```1``` and follow the prompts to enter the goal name, target amount, and deadline.

4. Edit a Goal:
    * Choose ```2```, a list of goals will appear. Enter the index of the goal you want to edit. Follow the prompts to update the goal details.

5. Delete a Goal:
    * Choose ```3```, a list of goals will appear. Enter the index of the goal you want to delete.

6. List Goals:
    * Choose ```4``` to view all your saving goals.

7. Contribute to a Goal:
    * Choose ```5```, a list of goals will appear. Enter the index of the goal you want to contribute to. Enter amount when prompted.

8. View Contribution History:
    * Choose ```6``` to see a detailed history of all contributions made to your goals.

9. View Monthly Report:
    * Choose ```7``` and enter the month (YYYY-MM) to generate a report of contributions for that month.

10. Send Notifications:
    * Choose ```8``` to receive notifications about goals that have been acieved or have upcoming deadlines.

11. Exit the Application:
    * Choose ```9``` to exit.














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
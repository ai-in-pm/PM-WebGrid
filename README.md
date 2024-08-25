# PM-WebGrid
A Python implementation of a Webgrid-inspired Project Management simulation designed to assess and enhance a project manager's decision-making speed, accuracy, and prioritization skills.

Overview
This project implements a simulation tool that creates a grid-based environment representing various project tasks. Project managers can use this tool to practice and improve their task management and decision-making skills in a time-constrained, gamified setting.

Features

Customizable grid sizes (4x4, 8x8, 12x12) to simulate projects of varying complexity
Random task generation with varying priorities and difficulties
Real-time scoring based on task completion and efficiency
Calculation of Project Management Efficiency (PME) and Bits Per Second (BPS) metrics
Interactive command-line interface for task selection
Feedback mechanism to provide insights on performance

Installation

Ensure you have Python 3.6+ installed on your system.

Clone this repository:

    Copygit clone -  https://github.com/your-username/webgrid-project-management.git
    
    cd webgrid-project-management


No additional libraries are required as this project uses Python standard libraries.

Usage

    Run the simulation using the following command:
    
        Copy - python webgrid_pm.py

Follow the prompts to:

    Enter the grid size (4 for small, 8 for medium, 12 for large projects)
    
    Set the simulation duration in seconds
    
    Select tasks by entering row and column numbers when prompted


How It Works

The simulation creates a grid of the specified size and populates it with tasks.
Each task has a unique identifier, priority, and difficulty level.
The user (project manager) selects tasks by entering grid coordinates.
Correct task selections earn points based on the task's priority and difficulty.
Incorrect selections (misclicks) deduct points.
The simulation runs for the specified duration, after which results are calculated and displayed.

Scoring

    -Project Management Efficiency (PME): Calculated as (Net Correct Tasks Completed Per Minute / Grid Size) * 100
    -Bits Per Second (BPS): Calculated as Log2(PME) / Total Time in Seconds

Higher scores in both metrics indicate better performance in task management and decision-making under time constraints.

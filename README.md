# EE202 – Object-Oriented Scientific Calculator

## Project Overview

This project is developed for the EE202 – Object-Oriented Computer Programming course.

The goal is to develop a desktop scientific calculator using Python, Object-Oriented Programming (OOP), and PyQt.

The application will include three main components:

1. **Scientific Calculator:** Performs basic and scientific mathematical operations.
2. **Equation Solver:** Solves two linear equations with two unknowns.
3. **Function Plotter:** Plots mathematical functions using Matplotlib.

## Technologies Used

- Python 3
- PyQt5 (Graphical User Interface)
- Object-Oriented Programming (OOP)
- GitHub (Version Control and Collaboration)

## Object-Oriented Design

The project is organized into six main classes:

| Class | Responsibility |
|---|---|
| CalculatorEngine | Performs basic arithmetic operations |
| TrigonometryEngine | Inherits from BasicCalculator and performs scientific calculations |
| MainWindow | Manages the graphical user interface |
| EquationSolver | Solves two linear equations |
| FunctionPlotter | Generates mathematical graphs |
| InputValidator | Validates user inputs and handles invalid values |

The project uses **inheritance**, where `TrigonometryEngine` inherits from `CalculatorEngine`.

The graphical user interface is separated from the mathematical calculation logic to make the application easier to understand, test, and maintain.

## Project Structure

```text
EE202-Scientific-Calculator/
│
├── README.md
├── main.py
├── requirements.txt
│
├── calculator/
│   ├── basic_calculator.py
│   └── scientific_calculator.py
│
├── gui/
│   └── main_window.py
│
├── modules/
│   ├── equation_solver.py
│   ├── function_plotter.py
│   └── input_validator.py
│
└── docs/
    └── checkpoint1/
        ├── Checkpoint1_Report.pdf
        ├── Initial_UML.png
        └── GUI_Sketches/
```

## Project Checkpoints

- **Checkpoint 1:** Requirements, initial GUI design, and UML class diagram.
- **Checkpoint 2:** Scientific calculator and OOP implementation.
- **Checkpoint 3:** Equation solver, function plotting, and integration.
- **Checkpoint 4:** Final application, testing, documentation, and presentation preparation.
- **Checkpoint 5:** Final presentation and technical evaluation.

## Project Status

The project is currently under development. The initial object-oriented design has been prepared, and the Python modules are being implemented and tested.

## Team Members

Developed by the EE202 project team.

- Member 1: Scientific Calculator
- Member 2: PyQt GUI and MainWindow
- Member 3: Equation Solver and Input Validation
- Member 4: Function Plotting and Testing

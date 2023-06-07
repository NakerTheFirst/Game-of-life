# Game-of-life
The project presents an interactive simulation of Conway's Game of Life, a cellular automaton concept where cells within a grid evolve over time following a set of rules. Developed to furtherly reinforce my understanding of OOP.

# Structure
The game is composed with six classes: Engine, Input, Matrix, UI, ConsoleInterface, and WindowInterface. The Engine serves as the central controller, incorporating the Input, Matrix, and either ConsoleInterface or WindowInterface classes through composition. The Matrix class manages the game logic, determining the state of the cells in the grid. The UI class is a foundational class from which the ConsoleInterface and WindowInterface inherit, demonstrating polymorphism by overriding the UI class methods to provide different means of interaction, either via a console or a graphical user interface. The GUI is implemented using Python's built-in tkinter library. The overall project emphasizes clean, modular design and highlights OOP principles: inheritance, encapsulation, and polymorphism.

## Class diagram
![Class diagram of Conway's Game of Life implementation](https://github.com/NakerTheFirst/Game-of-Life/blob/main/class_diagram.png)

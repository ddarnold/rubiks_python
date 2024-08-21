# Rubik's Cube Solver in python

## Introduction
This project simulates a 3x3 Rubik's Cube and includes tools for manipulation, visualization, and solving the cube. The project is modular, with separate files for different functionalities.

## Installation
Instructions on how to install the project...

## Usage
Basic usage examples...

## Project Structure

- **[cube.py](#cube.py-rubik's-cube-representation)**: Represents the Rubik's Cube and provides methods for manipulation.
- **moves.py**: Contains functions to apply standard Rubik's Cube moves.
- **solver.py**: Implements algorithms to solve the cube.
- **visualization/**: Optional module for visualizing the cube's state.

For a detailed explanation of each component, see below.

## Detailed Component Descriptions

### Cube.py - Rubik's Cube Representation

#### Overview

The `cube.py` file is the core component of this Rubik's Cube project. It defines the `Cube` class, which represents the state of a Rubik's Cube and provides methods for manipulating and interacting with the cube, such as applying rotations and checking whether the cube is solved.

#### Features

- **Cube Initialization**: Initializes the cube in a solved state, where each face is a solid color.
- **Face Rotation**: Methods to rotate any face of the cube clockwise or counterclockwise.
- **State Checking**: Ability to check if the cube is in a solved state.
- **Cube Visualization**: Provides a simple textual representation of the cube for debugging and visualization.

#### Class and Methods

##### Cube Class

The `Cube` class represents a standard 3x3 Rubik's Cube.

###### Attributes

- `faces`: A dictionary representing the six faces of the cube. Each face is a 3x3 matrix filled with a single character denoting the color (`'W'` for white, `'Y'` for yellow, `'G'` for green, `'B'` for blue, `'O'` for orange, `'R'` for red).

###### Methods

- **`__init__(self)`**: Initializes the cube in a solved state.

- **`rotate_face_clockwise(self, face)`**: Rotates the specified face (`'U'`, `'D'`, `'F'`, `'B'`, `'L'`, `'R'`) of the cube 90 degrees clockwise.

- **`rotate_face_counterclockwise(self, face)`**: Rotates the specified face 90 degrees counterclockwise.

- **`rotate_slice(self, slice_index, axis, direction)`**: (Placeholder) Rotates a slice of the cube along a given axis. This method is intended for more advanced manipulations of the cube and will affect multiple faces.

- **`apply_move(self, move)`**: Applies a single move (e.g., `'R'`, `'R'`, `'L'`, `'U'`, etc.) to the cube. This method calls the appropriate face rotation methods.

- **`is_solved(self)`**: Checks if the cube is in a solved state, where each face consists of a single color.

- **`__str__(self)`**: Returns a string representation of the cube's current state, useful for debugging and visualization.

#### Example Usage

```python
from cube import Cube

# Initialize the cube
cube = Cube()

# Print the initial state of the cube
print(cube)

# Apply a move (right face clockwise rotation)
cube.apply_move('R')

# Print the state of the cube after the move
print(cube)

# Check if the cube is solved
if cube.is_solved():
    print("The cube is solved!")
else:
    print("The cube is not solved.")
```

#### Future Work

- **Implement `rotate_slice` Method**: This method will allow for rotating slices of the cube, affecting multiple faces at once.
- **Enhance `apply_move` Method**: Expand this method to handle more complex sequences of moves.
- **Add Graphical Visualization**: Consider adding a graphical representation of the cube for a more intuitive visualization.

#### Dependencies

- `numpy`: Used for matrix manipulation of the cube's faces. You can install it via pip:

```bash
pip install numpy
```


### moves.py - Cube Movements

(Briefly describe and link to a detailed section if necessary)

## Contributing
If you'd like to contribute to the project, feel free to submit a pull request. Please ensure your code follows the existing style and includes tests for any new features.

## License
License details...

## Contact Information
dorotej.d.arnold@gmail.com - Dorotej-Dado Arnold
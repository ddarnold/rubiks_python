import matplotlib.pyplot as plt
import numpy as np

class CubeVisualizer:
    def __init__(self, cube):
        self.cube = cube

    def plot_face(self, ax, face, color):
        """Plot a single face of the cube."""
        ax.imshow(np.full((3, 3), color), cmap='tab10', vmin=0, vmax=9)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(face)

    def plot_cube(self):
        """Plot the entire Rubik's Cube."""
        fig, axs = plt.subplots(3, 3, figsize=(9, 9))
        plt.subplots_adjust(wspace=0.05, hspace=0.05)

        # Define face colors based on typical Rubik's Cube color scheme
        face_colors = {
            'U': 'white',
            'D': 'yellow',
            'F': 'green',
            'B': 'blue',
            'L': 'orange',
            'R': 'red'
        }

        # Plot each face
        faces_order = ['U', 'L', 'F', 'R', 'B', 'D']
        for i, face in enumerate(faces_order):
            row = i // 3
            col = i % 3
            self.plot_face(axs[row, col], face, face_colors[face])
        
        plt.show()

class Cube:
    def __init__(self):
        self.faces = {
            'U': 'W',
            'D': 'Y',
            'F': 'G',
            'B': 'B',
            'L': 'O',
            'R': 'R'
        }
        # Initialization of the cube faces with default colors
        self.faces = {k: np.full((3, 3), v) for k, v in self.faces.items()}

# Example Usage
cube = Cube()
visualizer = CubeVisualizer(cube)
visualizer.plot_cube()
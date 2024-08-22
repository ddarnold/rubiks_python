import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

class CubeVisualizer:
    def __init__(self, cube):
        self.cube = cube
        # Define color mappings for each face
        self.color_mapping = {
            'W': 0,  # White
            'Y': 1,  # Yellow
            'G': 2,  # Green
            'B': 3,  # Blue
            'R': 4,  # Red
            'O': 5   # Orange
        }
        # Define the colors to be used in the plot
        self.colors = ['white', 'yellow', 'green', 'blue', 'red', 'orange']
        self.cmap = ListedColormap(self.colors)

    def plot_face(self, ax, face_data):
        # Convert face_data to an array of integers using the color mapping
        face_colors = np.vectorize(self.color_mapping.get)(face_data)
        ax.imshow(face_colors, cmap=self.cmap, vmin=0, vmax=len(self.colors) - 1)
        ax.set_xticks([])  # Remove x-axis ticks
        ax.set_yticks([])  # Remove y-axis ticks

    def plot_cube(self):
        fig, axs = plt.subplots(3, 4, figsize=(8, 6))

        # Layout mapping for the cube faces (top view)
        layout = {
            'U': (0, 1),
            'L': (1, 0),
            'F': (1, 1),
            'R': (1, 2),
            'B': (1, 3),
            'D': (2, 1)
        }

        # Plot each face in its respective subplot
        for face, (row, col) in layout.items():
            self.plot_face(axs[row, col], self.cube.faces[face])
            axs[row, col].set_title(f"{face} face")

        # Hide unused subplots
        for i in range(3):
            for j in range(4):
                if (i, j) not in layout.values():
                    axs[i, j].axis('off')

        plt.show()
        
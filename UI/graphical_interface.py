import tkinter as tk
from Cube import cube
from Cube.cube import Cube
from Cube.moves import apply_move_sequence
from Visualization.graphical_visualization import CubeVisualizer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CubeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rubik's Cube GUI")
        
        # Initialize the Cube and Visualizer
        self.cube = Cube()
        self.cube.make_minority_cross()
        self.visualizer = CubeVisualizer(self.cube)
        
        # Create Buttons for Patterns
        self.create_pattern_buttons()
        
        # Create Canvas for Visualization
        self.figure, self.axs = plt.subplots(3, 4, figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        # Create Buttons for Moves
        self.create_move_buttons()
        
        # Initial Cube Visualization
        self.update_visualization()
    
    def create_move_buttons(self):
        """Create move buttons for the GUI."""
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.BOTTOM)
        
        moves = ["L", "L'", "M", "M'", "R", "R'", "U", "U'", "E", "E'", "D", "D'", "F", "F'", "S", "S'", "B", "B'", "X", "X'", "Y", "Y'", "Z", "Z'"]
        for move in moves:
            button = tk.Button(button_frame, text=move, command=lambda m=move: self.apply_move(m))
            button.pack(side=tk.LEFT)
    
    def create_pattern_buttons(self):
        """Create pattern buttons for the GUI."""
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        patterns = ["checkerboard", "giftbox", "minority_cross", "perfect_scrumble", "solved"]
        for pattern in patterns:
            button = tk.Button(button_frame, text=pattern, command=lambda p=pattern: self.apply_pattern(p))
            button.pack(side=tk.LEFT)
    
    def apply_move(self, move):
        """Apply the move to the cube and update the visualization."""
        apply_move_sequence(self.cube, move)
        self.update_visualization()
        
    def apply_pattern(self, pattern):
        if pattern == "checkerboard":
            self.cube.make_checkerboard()
        elif pattern == "giftbox":
            self.cube.make_giftbox()
        elif pattern == "minority_cross":
            self.cube.make_minority_cross()
        elif pattern == "perfect_scrumble":
            self.cube.make_perfect_scramble()
        elif pattern == "solved":
            self.cube.make_solved()
        
        self.update_visualization()
    
    def update_visualization(self):
        """Update the cube visualization on the canvas."""
        for ax in self.axs.flatten():
            ax.clear()
        self.visualizer.plot_cube(self.axs)
        self.canvas.draw()

def main():
    root = tk.Tk()
    gui = CubeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

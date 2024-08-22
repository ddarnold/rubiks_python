from Cube.cube import Cube
from Visualization.graphical_visualization import CubeVisualizer

def main():
    # Initialize the cube
    cube = Cube()
    
    # Display the initial state of the cube
    visualizer = CubeVisualizer(cube)
    print("Initial Cube State:")
    visualizer.plot_cube()    
    # print(cube)
    
if __name__ == "__main__":
    main()
    
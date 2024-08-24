from Cube.cube import Cube
from Cube.moves import apply_move_sequence
from Visualization.graphical_visualization import CubeVisualizer

def main():
    # Initialize the cube
    cube = Cube()
    visualizer = CubeVisualizer(cube)

    # apply_move_sequence(cube, 'LLD\'BBLLBBD\'FFDU\'BBLBBF\'LB\'FU\'F\'ULL')
    visualizer.plot_cube()
    
    
if __name__ == "__main__":
    main()
    
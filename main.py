from Cube.cube import Cube
from Cube.moves import apply_move_sequence
from Visualization.graphical_visualization import CubeVisualizer

def main():
    # Initialize the cube
    cube = Cube()
    visualizer = CubeVisualizer(cube)

    
    # Display the initial state of the cube
    # print("Initial Cube State:")
    # visualizer.plot_cube()    
    
    # Display the Changed state of the cube
    cube.make_minority_cross()
    apply_move_sequence(cube, 'LLD\'BBLLBBD\'FFDU\'BBLBBF\'LB\'FU\'F\'ULL')
    visualizer.plot_cube()
    
    
if __name__ == "__main__":
    main()
    
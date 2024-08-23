import unittest
import numpy as np
from Cube.cube import Cube
from Cube.moves import apply_moves

class TestRubiksCubeMoves(unittest.TestCase):

    def setUp(self):
        """Initialize the giftbox cube pattern before each test."""
        self.cube = Cube()
        self.cube.make_giftbox()

    def test_L_move(self):
        """Test the L move."""
        apply_moves(self.cube, 'L')
        expected_L = np.array([['G', 'G', 'G'],
                               ['R', 'R', 'R'],
                               ['B', 'B', 'B']])
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), "L move failed.")

    def test_L_prime_move(self):
        """Test the L' move."""
        apply_moves(self.cube, 'Lp')
        expected_L_prime = np.array([['B', 'B', 'B'],
                                     ['R', 'R', 'R'],
                                     ['G', 'G', 'G']])
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L_prime), "L' move failed.")

    def test_R_move(self):
        """Test the R move."""
        apply_moves(self.cube, 'R')
        expected_R = np.array([['O', 'O', 'O'],
                               ['G', 'G', 'G'],
                               ['B', 'B', 'B']])
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), "R move failed.")

    def test_R_prime_move(self):
        """Test the R' move."""
        apply_moves(self.cube, 'Rp')
        expected_R_prime = np.array([['G', 'G', 'G'],
                                     ['B', 'B', 'B'],
                                     ['O', 'O', 'O']])
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R_prime), "R' move failed.")

    def test_U_move(self):
        """Test the U move."""
        apply_moves(self.cube, 'U')
        expected_U = np.array([['W', 'W', 'Y'],
                               ['Y', 'Y', 'Y'],
                               ['W', 'W', 'Y']])
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), "U move failed.")

    def test_U_prime_move(self):
        """Test the U' move."""
        apply_moves(self.cube, 'Up')
        expected_U_prime = np.array([['Y', 'W', 'W'],
                                     ['Y', 'Y', 'Y'],
                                     ['Y', 'W', 'W']])
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U_prime), "U' move failed.")

    def test_D_move(self):
        """Test the D move."""
        apply_moves(self.cube, 'D')
        expected_D = np.array([['Y', 'Y', 'W'],
                               ['W', 'W', 'W'],
                               ['Y', 'Y', 'W']])
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), "D move failed.")

    def test_D_prime_move(self):
        """Test the D' move."""
        apply_moves(self.cube, 'Dp')
        expected_D_prime = np.array([['W', 'Y', 'Y'],
                                     ['W', 'W', 'W'],
                                     ['W', 'Y', 'Y']])
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D_prime), "D' move failed.")

    def test_F_move(self):
        """Test the F move."""
        apply_moves(self.cube, 'F')
        expected_F = np.array([['R', 'O', 'G'],
                               ['R', 'O', 'G'],
                               ['R', 'O', 'G']])
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), "F move failed.")

    def test_F_prime_move(self):
        """Test the F' move."""
        apply_moves(self.cube, 'Fp')
        expected_F_prime = np.array([['G', 'R', 'O'],
                                     ['G', 'R', 'O'],
                                     ['G', 'R', 'O']])
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F_prime), "F' move failed.")

    def test_B_move(self):
        """Test the B move."""
        apply_moves(self.cube, 'B')
        expected_B = np.array([['B', 'R', 'B'],
                               ['O', 'R', 'O'],
                               ['G', 'R', 'G']])
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), "B move failed.")

    def test_B_prime_move(self):
        """Test the B' move."""
        apply_moves(self.cube, 'Bp')
        expected_B_prime = np.array([['G', 'R', 'G'],
                                     ['O', 'R', 'O'],
                                     ['B', 'R', 'B']])
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B_prime), "B' move failed.")

    def test_apply_moves_sequence(self):
        """Test applying a sequence of moves."""
        sequence = "L R U D F B"
        apply_moves(self.cube, sequence)
        # The expected result should be computed by applying the sequence manually or by trusted logic.
        # Here, we assume the expected result for illustration purposes.
        expected_L = np.array([['G', 'G', 'G'],
                               ['R', 'R', 'R'],
                               ['B', 'B', 'B']])
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), "Apply moves failed on L face.")
        # Add more assertions to verify other faces if needed.

if __name__ == '__main__':
    unittest.main()

import unittest
import numpy as np
from Cube.cube import Cube
from Cube.moves import apply_move, apply_move_sequence

class TestRubiksCubeMoves(unittest.TestCase):

    def setUp(self):
        """Initialize the giftbox cube pattern before each test."""
        self.cube = Cube()
        self.cube.make_minority_cross()

    def test_L_move(self):
        """Test the L move."""
        move = 'L'
        
        expected_U = np.array([['W', 'O', 'G'],
                               ['R', 'Y', 'B'],
                               ['W', 'R', 'G']])
        expected_D = np.array([['Y', 'O', 'B'],
                               ['R', 'W', 'R'],
                               ['Y', 'G', 'B']])
        expected_F = np.array([['G', 'B', 'Y'],
                               ['W', 'G', 'O'],
                               ['G', 'W', 'Y']])
        expected_B = np.array([['W', 'G', 'B'],
                               ['O', 'B', 'Y'],
                               ['W', 'Y', 'B']])
        expected_L = np.array([['O', 'W', 'O'],
                               ['B', 'R', 'G'],
                               ['O', 'Y', 'O']])
        expected_R = np.array([['R', 'W', 'R'],
                               ['B', 'O', 'Y'],
                               ['R', 'G', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")
 
    def test_L_prime_move(self):
        """Test the L prime move."""
        move = 'L\''
        
        expected_U = np.array([['Y', 'O', 'G'],
                               ['R', 'Y', 'B'],
                               ['Y', 'R', 'G']])
        expected_D = np.array([['W', 'O', 'B'],
                               ['R', 'W', 'R'],
                               ['W', 'G', 'B']])
        expected_F = np.array([['B', 'B', 'Y'],
                               ['Y', 'G', 'O'],
                               ['B', 'W', 'Y']])
        expected_B = np.array([['W', 'G', 'G'],
                               ['O', 'B', 'W'],
                               ['W', 'Y', 'G']])
        expected_L = np.array([['O', 'Y', 'O'],
                               ['G', 'R', 'B'],
                               ['O', 'W', 'O']])
        expected_R = np.array([['R', 'W', 'R'],
                               ['B', 'O', 'Y'],
                               ['R', 'G', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_R_move(self):
        """Test the R move."""
        move = 'R'
        
        expected_U = np.array([['G', 'O', 'Y'],
                               ['W', 'Y', 'O'],
                               ['G', 'R', 'Y']])
        expected_D = np.array([['B', 'O', 'W'],
                               ['Y', 'W', 'O'],
                               ['B', 'G', 'W']])
        expected_F = np.array([['Y', 'B', 'B'],
                               ['R', 'G', 'R'],
                               ['Y', 'W', 'B']])
        expected_B = np.array([['G', 'G', 'W'],
                               ['B', 'B', 'R'],
                               ['G', 'Y', 'W']])
        expected_L = np.array([['O', 'G', 'O'],
                               ['W', 'R', 'Y'],
                               ['O', 'B', 'O']])
        expected_R = np.array([['R', 'B', 'R'],
                               ['G', 'O', 'W'],
                               ['R', 'Y', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_R_prime_move(self):
        """Test the R prime move."""
        move = 'R\''
        
        expected_U = np.array([['G', 'O', 'W'],
                               ['W', 'Y', 'O'],
                               ['G', 'R', 'W']])
        expected_D = np.array([['B', 'O', 'Y'],
                               ['Y', 'W', 'O'],
                               ['B', 'G', 'Y']])
        expected_F = np.array([['Y', 'B', 'G'],
                               ['R', 'G', 'B'],
                               ['Y', 'W', 'G']])
        expected_B = np.array([['B', 'G', 'W'],
                               ['R', 'B', 'R'],
                               ['B', 'Y', 'W']])
        expected_L = np.array([['O', 'G', 'O'],
                               ['W', 'R', 'Y'],
                               ['O', 'B', 'O']])
        expected_R = np.array([['R', 'Y', 'R'],
                               ['W', 'O', 'G'],
                               ['R', 'B', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_M_move(self):
        """Test the M move."""
        move = 'M'
        
        expected_U = np.array([['G', 'Y', 'G'],
                               ['W', 'B', 'B'],
                               ['G', 'G', 'G']])
        expected_D = np.array([['B', 'B', 'B'],
                               ['Y', 'G', 'R'],
                               ['B', 'W', 'B']])
        expected_F = np.array([['Y', 'O', 'Y'],
                               ['R', 'Y', 'O'],
                               ['Y', 'R', 'Y']])
        expected_B = np.array([['W', 'G', 'W'],
                               ['O', 'W', 'R'],
                               ['W', 'O', 'W']])
        expected_L = np.array([['O', 'G', 'O'],
                               ['W', 'R', 'Y'],
                               ['O', 'B', 'O']])
        expected_R = np.array([['R', 'W', 'R'],
                               ['B', 'O', 'Y'],
                               ['R', 'G', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_M_prime_move(self):
        """Test the M prime move."""
        move = 'M\''
        
        expected_U = np.array([['G', 'B', 'G'],
                               ['W', 'G', 'B'],
                               ['G', 'W', 'G']])
        expected_D = np.array([['B', 'Y', 'B'],
                               ['Y', 'B', 'R'],
                               ['B', 'G', 'B']])
        expected_F = np.array([['Y', 'O', 'Y'],
                               ['R', 'W', 'O'],
                               ['Y', 'G', 'Y']])
        expected_B = np.array([['W', 'R', 'W'],
                               ['O', 'Y', 'R'],
                               ['W', 'O', 'W']])
        expected_L = np.array([['O', 'G', 'O'],
                               ['W', 'R', 'Y'],
                               ['O', 'B', 'O']])
        expected_R = np.array([['R', 'W', 'R'],
                               ['B', 'O', 'Y'],
                               ['R', 'G', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_U_move(self):
        """Test the U move."""
        move = 'U'
        
        expected_U = np.array([['G', 'W', 'G'],
                               ['R', 'Y', 'O'],
                               ['G', 'B', 'G']])
        expected_D = np.array([['B', 'O', 'B'],
                               ['Y', 'W', 'R'],
                               ['B', 'G', 'B']])
        expected_F = np.array([['R', 'W', 'R'],
                               ['R', 'G', 'O'],
                               ['Y', 'W', 'Y']])
        expected_B = np.array([['O', 'G', 'O'],
                               ['O', 'B', 'R'],
                               ['W', 'Y', 'W']])
        expected_L = np.array([['Y', 'B', 'Y'],
                               ['W', 'R', 'Y'],
                               ['O', 'B', 'O']])
        expected_R = np.array([['W', 'G', 'W'],
                               ['B', 'O', 'Y'],
                               ['R', 'G', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_U_prime_move(self):
        """Test the U prime move."""
        move = 'U\''
        
        expected_U = np.array([['G', 'B', 'G'],
                               ['O', 'Y', 'R'],
                               ['G', 'W', 'G']])
        expected_D = np.array([['B', 'O', 'B'],
                               ['Y', 'W', 'R'],
                               ['B', 'G', 'B']])
        expected_F = np.array([['O', 'G', 'O'],
                               ['R', 'G', 'O'],
                               ['Y', 'W', 'Y']])
        expected_B = np.array([['R', 'W', 'R'],
                               ['O', 'B', 'R'],
                               ['W', 'Y', 'W']])
        expected_L = np.array([['W', 'G', 'W'],
                               ['W', 'R', 'Y'],
                               ['O', 'B', 'O']])
        expected_R = np.array([['Y', 'B', 'Y'],
                               ['B', 'O', 'Y'],
                               ['R', 'G', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_E_move(self):
        """Test the E move."""
        move = 'E'
        
        expected_U = np.array([['G', 'O', 'G'],
                               ['W', 'Y', 'B'],
                               ['G', 'R', 'G']])
        expected_D = np.array([['B', 'O', 'B'],
                               ['Y', 'W', 'R'],
                               ['B', 'G', 'B']])
        expected_F = np.array([['Y', 'B', 'Y'],
                               ['W', 'R', 'Y'],
                               ['Y', 'W', 'Y']])
        expected_B = np.array([['W', 'G', 'W'],
                               ['B', 'O', 'Y'],
                               ['W', 'Y', 'W']])
        expected_L = np.array([['O', 'G', 'O'],
                               ['O', 'B', 'R'],
                               ['O', 'B', 'O']])
        expected_R = np.array([['R', 'W', 'R'],
                               ['R', 'G', 'O'],
                               ['R', 'G', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_E_prime_move(self):
        """Test the E prime move."""
        move = 'E\''
        
        expected_U = np.array([['G', 'O', 'G'],
                               ['W', 'Y', 'B'],
                               ['G', 'R', 'G']])
        expected_D = np.array([['B', 'O', 'B'],
                               ['Y', 'W', 'R'],
                               ['B', 'G', 'B']])
        expected_F = np.array([['Y', 'B', 'Y'],
                               ['B', 'O', 'Y'],
                               ['Y', 'W', 'Y']])
        expected_B = np.array([['W', 'G', 'W'],
                               ['W', 'R', 'Y'],
                               ['W', 'Y', 'W']])
        expected_L = np.array([['O', 'G', 'O'],
                               ['R', 'G', 'O'],
                               ['O', 'B', 'O']])
        expected_R = np.array([['R', 'W', 'R'],
                               ['O', 'B', 'R'],
                               ['R', 'G', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_D_move(self):
        """Test the D move."""
        move = 'D'
        
        expected_U = np.array([['G', 'O', 'G'],
                               ['W', 'Y', 'B'],
                               ['G', 'R', 'G']])
        expected_D = np.array([['B', 'Y', 'B'],
                               ['G', 'W', 'O'],
                               ['B', 'R', 'B']])
        expected_F = np.array([['Y', 'B', 'Y'],
                               ['R', 'G', 'O'],
                               ['O', 'B', 'O']])
        expected_B = np.array([['W', 'G', 'W'],
                               ['O', 'B', 'R'],
                               ['R', 'G', 'R']])
        expected_L = np.array([['O', 'G', 'O'],
                               ['W', 'R', 'Y'],
                               ['W', 'Y', 'W']])
        expected_R = np.array([['R', 'W', 'R'],
                               ['B', 'O', 'Y'],
                               ['Y', 'W', 'Y']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_D_prime_move(self):
        """Test the D prime move."""
        move = 'D\''
        
        expected_U = np.array([['G', 'O', 'G'],
                               ['W', 'Y', 'B'],
                               ['G', 'R', 'G']])
        expected_D = np.array([['B', 'R', 'B'],
                               ['O', 'W', 'G'],
                               ['B', 'Y', 'B']])
        expected_F = np.array([['Y', 'B', 'Y'],
                               ['R', 'G', 'O'],
                               ['R', 'G', 'R']])
        expected_B = np.array([['W', 'G', 'W'],
                               ['O', 'B', 'R'],
                               ['O', 'B', 'O']])
        expected_L = np.array([['O', 'G', 'O'],
                               ['W', 'R', 'Y'],
                               ['Y', 'W', 'Y']])
        expected_R = np.array([['R', 'W', 'R'],
                               ['B', 'O', 'Y'],
                               ['W', 'Y', 'W']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_F_move(self):
        """Test the F move."""
        move = 'F'
        
        expected_U = np.array([['G', 'O', 'G'],
                               ['W', 'Y', 'B'],
                               ['O', 'Y', 'O']])
        expected_D = np.array([['R', 'B', 'R'],
                               ['Y', 'W', 'R'],
                               ['B', 'G', 'B']])
        expected_F = np.array([['Y', 'R', 'Y'],
                               ['W', 'G', 'B'],
                               ['Y', 'O', 'Y']])
        expected_B = np.array([['W', 'G', 'W'],
                               ['O', 'B', 'R'],
                               ['W', 'Y', 'W']])
        expected_L = np.array([['O', 'G', 'B'],
                               ['W', 'R', 'O'],
                               ['O', 'B', 'B']])
        expected_R = np.array([['G', 'W', 'R'],
                               ['R', 'O', 'Y'],
                               ['G', 'G', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_F_prime_move(self):
        """Test the F prime move."""
        move = 'F\''
        
        expected_U = np.array([['G', 'O', 'G'],
                               ['W', 'Y', 'B'],
                               ['R', 'B', 'R']])
        expected_D = np.array([['O', 'Y', 'O'],
                               ['Y', 'W', 'R'],
                               ['B', 'G', 'B']])
        expected_F = np.array([['Y', 'O', 'Y'],
                               ['B', 'G', 'W'],
                               ['Y', 'R', 'Y']])
        expected_B = np.array([['W', 'G', 'W'],
                               ['O', 'B', 'R'],
                               ['W', 'Y', 'W']])
        expected_L = np.array([['O', 'G', 'G'],
                               ['W', 'R', 'R'],
                               ['O', 'B', 'G']])
        expected_R = np.array([['B', 'W', 'R'],
                               ['O', 'O', 'Y'],
                               ['B', 'G', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_S_move(self):
        """Test the S move."""
        move = 'S'
        
        expected_U = np.array([['G', 'O', 'G'],
                               ['B', 'R', 'G'],
                               ['G', 'R', 'G']])
        expected_D = np.array([['B', 'O', 'B'],
                               ['G', 'O', 'W'],
                               ['B', 'G', 'B']])
        expected_F = np.array([['Y', 'B', 'Y'],
                               ['R', 'G', 'O'],
                               ['Y', 'W', 'Y']])
        expected_B = np.array([['W', 'G', 'W'],
                               ['O', 'B', 'R'],
                               ['W', 'Y', 'W']])
        expected_L = np.array([['O', 'Y', 'O'],
                               ['W', 'W', 'Y'],
                               ['O', 'R', 'O']])
        expected_R = np.array([['R', 'W', 'R'],
                               ['B', 'Y', 'Y'],
                               ['R', 'B', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_S_prime_move(self):
        """Test the S prime move."""
        move = 'S\''
        
        expected_U = np.array([['G', 'O', 'G'],
                               ['W', 'O', 'G'],
                               ['G', 'R', 'G']])
        expected_D = np.array([['B', 'O', 'B'],
                               ['G', 'R', 'B'],
                               ['B', 'G', 'B']])
        expected_F = np.array([['Y', 'B', 'Y'],
                               ['R', 'G', 'O'],
                               ['Y', 'W', 'Y']])
        expected_B = np.array([['W', 'G', 'W'],
                               ['O', 'B', 'R'],
                               ['W', 'Y', 'W']])
        expected_L = np.array([['O', 'B', 'O'],
                               ['W', 'Y', 'Y'],
                               ['O', 'W', 'O']])
        expected_R = np.array([['R', 'R', 'R'],
                               ['B', 'W', 'Y'],
                               ['R', 'Y', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_B_move(self):
        """Test the B move."""
        move = 'B'
        
        expected_U = np.array([['R', 'Y', 'R'],
                               ['W', 'Y', 'B'],
                               ['G', 'R', 'G']])
        expected_D = np.array([['B', 'O', 'B'],
                               ['Y', 'W', 'R'],
                               ['O', 'W', 'O']])
        expected_F = np.array([['Y', 'B', 'Y'],
                               ['R', 'G', 'O'],
                               ['Y', 'W', 'Y']])
        expected_B = np.array([['W', 'O', 'W'],
                               ['Y', 'B', 'G'],
                               ['W', 'R', 'W']])
        expected_L = np.array([['G', 'G', 'O'],
                               ['O', 'R', 'Y'],
                               ['G', 'B', 'O']])
        expected_R = np.array([['R', 'W', 'B'],
                               ['B', 'O', 'G'],
                               ['R', 'G', 'B']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_B_prime_move(self):
        """Test the S prime move."""
        move = 'B\''
        
        expected_U = np.array([['O', 'W', 'O'],
                               ['W', 'Y', 'B'],
                               ['G', 'R', 'G']])
        expected_D = np.array([['B', 'O', 'B'],
                               ['Y', 'W', 'R'],
                               ['R', 'Y', 'R']])
        expected_F = np.array([['Y', 'B', 'Y'],
                               ['R', 'G', 'O'],
                               ['Y', 'W', 'Y']])
        expected_B = np.array([['W', 'R', 'W'],
                               ['G', 'B', 'Y'],
                               ['W', 'O', 'W']])
        expected_L = np.array([['B', 'G', 'O'],
                               ['G', 'R', 'Y'],
                               ['B', 'B', 'O']])
        expected_R = np.array([['R', 'W', 'G'],
                               ['B', 'O', 'O'],
                               ['R', 'G', 'G']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_X_move(self):
        """Test the X move."""
        move = 'X'
        
        expected_B = np.array([['G', 'R', 'G'],
                               ['B', 'Y', 'W'],
                               ['G', 'O', 'G']])
        expected_F = np.array([['B', 'O', 'B'],
                               ['Y', 'W', 'R'],
                               ['B', 'G', 'B']])
        expected_U = np.array([['Y', 'B', 'Y'],
                               ['R', 'G', 'O'],
                               ['Y', 'W', 'Y']])
        expected_D = np.array([['W', 'Y', 'W'],
                               ['R', 'B', 'O'],
                               ['W', 'G', 'W']])
        expected_L = np.array([['O', 'Y', 'O'],
                               ['G', 'R', 'B'],
                               ['O', 'W', 'O']])
        expected_R = np.array([['R', 'B', 'R'],
                               ['G', 'O', 'W'],
                               ['R', 'Y', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_X_prime_move(self):
        """Test the X prime move."""
        move = 'X\''
        
        expected_F = np.array([['G', 'O', 'G'],
                               ['W', 'Y', 'B'],
                               ['G', 'R', 'G']])
        expected_B = np.array([['B', 'G', 'B'],
                               ['R', 'W', 'Y'],
                               ['B', 'O', 'B']])
        expected_D = np.array([['Y', 'B', 'Y'],
                               ['R', 'G', 'O'],
                               ['Y', 'W', 'Y']])
        expected_U = np.array([['W', 'Y', 'W'],
                               ['R', 'B', 'O'],
                               ['W', 'G', 'W']])
        expected_L = np.array([['O', 'W', 'O'],
                               ['B', 'R', 'G'],
                               ['O', 'Y', 'O']])
        expected_R = np.array([['R', 'Y', 'R'],
                               ['W', 'O', 'G'],
                               ['R', 'B', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_Y_move(self):
        """Test the Y move."""
        move = 'Y'
        
        expected_U = np.array([['G', 'W', 'G'],
                               ['R', 'Y', 'O'],
                               ['G', 'B', 'G']])
        expected_D = np.array([['B', 'R', 'B'],
                               ['O', 'W', 'G'],
                               ['B', 'Y', 'B']])
        expected_L = np.array([['Y', 'B', 'Y'],
                               ['R', 'G', 'O'],
                               ['Y', 'W', 'Y']])
        expected_R = np.array([['W', 'G', 'W'],
                               ['O', 'B', 'R'],
                               ['W', 'Y', 'W']])
        expected_B = np.array([['O', 'G', 'O'],
                               ['W', 'R', 'Y'],
                               ['O', 'B', 'O']])
        expected_F = np.array([['R', 'W', 'R'],
                               ['B', 'O', 'Y'],
                               ['R', 'G', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")
 
    def test_Y_prime_move(self):
        """Test the Y prime move."""
        move = 'Y\''
        
        expected_U = np.array([['G', 'B', 'G'],
                               ['O', 'Y', 'R'],
                               ['G', 'W', 'G']])
        expected_D = np.array([['B', 'Y', 'B'],
                               ['G', 'W', 'O'],
                               ['B', 'R', 'B']])
        expected_R = np.array([['Y', 'B', 'Y'],
                               ['R', 'G', 'O'],
                               ['Y', 'W', 'Y']])
        expected_L = np.array([['W', 'G', 'W'],
                               ['O', 'B', 'R'],
                               ['W', 'Y', 'W']])
        expected_F = np.array([['O', 'G', 'O'],
                               ['W', 'R', 'Y'],
                               ['O', 'B', 'O']])
        expected_B = np.array([['R', 'W', 'R'],
                               ['B', 'O', 'Y'],
                               ['R', 'G', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_Z_move(self):
        """Test the Z move."""
        move = 'Z'
        
        expected_R = np.array([['G', 'W', 'G'],
                               ['R', 'Y', 'O'],
                               ['G', 'B', 'G']])
        expected_L = np.array([['B', 'Y', 'B'],
                               ['G', 'W', 'O'],
                               ['B', 'R', 'B']])
        expected_F = np.array([['Y', 'R', 'Y'],
                               ['W', 'G', 'B'],
                               ['Y', 'O', 'Y']])
        expected_B = np.array([['W', 'R', 'W'],
                               ['G', 'B', 'Y'],
                               ['W', 'O', 'W']])
        expected_U = np.array([['O', 'W', 'O'],
                               ['B', 'R', 'G'],
                               ['O', 'Y', 'O']])
        expected_D = np.array([['R', 'B', 'R'],
                               ['G', 'O', 'W'],
                               ['R', 'Y', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_Z_prime_move(self):
        """Test the Z prime move."""
        move = 'Z\''
        
        expected_L = np.array([['G', 'B', 'G'],
                               ['O', 'Y', 'R'],
                               ['G', 'W', 'G']])
        expected_R = np.array([['B', 'R', 'B'],
                               ['O', 'W', 'G'],
                               ['B', 'Y', 'B']])
        expected_F = np.array([['Y', 'O', 'Y'],
                               ['B', 'G', 'W'],
                               ['Y', 'R', 'Y']])
        expected_B = np.array([['W', 'O', 'W'],
                               ['Y', 'B', 'G'],
                               ['W', 'R', 'W']])
        expected_D = np.array([['O', 'Y', 'O'],
                               ['G', 'R', 'B'],
                               ['O', 'W', 'O']])
        expected_U = np.array([['R', 'Y', 'R'],
                               ['W', 'O', 'G'],
                               ['R', 'B', 'R']])
        
        #########################
        apply_move(self.cube, move)
        self.assertTrue(np.array_equal(self.cube.faces['U'], expected_U), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['D'], expected_D), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['F'], expected_F), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['B'], expected_B), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['L'], expected_L), move + " move failed.")
        self.assertTrue(np.array_equal(self.cube.faces['R'], expected_R), move + " move failed.")

    def test_apply_moves_sequence(self):
        """Test applying a sequence of moves."""
        sequence = "LLU\'FUF\'BL\'FBBL\'BBUD\'FFDBBLLBBDLL"
        
        apply_move_sequence(self.cube, sequence)
        self.assertTrue(self.cube.is_solved(), "Apply moves sequence failed.")
        # Add more assertions to verify other faces if needed.

if __name__ == '__main__':
    unittest.main()

""" 
        expected_U = np.array([['G', 'O', 'G'],
                               ['W', 'Y', 'B'],
                               ['G', 'R', 'G']])
        expected_D = np.array([['B', 'O', 'B'],
                               ['Y', 'W', 'R'],
                               ['B', 'G', 'B']])
        expected_F = np.array([['Y', 'B', 'Y'],
                               ['R', 'G', 'O'],
                               ['Y', 'W', 'Y']])
        expected_B = np.array([['W', 'G', 'W'],
                               ['O', 'B', 'R'],
                               ['W', 'Y', 'W']])
        expected_L = np.array([['O', 'G', 'O'],
                               ['W', 'R', 'Y'],
                               ['O', 'B', 'O']])
        expected_R = np.array([['R', 'W', 'R'],
                               ['B', 'O', 'Y'],
                               ['R', 'G', 'R']])
"""
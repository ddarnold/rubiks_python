import unittest
import numpy as np
from Cube.cube import Cube
from Cube.moves import apply_move, apply_move_sequence

class TestRubiksCubeMoves(unittest.TestCase):

    def setUp(self):
        """Initialize the giftbox cube pattern before each test."""
        self.cube = Cube()
        self.cube.make_perfect_scramble()

    def test_L_move(self):
        """Test the L move."""
        move = 'L'
        
        expected_U = np.array([['W', 'R', 'Y'],
                               ['Y', 'W', 'B'],
                               ['W', 'R', 'G']])
        expected_D = np.array([['O', 'W', 'B'],
                               ['W', 'Y', 'O'],
                               ['Y', 'B', 'R']])
        expected_F = np.array([['O', 'Y', 'W'],
                               ['G', 'G', 'B'],
                               ['B', 'O', 'R']])
        expected_B = np.array([['O', 'G', 'G'],
                               ['R', 'B', 'O'],
                               ['G', 'O', 'R']])
        expected_L = np.array([['R', 'G', 'B'],
                               ['Y', 'O', 'W'],
                               ['B', 'R', 'Y']])
        expected_R = np.array([['O', 'W', 'G'],
                               ['Y', 'R', 'B'],
                               ['W', 'G', 'Y']])
        
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
        
        expected_U = np.array([['O', 'R', 'Y'],
                               ['W', 'W', 'B'],
                               ['Y', 'R', 'G']])
        expected_D = np.array([['W', 'W', 'B'],
                               ['Y', 'Y', 'O'],
                               ['W', 'B', 'R']])
        expected_F = np.array([['R', 'Y', 'W'],
                               ['O', 'G', 'B'],
                               ['G', 'O', 'R']])
        expected_B = np.array([['O', 'G', 'B'],
                               ['R', 'B', 'G'],
                               ['G', 'O', 'O']])
        expected_L = np.array([['Y', 'R', 'B'],
                               ['W', 'O', 'Y'],
                               ['B', 'G', 'R']])
        expected_R = np.array([['O', 'W', 'G'],
                               ['Y', 'R', 'B'],
                               ['W', 'G', 'Y']])
        
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
        
        expected_U = np.array([['O', 'R', 'W'],
                               ['G', 'W', 'B'],
                               ['B', 'R', 'R']])
        expected_D = np.array([['R', 'W', 'G'],
                               ['O', 'Y', 'R'],
                               ['G', 'B', 'O']])
        expected_F = np.array([['O', 'Y', 'B'],
                               ['W', 'G', 'O'],
                               ['Y', 'O', 'R']])
        expected_B = np.array([['G', 'G', 'W'],
                               ['B', 'B', 'Y'],
                               ['Y', 'O', 'W']])
        expected_L = np.array([['B', 'W', 'Y'],
                               ['G', 'O', 'R'],
                               ['R', 'Y', 'B']])
        expected_R = np.array([['W', 'Y', 'O'],
                               ['G', 'R', 'W'],
                               ['Y', 'B', 'G']])
        
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
        
        expected_U = np.array([['O', 'R', 'G'],
                               ['G', 'W', 'R'],
                               ['B', 'R', 'O']])
        expected_D = np.array([['R', 'W', 'W'],
                               ['O', 'Y', 'B'],
                               ['G', 'B', 'R']])
        expected_F = np.array([['O', 'Y', 'Y'],
                               ['W', 'G', 'B'],
                               ['Y', 'O', 'G']])
        expected_B = np.array([['R', 'G', 'W'],
                               ['O', 'B', 'Y'],
                               ['B', 'O', 'W']])
        expected_L = np.array([['B', 'W', 'Y'],
                               ['G', 'O', 'R'],
                               ['R', 'Y', 'B']])
        expected_R = np.array([['G', 'B', 'Y'],
                               ['W', 'R', 'G'],
                               ['O', 'Y', 'W']])
        
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
        
        expected_U = np.array([['O', 'O', 'Y'],
                               ['G', 'B', 'B'],
                               ['B', 'G', 'G']])
        expected_D = np.array([['R', 'Y', 'B'],
                               ['O', 'G', 'O'],
                               ['G', 'O', 'R']])
        expected_F = np.array([['O', 'R', 'W'],
                               ['W', 'W', 'B'],
                               ['Y', 'R', 'R']])
        expected_B = np.array([['O', 'B', 'W'],
                               ['R', 'Y', 'Y'],
                               ['G', 'W', 'W']])
        expected_L = np.array([['B', 'W', 'Y'],
                               ['G', 'O', 'R'],
                               ['R', 'Y', 'B']])
        expected_R = np.array([['O', 'W', 'G'],
                               ['Y', 'R', 'B'],
                               ['W', 'G', 'Y']])
        
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
        
        expected_U = np.array([['O', 'Y', 'Y'],
                               ['G', 'G', 'B'],
                               ['B', 'O', 'G']])
        expected_D = np.array([['R', 'O', 'B'],
                               ['O', 'B', 'O'],
                               ['G', 'G', 'R']])
        expected_F = np.array([['O', 'W', 'W'],
                               ['W', 'Y', 'B'],
                               ['Y', 'B', 'R']])
        expected_B = np.array([['O', 'R', 'W'],
                               ['R', 'W', 'Y'],
                               ['G', 'R', 'W']])
        expected_L = np.array([['B', 'W', 'Y'],
                               ['G', 'O', 'R'],
                               ['R', 'Y', 'B']])
        expected_R = np.array([['O', 'W', 'G'],
                               ['Y', 'R', 'B'],
                               ['W', 'G', 'Y']])
        
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
        
        expected_U = np.array([['B', 'G', 'O'],
                               ['R', 'W', 'R'],
                               ['G', 'B', 'Y']])
        expected_D = np.array([['R', 'W', 'B'],
                               ['O', 'Y', 'O'],
                               ['G', 'B', 'R']])
        expected_F = np.array([['O', 'W', 'G'],
                               ['W', 'G', 'B'],
                               ['Y', 'O', 'R']])
        expected_B = np.array([['B', 'W', 'Y'],
                               ['R', 'B', 'Y'],
                               ['G', 'O', 'W']])
        expected_L = np.array([['O', 'Y', 'W'],
                               ['G', 'O', 'R'],
                               ['R', 'Y', 'B']])
        expected_R = np.array([['O', 'G', 'W'],
                               ['Y', 'R', 'B'],
                               ['W', 'G', 'Y']])
        
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
        
        expected_U = np.array([['Y', 'B', 'G'],
                               ['R', 'W', 'R'],
                               ['O', 'G', 'B']])
        expected_D = np.array([['R', 'W', 'B'],
                               ['O', 'Y', 'O'],
                               ['G', 'B', 'R']])
        expected_F = np.array([['B', 'W', 'Y'],
                               ['W', 'G', 'B'],
                               ['Y', 'O', 'R']])
        expected_B = np.array([['O', 'W', 'G'],
                               ['R', 'B', 'Y'],
                               ['G', 'O', 'W']])
        expected_L = np.array([['O', 'G', 'W'],
                               ['G', 'O', 'R'],
                               ['R', 'Y', 'B']])
        expected_R = np.array([['O', 'Y', 'W'],
                               ['Y', 'R', 'B'],
                               ['W', 'G', 'Y']])
        
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
        
        expected_U = np.array([['O', 'R', 'Y'],
                               ['G', 'W', 'B'],
                               ['B', 'R', 'G']])
        expected_D = np.array([['R', 'W', 'B'],
                               ['O', 'Y', 'O'],
                               ['G', 'B', 'R']])
        expected_F = np.array([['O', 'Y', 'W'],
                               ['G', 'O', 'R'],
                               ['Y', 'O', 'R']])
        expected_B = np.array([['O', 'G', 'W'],
                               ['Y', 'R', 'B'],
                               ['G', 'O', 'W']])
        expected_L = np.array([['B', 'W', 'Y'],
                               ['R', 'B', 'Y'],
                               ['R', 'Y', 'B']])
        expected_R = np.array([['O', 'W', 'G'],
                               ['W', 'G', 'B'],
                               ['W', 'G', 'Y']])
        
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
        
        expected_U = np.array([['O', 'R', 'Y'],
                               ['G', 'W', 'B'],
                               ['B', 'R', 'G']])
        expected_D = np.array([['R', 'W', 'B'],
                               ['O', 'Y', 'O'],
                               ['G', 'B', 'R']])
        expected_F = np.array([['O', 'Y', 'W'],
                               ['Y', 'R', 'B'],
                               ['Y', 'O', 'R']])
        expected_B = np.array([['O', 'G', 'W'],
                               ['G', 'O', 'R'],
                               ['G', 'O', 'W']])
        expected_L = np.array([['B', 'W', 'Y'],
                               ['W', 'G', 'B'],
                               ['R', 'Y', 'B']])
        expected_R = np.array([['O', 'W', 'G'],
                               ['R', 'B', 'Y'],
                               ['W', 'G', 'Y']])
        
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
        
        expected_U = np.array([['O', 'R', 'Y'],
                               ['G', 'W', 'B'],
                               ['B', 'R', 'G']])
        expected_D = np.array([['G', 'O', 'R'],
                               ['B', 'Y', 'W'],
                               ['R', 'O', 'B']])
        expected_F = np.array([['O', 'Y', 'W'],
                               ['W', 'G', 'B'],
                               ['R', 'Y', 'B']])
        expected_B = np.array([['O', 'G', 'W'],
                               ['R', 'B', 'Y'],
                               ['W', 'G', 'Y']])
        expected_L = np.array([['B', 'W', 'Y'],
                               ['G', 'O', 'R'],
                               ['G', 'O', 'W']])
        expected_R = np.array([['O', 'W', 'G'],
                               ['Y', 'R', 'B'],
                               ['Y', 'O', 'R']])
        
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
        
        expected_U = np.array([['O', 'R', 'Y'],
                               ['G', 'W', 'B'],
                               ['B', 'R', 'G']])
        expected_D = np.array([['B', 'O', 'R'],
                               ['W', 'Y', 'B'],
                               ['R', 'O', 'G']])
        expected_F = np.array([['O', 'Y', 'W'],
                               ['W', 'G', 'B'],
                               ['W', 'G', 'Y']])
        expected_B = np.array([['O', 'G', 'W'],
                               ['R', 'B', 'Y'],
                               ['R', 'Y', 'B']])
        expected_L = np.array([['B', 'W', 'Y'],
                               ['G', 'O', 'R'],
                               ['Y', 'O', 'R']])
        expected_R = np.array([['O', 'W', 'G'],
                               ['Y', 'R', 'B'],
                               ['G', 'O', 'W']])
        
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
        
        expected_U = np.array([['O', 'R', 'Y'],
                               ['G', 'W', 'B'],
                               ['B', 'R', 'Y']])
        expected_D = np.array([['W', 'Y', 'O'],
                               ['O', 'Y', 'O'],
                               ['G', 'B', 'R']])
        expected_F = np.array([['Y', 'W', 'O'],
                               ['O', 'G', 'Y'],
                               ['R', 'B', 'W']])
        expected_B = np.array([['O', 'G', 'W'],
                               ['R', 'B', 'Y'],
                               ['G', 'O', 'W']])
        expected_L = np.array([['B', 'W', 'R'],
                               ['G', 'O', 'W'],
                               ['R', 'Y', 'B']])
        expected_R = np.array([['B', 'W', 'G'],
                               ['R', 'R', 'B'],
                               ['G', 'G', 'Y']])
        
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
        
        expected_U = np.array([['O', 'R', 'Y'],
                               ['G', 'W', 'B'],
                               ['O', 'Y', 'W']])
        expected_D = np.array([['Y', 'R', 'B'],
                               ['O', 'Y', 'O'],
                               ['G', 'B', 'R']])
        expected_F = np.array([['W', 'B', 'R'],
                               ['Y', 'G', 'O'],
                               ['O', 'W', 'Y']])
        expected_B = np.array([['O', 'G', 'W'],
                               ['R', 'B', 'Y'],
                               ['G', 'O', 'W']])
        expected_L = np.array([['B', 'W', 'G'],
                               ['G', 'O', 'R'],
                               ['R', 'Y', 'B']])
        expected_R = np.array([['B', 'W', 'G'],
                               ['W', 'R', 'B'],
                               ['R', 'G', 'Y']])
        
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
        
        expected_U = np.array([['O', 'R', 'Y'],
                               ['Y', 'O', 'W'],
                               ['B', 'R', 'G']])
        expected_D = np.array([['R', 'W', 'B'],
                               ['G', 'R', 'W'],
                               ['G', 'B', 'R']])
        expected_F = np.array([['O', 'Y', 'W'],
                               ['W', 'G', 'B'],
                               ['Y', 'O', 'R']])
        expected_B = np.array([['O', 'G', 'W'],
                               ['R', 'B', 'Y'],
                               ['G', 'O', 'W']])
        expected_L = np.array([['B', 'O', 'Y'],
                               ['G', 'Y', 'R'],
                               ['R', 'O', 'B']])
        expected_R = np.array([['O', 'G', 'G'],
                               ['Y', 'W', 'B'],
                               ['W', 'B', 'Y']])
        
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
        
        expected_U = np.array([['O', 'R', 'Y'],
                               ['W', 'R', 'G'],
                               ['B', 'R', 'G']])
        expected_D = np.array([['R', 'W', 'B'],
                               ['W', 'O', 'Y'],
                               ['G', 'B', 'R']])
        expected_F = np.array([['O', 'Y', 'W'],
                               ['W', 'G', 'B'],
                               ['Y', 'O', 'R']])
        expected_B = np.array([['O', 'G', 'W'],
                               ['R', 'B', 'Y'],
                               ['G', 'O', 'W']])
        expected_L = np.array([['B', 'B', 'Y'],
                               ['G', 'W', 'R'],
                               ['R', 'G', 'B']])
        expected_R = np.array([['O', 'O', 'G'],
                               ['Y', 'Y', 'B'],
                               ['W', 'O', 'Y']])
        
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
        
        expected_U = np.array([['G', 'B', 'Y'],
                               ['G', 'W', 'B'],
                               ['B', 'R', 'G']])
        expected_D = np.array([['R', 'W', 'B'],
                               ['O', 'Y', 'O'],
                               ['B', 'G', 'R']])
        expected_F = np.array([['O', 'Y', 'W'],
                               ['W', 'G', 'B'],
                               ['Y', 'O', 'R']])
        expected_B = np.array([['G', 'R', 'O'],
                               ['O', 'B', 'G'],
                               ['W', 'Y', 'W']])
        expected_L = np.array([['Y', 'W', 'Y'],
                               ['R', 'O', 'R'],
                               ['O', 'Y', 'B']])
        expected_R = np.array([['O', 'W', 'R'],
                               ['Y', 'R', 'B'],
                               ['W', 'G', 'G']])
        
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
        
        expected_U = np.array([['R', 'G', 'B'],
                               ['G', 'W', 'B'],
                               ['B', 'R', 'G']])
        expected_D = np.array([['R', 'W', 'B'],
                               ['O', 'Y', 'O'],
                               ['Y', 'B', 'G']])
        expected_F = np.array([['O', 'Y', 'W'],
                               ['W', 'G', 'B'],
                               ['Y', 'O', 'R']])
        expected_B = np.array([['W', 'Y', 'W'],
                               ['G', 'B', 'O'],
                               ['O', 'R', 'G']])
        expected_L = np.array([['G', 'W', 'Y'],
                               ['B', 'O', 'R'],
                               ['R', 'Y', 'B']])
        expected_R = np.array([['O', 'W', 'O'],
                               ['Y', 'R', 'R'],
                               ['W', 'G', 'Y']])
        
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
        
        expected_U = np.array([['O', 'Y', 'W'],
                               ['W', 'G', 'B'],
                               ['Y', 'O', 'R']])
        expected_D = np.array([['W', 'O', 'G'],
                               ['Y', 'B', 'R'],
                               ['W', 'G', 'O']])
        expected_F = np.array([['R', 'W', 'B'],
                               ['O', 'Y', 'O'],
                               ['G', 'B', 'R']])
        expected_B = np.array([['G', 'R', 'B'],
                               ['B', 'W', 'G'],
                               ['Y', 'R', 'O']])
        expected_L = np.array([['Y', 'R', 'B'],
                               ['W', 'O', 'Y'],
                               ['B', 'G', 'R']])
        expected_R = np.array([['W', 'Y', 'O'],
                               ['G', 'R', 'W'],
                               ['Y', 'B', 'G']])
        
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
        
        expected_U = np.array([['W', 'O', 'G'],
                               ['Y', 'B', 'R'],
                               ['W', 'G', 'O']])
        expected_D = np.array([['O', 'Y', 'W'],
                               ['W', 'G', 'B'],
                               ['Y', 'O', 'R']])
        expected_F = np.array([['O', 'R', 'Y'],
                               ['G', 'W', 'B'],
                               ['B', 'R', 'G']])
        expected_B = np.array([['R', 'B', 'G'],
                               ['O', 'Y', 'O'],
                               ['B', 'W', 'R']])
        expected_L = np.array([['R', 'G', 'B'],
                               ['Y', 'O', 'W'],
                               ['B', 'R', 'Y']])
        expected_R = np.array([['G', 'B', 'Y'],
                               ['W', 'R', 'G'],
                               ['O', 'Y', 'W']])
        
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
        
        expected_U = np.array([['B', 'G', 'O'],
                               ['R', 'W', 'R'],
                               ['G', 'B', 'Y']])
        expected_D = np.array([['B', 'O', 'R'],
                               ['W', 'Y', 'B'],
                               ['R', 'O', 'G']])
        expected_F = np.array([['O', 'W', 'G'],
                               ['Y', 'R', 'B'],
                               ['W', 'G', 'Y']])
        expected_B = np.array([['B', 'W', 'Y'],
                               ['G', 'O', 'R'],
                               ['R', 'Y', 'B']])
        expected_L = np.array([['O', 'Y', 'W'],
                               ['W', 'G', 'B'],
                               ['Y', 'O', 'R']])
        expected_R = np.array([['O', 'G', 'W'],
                               ['R', 'B', 'Y'],
                               ['G', 'O', 'W']])
        
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
        
        expected_U = np.array([['Y', 'B', 'G'],
                               ['R', 'W', 'R'],
                               ['O', 'G', 'B']])
        expected_D = np.array([['G', 'O', 'R'],
                               ['B', 'Y', 'W'],
                               ['R', 'O', 'B']])
        expected_F = np.array([['B', 'W', 'Y'],
                               ['G', 'O', 'R'],
                               ['R', 'Y', 'B']])
        expected_B = np.array([['O', 'W', 'G'],
                               ['Y', 'R', 'B'],
                               ['W', 'G', 'Y']])
        expected_L = np.array([['O', 'G', 'W'],
                               ['R', 'B', 'Y'],
                               ['G', 'O', 'W']])
        expected_R = np.array([['O', 'Y', 'W'],
                               ['W', 'G', 'B'],
                               ['Y', 'O', 'R']])
        
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
        
        expected_U = np.array([['R', 'G', 'B'],
                               ['Y', 'O', 'W'],
                               ['B', 'R', 'Y']])
        expected_D = np.array([['W', 'Y', 'O'],
                               ['G', 'R', 'W'],
                               ['Y', 'B', 'G']])
        expected_F = np.array([['Y', 'W', 'O'],
                               ['O', 'G', 'Y'],
                               ['R', 'B', 'W']])
        expected_B = np.array([['W', 'Y', 'W'],
                               ['G', 'B', 'O'],
                               ['O', 'R', 'G']])
        expected_L = np.array([['G', 'O', 'R'],
                               ['B', 'Y', 'W'],
                               ['R', 'O', 'B']])
        expected_R = np.array([['B', 'G', 'O'],
                               ['R', 'W', 'R'],
                               ['G', 'B', 'Y']])
        
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
        
        expected_U = np.array([['G', 'B', 'Y'],
                               ['W', 'R', 'G'],
                               ['O', 'Y', 'W']])
        expected_D = np.array([['Y', 'R', 'B'],
                               ['W', 'O', 'Y'],
                               ['B', 'G', 'R']])
        expected_F = np.array([['W', 'B', 'R'],
                               ['Y', 'G', 'O'],
                               ['O', 'W', 'Y']])
        expected_B = np.array([['G', 'R', 'O'],
                               ['O', 'B', 'G'],
                               ['W', 'Y', 'W']])
        expected_L = np.array([['Y', 'B', 'G'],
                               ['R', 'W', 'R'],
                               ['O', 'G', 'B']])
        expected_R = np.array([['B', 'O', 'R'],
                               ['W', 'Y', 'B'],
                               ['R', 'O', 'G']])
        
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
        sequence = "L'DFDDRF'BRRUFFU'FUFFU'LLDDRRFFDD"
        
        apply_move_sequence(self.cube, sequence)
        self.assertTrue(self.cube.is_solved(), "Apply moves sequence failed.")
        # Add more assertions to verify other faces if needed.

if __name__ == '__main__':
    unittest.main()

""" 
        expected_U = np.array([['O', 'R', 'Y'],
                               ['G', 'W', 'B'],
                               ['B', 'R', 'G']])
        expected_D = np.array([['R', 'W', 'B'],
                               ['O', 'Y', 'O'],
                               ['G', 'B', 'R']])
        expected_F = np.array([['O', 'Y', 'W'],
                               ['W', 'G', 'B'],
                               ['Y', 'O', 'R']])
        expected_B = np.array([['O', 'G', 'W'],
                               ['R', 'B', 'Y'],
                               ['G', 'O', 'W']])
        expected_L = np.array([['B', 'W', 'Y'],
                               ['G', 'O', 'R'],
                               ['R', 'Y', 'B']])
        expected_R = np.array([['O', 'W', 'G'],
                               ['Y', 'R', 'B'],
                               ['W', 'G', 'Y']])
"""
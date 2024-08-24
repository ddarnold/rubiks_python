from Cube.cube import Cube
import numpy as np

def apply_move (cube, move_str):
    move_functions = {
        'L': __L,
        'L\'': __L_prime,
        'M': __M,
        'M\'': __M_prime,
        'R': __R,
        'R\'': __R_prime,
        'U': __U,
        'U\'': __U_prime,
        'E': __E,
        'E\'': __E_prime,
        'D': __D,
        'D\'': __D_prime,
        'F': __F,
        'F\'': __F_prime,
        'S': __S,
        'S\'': __S_prime,
        'B': __B,
        'B\'': __B_prime,
        'X': __X,
        'X\'': __X_prime,
        'Y': __Y,
        'Y\'': __Y_prime,
        'Z': __Z,
        'Z\'': __Z_prime
    }
    move_functions[move_str](cube)

def apply_move_sequence(cube, moves_str):
    moves_list = []
    i = 0

    while i < len(moves_str):
        # Check if the next character is a single quote
        if i + 1 < len(moves_str) and moves_str[i + 1] == "'":
            moves_list.append(moves_str[i:i+2])  # Append the character and the quote as a single move
            i += 2  # Move forward by 2 characters
        else:
            moves_list.append(moves_str[i])  # Append the single character
            i += 1  # Move forward by 1 character
    
    for move in moves_list:
        apply_move(cube, move)


# Basic rotations ##########################################

def __L(cube):
    cube.rotate_face('L', 'clockwise')
    cube.rotate_slice('y', 0, 'counterclockwise')

def __L_prime(cube):
    cube.rotate_face('L', 'counterclockwise')
    cube.rotate_slice('y', 0, 'clockwise')

def __M(cube):
    cube.rotate_slice('y', 1, 'counterclockwise')

def __M_prime(cube):
    cube.rotate_slice('y', 1, 'clockwise')

def __R(cube):
    cube.rotate_face('R', 'clockwise')
    cube.rotate_slice('y', 2, 'clockwise')

def __R_prime(cube):
    cube.rotate_face('R', 'counterclockwise')
    cube.rotate_slice('y', 2, "counterclockwise")

def __U(cube):
    cube.rotate_face('U', 'clockwise')
    cube.rotate_slice('x', 0, 'clockwise')

def __U_prime(cube):
    cube.rotate_face('U', 'counterclockwise')
    cube.rotate_slice('x', 0, "counterclockwise")   

def __E(cube):
    cube.rotate_slice('x', 1, 'counterclockwise')

def __E_prime(cube):
    cube.rotate_slice('x', 1, "clockwise")
    
def __D(cube):
    cube.rotate_face('D', 'clockwise')
    cube.rotate_slice('x', 2, 'counterclockwise')

def __D_prime(cube):
    cube.rotate_face('D', 'counterclockwise')
    cube.rotate_slice('x', 2, "clockwise")   
    
def __F(cube):
    cube.rotate_face('F', 'clockwise')
    cube.rotate_slice('z', 0, 'clockwise')

def __F_prime(cube):
    cube.rotate_face('F', 'counterclockwise')
    cube.rotate_slice('z', 0, "counterclockwise")
    
def __S(cube):
    cube.rotate_slice('z', 1, 'clockwise')

def __S_prime(cube):
    cube.rotate_slice('z', 1, "counterclockwise")   

def __B(cube):
    cube.rotate_face('B', 'clockwise')
    cube.rotate_slice('z', 2, 'clockwise')

def __B_prime(cube):
    cube.rotate_face('B', 'counterclockwise')
    cube.rotate_slice('z', 2, "counterclockwise")
      
def  __X(cube):
    cube.rotate_face('L', 'counterclockwise')
    cube.rotate_face('R', 'clockwise')
    cube.change_axis('y', 'clockwise')

def  __X_prime(cube):
    cube.rotate_face('R', 'counterclockwise')
    cube.rotate_face('L', 'clockwise')
    cube.change_axis('y', 'counterclockwise')

def  __Y(cube):
    cube.rotate_face('D', 'counterclockwise')
    cube.rotate_face('U', 'clockwise')
    cube.change_axis('x', 'clockwise')

def  __Y_prime(cube):
    cube.rotate_face('D', 'clockwise')
    cube.rotate_face('U', 'counterclockwise')
    cube.change_axis('x', 'counterclockwise')

def  __Z(cube):
    cube.rotate_face('B', 'counterclockwise')
    cube.rotate_face('F', 'clockwise')
    cube.change_axis('z', 'clockwise')

def  __Z_prime(cube):
    cube.rotate_face('B', 'clockwise')
    cube.rotate_face('F', 'counterclockwise')
    cube.change_axis('z', 'counterclockwise')

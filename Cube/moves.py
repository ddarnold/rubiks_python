from Cube.cube import Cube
import numpy as np

def __L(cube):
    cube.rotate_face_clockwise('L')
    cube.rotate_slice('y', 0, 'counterclockwise')

def __L_prime(cube):
    cube.rotate_face_counterclockwise('L')
    cube.rotate_slice('y', 0, 'clockwise')

def __R(cube):
    cube.rotate_face_clockwise('R')
    cube.rotate_slice('y', 2, 'clockwise')

def __R_prime(cube):
    cube.rotate_face_counterclockwise('R')
    cube.rotate_slice('y', 2, "counterclockwise")

def __U(cube):
    cube.rotate_face_clockwise('U')
    cube.rotate_slice('x', 0, 'clockwise')

def __U_prime(cube):
    cube.rotate_face_counterclockwise('U')
    cube.rotate_slice('x', 0, "counterclockwise")   
    
def __D(cube):
    cube.rotate_face_clockwise('D')
    cube.rotate_slice('x', 2, 'counterclockwise')

def __D_prime(cube):
    cube.rotate_face_counterclockwise('D')
    cube.rotate_slice('x', 2, "clockwise")   
    
def __F(cube):
    cube.rotate_face_clockwise('F')
    cube.rotate_slice('z', 0, 'clockwise')

def __F_prime(cube):
    cube.rotate_face_counterclockwise('F')
    cube.rotate_slice('z', 0, "counterclockwise")   

def __B(cube):
    cube.rotate_face_clockwise('B')
    cube.rotate_slice('z', 2, 'clockwise')

def __B_prime(cube):
    cube.rotate_face_counterclockwise('B')
    cube.rotate_slice('z', 2, "counterclockwise")   
    

def apply_moves(cube, moves_str):
    moves = moves_str.split()
    move_functions = {
        'R': __R,
        'Rp': __R_prime,
        'L': __L,
        'Lp': __L_prime,
        'U': __U,
        'Up': __U_prime,
        'D': __D,
        'Dp': __D_prime,
        'F': __F,
        'Fp': __F_prime,
        'B': __B,
        'Bp': __B_prime
    }
    for move in moves:
        move_functions[move](cube)

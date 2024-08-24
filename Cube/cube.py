from ast import If
import numpy as np

class Cube:
    def __init__(self):
        self.faces = {
            'U': np.full((3, 3), 'Y'),
            'D': np.full((3, 3), 'W'),
            'F': np.full((3, 3), 'B'),
            'B': np.full((3, 3), 'G'),
            'L': np.full((3, 3), 'O'),
            'R': np.full((3, 3), 'R')
        }

    def is_solved(self):
        return all(np.all(face == face[0, 0]) for face in self.faces.values())

    def __str__(self):
        cube_str = ''
        for face, grid in self.faces.items():
            cube_str += f"{face} face:\n{grid}\n\n"
        return cube_str

# Cube changes ##############################################    

    def rotate_face(self, face, direction):
        if direction == 'clockwise':
            self.faces[face] = np.rot90(self.faces[face], -1)
        elif direction == 'counterclockwise':
            self.faces[face] = np.rot90(self.faces[face], 1)

    def change_axis(self, axis, direction):
        self.rotate_slice(axis, 0, direction)
        self.rotate_slice(axis, 1, direction)
        if axis == "z":
            self.rotate_slice(axis, 2, 'clockwise' if direction == 'counterclockwise' else 'counterclockwise')
        else:
            self.rotate_slice(axis, 2, direction)
    
    def rotate_slice(self, axis, slice_index, direction):
        """
        General function to rotate a slice of the cube.
        
        :param axis: Axis of rotation ('x', 'y', or 'z')
        :param slice_index: Index of the slice to rotate (0, 1, or 2)
        :param direction: Direction of rotation ('clockwise' or 'counterclockwise')
        """
        if axis == 'x':
            self.__rotate_x_slice(slice_index, direction)
        elif axis == 'y':
            self.__rotate_y_slice(slice_index, direction)
        elif axis == 'z':
            self.__rotate_z_slice(slice_index, direction)

    def __rotate_x_slice(self, slice_index, direction):
        if direction == 'clockwise':
            temp = self.faces['F'][slice_index, :].copy()
            self.faces['F'][slice_index, :] = self.faces['R'][slice_index, :]
            self.faces['R'][slice_index, :] = self.faces['B'][slice_index, :]
            self.faces['B'][slice_index, :] = self.faces['L'][slice_index, :]
            self.faces['L'][slice_index, :] = temp
        else:  # counterclockwise
            temp = self.faces['F'][slice_index, :].copy()
            self.faces['F'][slice_index, :] = self.faces['L'][slice_index, :]
            self.faces['L'][slice_index, :] = self.faces['B'][slice_index, :]
            self.faces['B'][slice_index, :] = self.faces['R'][slice_index, :]
            self.faces['R'][slice_index, :] = temp

    def __rotate_y_slice(self, slice_index, direction):
        if direction == 'clockwise':
            temp = self.faces['U'][:, slice_index].copy()
            self.faces['U'][:, slice_index] = self.faces['F'][:, slice_index]
            self.faces['F'][:, slice_index] = self.faces['D'][:, slice_index]
            self.faces['D'][:, slice_index] = self.faces['B'][:, 2 - slice_index][::-1]
            self.faces['B'][:, 2 - slice_index] = temp[::-1]
        else:  # counterclockwise
            temp = self.faces['U'][:, slice_index].copy()
            self.faces['U'][:, slice_index] = self.faces['B'][:, 2 - slice_index][::-1]
            self.faces['B'][:, 2 - slice_index] = self.faces['D'][:, slice_index][::-1]
            self.faces['D'][:, slice_index] = self.faces['F'][:, slice_index]
            self.faces['F'][:, slice_index] = temp

    def __rotate_z_slice(self, slice_index, direction):
        if direction == 'clockwise':
            if slice_index == 0:
                temp = self.faces['U'][2, :].copy()
                self.faces['U'][2, :] = self.faces['L'][:, 2][::-1]
                self.faces['L'][:, 2] = self.faces['D'][0, :][::-1]
                self.faces['D'][0, :] = self.faces['R'][:, 0]
                self.faces['R'][:, 0] = temp[::-1]
            elif slice_index == 1:
                temp = self.faces['U'][1, :].copy()
                self.faces['U'][1, :] = self.faces['L'][:, 1][::-1]
                self.faces['L'][:, 1] = self.faces['D'][1, :]
                self.faces['D'][1, :] = self.faces['R'][:, 1][::-1]
                self.faces['R'][:, 1] = temp
            else:  # slice_index == 2
                temp = self.faces['U'][0, :].copy()
                self.faces['U'][0, :] = self.faces['R'][:, 2]
                self.faces['R'][:, 2] = self.faces['D'][2, :][::-1]
                self.faces['D'][2, :] = self.faces['L'][:, 0][::-1]
                self.faces['L'][:, 0] = temp
        else:  # counterclockwise
            if slice_index == 0:
                temp = self.faces['U'][2, :].copy()
                self.faces['U'][2, :] = self.faces['R'][:, 0][::-1]
                self.faces['R'][:, 0] = self.faces['D'][0, :][::-1]
                self.faces['D'][0, :] = self.faces['L'][:, 2]
                self.faces['L'][:, 2] = temp[::-1]
            elif slice_index == 1:
                temp = self.faces['U'][1, :].copy()
                self.faces['U'][1, :] = self.faces['R'][:, 1]
                self.faces['R'][:, 1] = self.faces['D'][1, :][::-1]
                self.faces['D'][1, :] = self.faces['L'][:, 1]
                self.faces['L'][:, 1] = temp[::-1]
            else:  # slice_index == 2
                temp = self.faces['U'][0, :].copy()
                self.faces['U'][0, :] = self.faces['L'][:, 0][::-1]
                self.faces['L'][:, 0] = self.faces['D'][2, :]
                self.faces['D'][2, :] = self.faces['R'][:, 2]
                self.faces['R'][:, 2] = temp
#############################################################

# Pattern creation ##########################################    

    def make_checkerboard(self):
        self.faces['U'] = np.array([['Y', 'W', 'Y'],
                                    ['W', 'Y', 'W'],
                                    ['Y', 'W', 'Y']])
        self.faces['D'] = np.array([['W', 'Y', 'W'],
                                    ['Y', 'W', 'Y'],
                                    ['W', 'Y', 'W']])
        self.faces['F'] = np.array([['G', 'B', 'G'],
                                    ['B', 'G', 'B'],
                                    ['G', 'B', 'G']])
        self.faces['B'] = np.array([['B', 'G', 'B'],
                                    ['G', 'B', 'G'],
                                    ['B', 'G', 'B']])
        self.faces['L'] = np.array([['R', 'O', 'R'],
                                    ['O', 'R', 'O'],
                                    ['R', 'O', 'R']])
        self.faces['R'] = np.array([['O', 'R', 'O'],
                                    ['R', 'O', 'R'],
                                    ['O', 'R', 'O']])
        
    def make_giftbox(self):
        self.faces['U'] = np.array([['W', 'Y', 'W'],
                                    ['Y', 'Y', 'Y'],
                                    ['W', 'Y', 'W']])
        self.faces['D'] = np.array([['Y', 'W', 'Y'],
                                    ['W', 'W', 'W'],
                                    ['Y', 'W', 'Y']])
        self.faces['F'] = np.array([['O', 'G', 'R'],
                                    ['O', 'G', 'R'],
                                    ['O', 'G', 'R']])
        self.faces['B'] = np.array([['R', 'B', 'O'],
                                    ['R', 'B', 'O'],
                                    ['R', 'B', 'O']])
        self.faces['L'] = np.array([['G', 'R', 'B'],
                                    ['G', 'R', 'B'],
                                    ['G', 'R', 'B']])
        self.faces['R'] = np.array([['B', 'O', 'G'],
                                    ['B', 'O', 'G'],
                                    ['B', 'O', 'G']])
        
    def make_minority_cross(self):
        self.faces['U'] = np.array([['G', 'O', 'G'],
                                    ['W', 'Y', 'B'],
                                    ['G', 'R', 'G']])
        self.faces['D'] = np.array([['B', 'O', 'B'],
                                    ['Y', 'W', 'R'],
                                    ['B', 'G', 'B']])
        self.faces['F'] = np.array([['Y', 'B', 'Y'],
                                    ['R', 'G', 'O'],
                                    ['Y', 'W', 'Y']])
        self.faces['B'] = np.array([['W', 'G', 'W'],
                                    ['O', 'B', 'R'],
                                    ['W', 'Y', 'W']])
        self.faces['L'] = np.array([['O', 'G', 'O'],
                                    ['W', 'R', 'Y'],
                                    ['O', 'B', 'O']])
        self.faces['R'] = np.array([['R', 'W', 'R'],
                                    ['B', 'O', 'Y'],
                                    ['R', 'G', 'R']])
    
    def make_solved(self):
        self.faces['U'] = np.array([['Y', 'Y', 'Y'],
                                    ['Y', 'Y', 'Y'],
                                    ['Y', 'Y', 'Y']])
        self.faces['D'] = np.array([['W', 'W', 'W'],
                                    ['W', 'W', 'W'],
                                    ['W', 'W', 'W']])
        self.faces['F'] = np.array([['G', 'G', 'G'],
                                    ['G', 'G', 'G'],
                                    ['G', 'G', 'G']])
        self.faces['B'] = np.array([['B', 'B', 'B'],
                                    ['B', 'B', 'B'],
                                    ['B', 'B', 'B']])
        self.faces['L'] = np.array([['R', 'R', 'R'],
                                    ['R', 'R', 'R'],
                                    ['R', 'R', 'R']])
        self.faces['R'] = np.array([['O', 'O', 'O'],
                                    ['O', 'O', 'O'],
                                    ['O', 'O', 'O']])
#############################################################

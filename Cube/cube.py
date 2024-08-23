from ast import If
import numpy as np

class Cube:
    def __init__(self):
        self.faces = {
            'U': np.full((3, 3), 'Y'),
            'D': np.full((3, 3), 'W'),
            'F': np.full((3, 3), 'G'),
            'B': np.full((3, 3), 'B'),
            'L': np.full((3, 3), 'R'),
            'R': np.full((3, 3), 'O')
        }

    def rotate_face_clockwise(self, face):
        self.faces[face] = np.rot90(self.faces[face], -1)

    def rotate_face_counterclockwise(self, face):
        self.faces[face] = np.rot90(self.faces[face], 1)
    
    def rotate_slice(self, axis, slice_index, direction):
        """
        General function to rotate a slice of the cube.
        
        :param axis: Axis of rotation ('x', 'y', or 'z')
        :param slice_index: Index of the slice to rotate (0, 1, or 2)
        :param direction: Direction of rotation ('clockwise' or 'counterclockwise')
        """
        if axis == 'x':
            self.__rotate_x(slice_index, direction)
        elif axis == 'y':
            self.__rotate_y(slice_index, direction)
        elif axis == 'z':
            self.__rotate_z(slice_index, direction)

    def __rotate_x(self, slice_index, direction):
        if direction == 'clockwise':
            temp = self.faces['U'][slice_index, :].copy()
            self.faces['U'][slice_index, :] = self.faces['R'][slice_index, :]
            self.faces['R'][slice_index, :] = self.faces['D'][slice_index, :]
            self.faces['D'][slice_index, :] = self.faces['L'][slice_index, :]
            self.faces['L'][slice_index, :] = temp
        else:  # counterclockwise
            temp = self.faces['U'][slice_index, :].copy()
            self.faces['U'][slice_index, :] = self.faces['L'][slice_index, :]
            self.faces['L'][slice_index, :] = self.faces['D'][slice_index, :]
            self.faces['D'][slice_index, :] = self.faces['R'][slice_index, :]
            self.faces['R'][slice_index, :] = temp

    def __rotate_y(self, slice_index, direction):
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

    def __rotate_z(self, slice_index, direction):
        if direction == 'clockwise':
            if slice_index == 0:
                temp = self.faces['U'][2, :].copy()
                self.faces['U'][2, :] = self.faces['L'][:, 2][::-1]
                self.faces['L'][:, 2] = self.faces['D'][0, :][::-1]
                self.faces['D'][0, :] = self.faces['R'][:, 0]
                self.faces['R'][:, 0] = temp[::-1]
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
            else:  # slice_index == 2
                temp = self.faces['U'][0, :].copy()
                self.faces['U'][0, :] = self.faces['L'][:, 0][::-1]
                self.faces['L'][:, 0] = self.faces['D'][2, :]
                self.faces['D'][2, :] = self.faces['R'][:, 2]
                self.faces['R'][:, 2] = temp
            
        

    def make_checkerboard(self):
        self.faces['U'] = np.array([['Y', 'W', 'Y'],
                                    ['W', 'Y', 'W'],
                                    ['Y', 'W', 'Y']])
        self.faces['D'] = np.array([['W', 'Y', 'W'],
                                    ['Y', 'W', 'Y'],
                                    ['W', 'Y', 'W']])
        self.faces['F'] =  np.array([['G', 'B', 'G'],
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
        self.faces['F'] =  np.array([['O', 'G', 'R'],
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

    def is_solved(self):
        return all(np.all(face == face[0, 0]) for face in self.faces.values())

    def __str__(self):
        cube_str = ''
        for face, grid in self.faces.items():
            cube_str += f"{face} face:\n{grid}\n\n"
        return cube_str

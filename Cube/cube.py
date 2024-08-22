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

    def rotate_slice(self, slice_index, axis, direction):
        pass  # TODO: Implement rotation logic here

    def apply_move(self, move):
        if move == 'R':
            self.rotate_face_clockwise('R')
            # TODO: Implement adjacent updates
        elif move == 'R\'':
            self.rotate_face_counterclockwise('R')
            # Implement adjacent updates
        # TODO: Add other moves (L, U, D, F, B)

    def is_solved(self):
        return all(np.all(face == face[0, 0]) for face in self.faces.values())

    def __str__(self):
        cube_str = ''
        for face, grid in self.faces.items():
            cube_str += f"{face} face:\n{grid}\n\n"
        return cube_str

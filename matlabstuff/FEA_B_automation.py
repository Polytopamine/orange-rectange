# aims to automate some sections of the FEA B exercises that wil likely be in the exam


import numpy as np
import math
from fractions import Fraction
from sympy import *

init_printing()

# -- Find principal stresses and directions


T_ij = Matrix([[21, 0, 0],
               [0, 14, 14],
               [0, 14, 35]])
print("T_ij:")
pprint(T_ij)

a = 1 / 2
b = math.sqrt(3) / 2
Q_ij = Matrix([[a, b, 0],
               [-b, a, 0],
               [0, 0, 1]])

print("Q_ij:")
pprint(Q_ij)

pprint(T_ij.eigenvals())
pprint(T_ij.eigenvects())
pprint(T_ij.eigenvects()[0])


def rotate_coordinate_system(original_tensor, rotation_tensor):
    """ returns the original tensor within a new coordinate system
     that has been rotated by the rotation tensor"""

    print(f"Q_ij * T_ij:")
    pprint(Q_ij * T_ij)
    print("result:")
    pprint(Q_ij * T_ij * Q_ij.T)
    new_tensor = Q_ij * T_ij * Q_ij.T

    return new_tensor  # new_tensor

# rotate_coordinate_system(T_ij, Q_ij)

# pprint(rotate_coordinate_system(T_ij, Q_ij))





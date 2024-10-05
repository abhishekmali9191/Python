from scipy.linalg import inv, det
import numpy as np

#define a matrix
matrix = np.array([[1,2],[3,4]])

#compute the determinant of the matrix
matrix_det = det(matrix)
print(matrix_det)

#compute the inverse of the matrix
matrix_inv = inv(matrix)
print(matrix_inv)


# ######################################
# Output
# -2.0
# [[-2.   1. ]
#  [ 1.5 -0.5]]
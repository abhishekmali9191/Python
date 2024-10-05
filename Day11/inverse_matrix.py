#Assignment 1 finding the inverse of matrix

from scipy.linalg import inv
import numpy as np

matrix = np.array([[4,7],[2,6]])
print(matrix)
matrix_inv = inv(matrix)
print(matrix_inv)


# ################################
# OUTPUT
# [[4 7]
#  [2 6]]
# [[ 0.6 -0.7]
#  [-0.2  0.4]]
# Assignment 10 Matrix multiplication and transpose

matrix1 = np.array([[1,2],[3,4],[5,6],[7,8]])
matrix2 = np.array([[3,4,2],[7,5,2]])
print(matrix1)
print(matrix2)

multi_matrix = np.matmul(matrix1,matrix2)
print(multi_matrix)
print(multi_matrix.T)

###########################################
# OUTPUT
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
# [[3 4 2]
#  [7 5 2]]
# [[17 14  6]
#  [37 32 14]
#  [57 50 22]
#  [77 68 30]]
# [[17 37 57 77]
#  [14 32 50 68]
#  [ 6 14 22 30]]
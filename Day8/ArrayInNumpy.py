array_1D = np.array([1,2,3,4])
print(array_1D)
print(array_1D.ndim)
print(array_1D.shape)
print(array_1D.size)
print(array_1D.dtype)

array_2D = np.array([[1,2,3],[4,5,6]])
print(array_2D)
print(array_2D.ndim)
print(array_2D.shape)
print(array_2D.size)
print(array_2D.dtype)

array_3D = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[3,2,1]]])
print(array_3D)
print(array_3D.ndim)
print(array_3D.shape)
print(array_3D.size)
print(array_3D.dtype)

################################################################
# OUTPUT
# [1 2 3 4]
# 1
# (4,)
# 4
# int64
# [[1 2 3]
#  [4 5 6]]
# 2
# (2, 3)
# 6
# int64
# [[[1 2 3]
#   [4 5 6]]

#  [[7 8 9]
#   [3 2 1]]]
# 3
# (2, 2, 3)
# 12
# int64
array_1D = np.arange(10)
print("1D Array : ", array_1D)

print("3rd ele : ", array_1D[2])
print("4th ele : ", array_1D[3])
print("last ele : ", array_1D[-1])
print("2nd last ele : ", array_1D[-2])# second last ele
print("3rd last ele : ", array_1D[-3])

print("first 5 ele : ", array_1D[:5]) # ele from start to index 4
print("every 2nd ele : ", array_1D[::2])  # every 2nd ele
print("Array revesed  : ", array_1D[::-1])

array_2d = np.arange(10,22).reshape(3,4)
print("2 d array : ", array_2d)

# accessing entire rows and columns
print("Enitre 1st row : ", array_2d[0, :]) # first row)
print("Entire 2nd column : ", array_2d[:,1])  # second column

# Slicing to extract a subarray
subarray = array_2d[:2, -2:] # first 2 row and last 2 col
print("Subarray (first 2 rows, last 2 col): ", subarray)

# Extracting every other element
sliced_array = array_1D[::2] # Every other element along rows and col
print("Sliced array (every other element): ", sliced_array)


# Extracting every other element along rows and columns
sliced_array = array_2d[::2, ::2]  # Every other element along rows and columns
print("Every Other Element of 2D Array:\n", sliced_array)

# Create a 3D array
array_3d = np.random.randint(1, 21, (2, 3, 4))
print("3D Array:\n", array_3d)

# Access a specific element
print("Element in 1st Matrix, 2nd Row, 3rd Column:", array_3d[0, 1, 2])

# Access the entire 2nd "matrix"
print("Entire 2nd Matrix:\n", array_3d[1, :, :])

# Extract a subarray
subarray_3d = array_3d[:, :2, :3]  # All matrices, first 2 rows, first 3 columns
print("Subarray (First 2 Rows, First 3 Columns of All Matrices):\n", subarray_3d)


################################################################################
# OUTPUT
# 1D Array :  [0 1 2 3 4 5 6 7 8 9]
# 3rd ele :  2
# 4th ele :  3
# last ele :  9
# 2nd last ele :  8
# 3rd last ele :  7
# first 5 ele :  [0 1 2 3 4]
# every 2nd ele :  [0 2 4 6 8]
# Array revesed  :  [9 8 7 6 5 4 3 2 1 0]
# 2 d array :  [[10 11 12 13]
#  [14 15 16 17]
#  [18 19 20 21]]
# Enitre 1st row :  [10 11 12 13]
# Entire 2nd column :  [14 15 16 17]
# Subarray (first 2 rows, last 2 col):  [[12 13]
#  [16 17]]
# Sliced array (every other element):  [0 2 4 6 8]
# Every Other Element of 2D Array:
#  [[10 12]
#  [18 20]]
# 3D Array:
#  [[[13  2  9 12]
#   [16 12 12 19]
#   [20  3  2 16]]

#  [[ 1  7  2  4]
#   [ 7 19  6 17]
#   [11 15 17  7]]]
# Element in 1st Matrix, 2nd Row, 3rd Column: 12
# Entire 2nd Matrix:
#  [[ 1  7  2  4]
#  [ 7 19  6 17]
#  [11 15 17  7]]
# Subarray (First 2 Rows, First 3 Columns of All Matrices):
#  [[[13  2  9]
#   [16 12 12]]

#  [[ 1  7  2]
#   [ 7 19  6]]]
#Assignment 1 1D array with 20 elements
array = np.arange(0,20)
print(array)
print("reshaped array to 4X5\n",array.reshape(4,5))
array1 = np.random.randint(1, 10, size=(3,3))
print("random array 3X3\n",array1)
print("Transpose of array1 is : \n", np.transpose(array1))



################################################################
# OUTPUT
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
# reshaped array to 4X5
#  [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]]
# random array 3X3
#  [[3 7 2]
#  [5 6 1]
#  [7 4 3]]
# Transpose of array1 is : 
#  [[3 5 7]
#  [7 6 4]
#  [2 1 3]]
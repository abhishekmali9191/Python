import numpy as np

#1D Array
OneD_array = np.array([1,2,3,4])
print("One D Array : ",OneD_array)

#2D Array
twoD_Array = np.array([[1,2],[3,4]])
print("2D array : ",twoD_Array)

#3D Array
threeD_array = np.array([[1,2,3],[4,5,6],[7,8,9],[4,3,2]])
print("3D array : ",threeD_array)

# array of Zeros
zero_Array = np.zeros((3,4))  # (rows, columns)
print("Zero Array : ",zero_Array)

#array of ones
ones_array = np.ones((2,3))
print("Ones array : ", ones_array)

#2X2 array filled with the value 7
full_array = np.full((2,2),7)
print("Array filled with 7 : ", full_array)

# array with value from 0 to 9
range_array =  np.arange(0,10)
print("Array with range : \n ",range_array)

#array with specific step size
step_array = np.arange(0,10,2)
print("Array with step Size: \n", step_array)

#Array with linearly spaced values
linspace_array = np.linspace(0,1, 10 )  # 5 value from 0 to 1
print("Array with linear spaced value :\n ", linspace_array)

#2X2 with random integer between 1 and 10
random_int_array = np.random.randint(1, 10, size=(2,2))
print("Array with random Integers : \n ", random_int_array)

# 3X3 identity matrix
identity_matrix = np.eye(3)
print("Identity matrix : \n ", identity_matrix)

#diagonal matrix with specified diagonal values
diag_matrix = np.diag([1,2,3])
print("Diagonal Matrix : \n ", diag_matrix)

#reshaping array to 2X3
array = np.array([1,2,3,4,5,6])
reshaped_array = array.reshape((2,3))
print("Reshaped array : ", reshaped_array)

#empty 1D array of size 5
empty_id = np.empty(5)
print("1D empty array : ", empty_id)

#2X3 empty array
empty_2D = np.empty((2,3))
print("2D empty array ",empty_2D)

#3X3X2 empty array
empty_3D = np.empty((3,3,2))
print("3D empty array : \n", empty_3D)




#----------------------------------------------------------------------
# OUTPUT
# One D Array :  [1 2 3 4]
# 2D array :  [[1 2]
#  [3 4]]
# 3D array :  [[1 2 3]
#  [4 5 6]
#  [7 8 9]
#  [4 3 2]]
# Zero Array :  [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]
# Ones array :  [[1. 1. 1.]
#  [1. 1. 1.]]
# Array filled with 7 :  [[7 7]
#  [7 7]]
# Array with range : 
#   [0 1 2 3 4 5 6 7 8 9]
# Array with step Size: 
#  [0 2 4 6 8]
# Array with linear spaced value :
#   [0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556
#  0.66666667 0.77777778 0.88888889 1.        ]
# Array with random Integers : 
#   [[2 1]
#  [2 1]]
# Identity matrix : 
#   [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
# Diagonal Matrix : 
#   [[1 0 0]
#  [0 2 0]
#  [0 0 3]]
# Reshaped array :  [[1 2 3]
#  [4 5 6]]
# 1D empty array :  [1. 1. 1. 1. 1.]
# 2D empty array  [[1. 1. 1.]
#  [1. 1. 1.]]
# 3D empty array : 
#  [[[4.77353666e-310 0.00000000e+000]
#   [6.67800843e-310 6.67794162e-310]
#   [6.67800848e-310 6.67800843e-310]]

#  [[6.67800848e-310 6.67800848e-310]
#   [6.67800848e-310 6.67800846e-310]
#   [6.67800849e-310 6.67800849e-310]]

#  [[6.67800849e-310 6.67800833e-310]
#   [6.67800771e-310 6.67800848e-310]
#   [6.67800849e-310 6.67800846e-310]]]
import numpy as np
array_Int = np.array([10,2,3,4,5,6])
print("Item Size is : ",array_Int.itemsize)
print("memory of array : ",array_Int.nbytes)

array_float = np.array([1.23,2.321,3.34,4.1,5.2])
print("Item Size is : ",array_float.itemsize)
print("memory of array : ",array_float.nbytes)

#######################################################
# OUTPUT
# Item Size is :  8
# memory of array :  48
# Item Size is :  8
# memory of array :  40
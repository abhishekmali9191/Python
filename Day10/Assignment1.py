import pandas as pd
import numpy as np
numbers = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10,11]
num1 = np.array([i for i in numbers[:5]])
num2 = np.array([i for i in numbers[5:10]])
num3 = np.array([i for i in numbers[10:15]])
num4 = np.array([i for i in numbers[15:]])

print(num1, num2, num3, num4)
array1 = np.append(num1, num2)
array2 = np.append(num3, num4)
print(array1, array2)

print(array1 + array2)
print(array1 * array2)
print(array1 - array2)
print(array1 ** array2)
print(np.exp(array1))

##########################################################
# OUTPUT
# [1 2 3 4 5] [6 7 8 9 1] [2 3 4 5 6] [ 7  8  9 10 11]
# [1 2 3 4 5 6 7 8 9 1] [ 2  3  4  5  6  7  8  9 10 11]
# [ 3  5  7  9 11 13 15 17 19 12]
# [ 2  6 12 20 30 42 56 72 90 11]
# [ -1  -1  -1  -1  -1  -1  -1  -1  -1 -10]
# [         1          8         81       1024      15625     279936
#     5764801  134217728 3486784401          1]
# [2.71828183e+00 7.38905610e+00 2.00855369e+01 5.45981500e+01
#  1.48413159e+02 4.03428793e+02 1.09663316e+03 2.98095799e+03
#  8.10308393e+03 2.71828183e+00]
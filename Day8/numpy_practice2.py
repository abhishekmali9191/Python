import numpy as np

# 1. Create arrays with different data types: integers, floats, booleans
int_array = np.array([1, 2, 3, 4], dtype=np.int32)
float_array = np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float32)
bool_array = np.array([True, False, True, False], dtype=np.bool_)

# 2. Compare their itemsize and nbytes to understand memory requirements
print("Integer array:")
print("Item size (bytes):", int_array.itemsize)
print("Total memory (nbytes):", int_array.nbytes)

print("\nFloat array:")
print("Item size (bytes):", float_array.itemsize)
print("Total memory (nbytes):", float_array.nbytes)

print("\nBoolean array:")
print("Item size (bytes):", bool_array.itemsize)
print("Total memory (nbytes):", bool_array.nbytes)

# 3. Change the dtype of an existing array from int to float and verify changes
converted_array = int_array.astype(np.float32)

print("\nConverted integer array to float:")
print("Item size (bytes):", converted_array.itemsize)
print("Total memory (nbytes):", converted_array.nbytes)

###########################################################################
# OUTPUT
# Integer array:
# Item size (bytes): 4
# Total memory (nbytes): 16

# Float array:
# Item size (bytes): 4
# Total memory (nbytes): 16

# Boolean array:
# Item size (bytes): 1
# Total memory (nbytes): 4

# Converted integer array to float:
# Item size (bytes): 4
# Total memory (nbytes): 16
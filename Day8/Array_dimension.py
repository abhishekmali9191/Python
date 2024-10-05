#Assignment array dimension and shape

def describe_array(arr):
    print("Dimension of array : ", arr.ndim)
    print("shape of array : ", arr.shape)
    print("size of array : ",arr.size)
    print("type of array : ", arr.dtype)

array = np.array([[1,2,3],[4,5,6]])
describe_array(array)

###############################################
# OUTPUT
# Dimension of array :  2
# shape of array :  (2, 3)
# size of array :  6
# type of array :  int64
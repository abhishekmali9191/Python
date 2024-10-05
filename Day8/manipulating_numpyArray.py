#Assignment Manipulating 2D array of shape (5,5) filled with random int between 50 t 100, replace the central 3x3 subarray with zeros

a = np.random.randint(50,100,size=(5,5))
print(a)
# b=np.zeros(3)
# print(b)
a[1:4,1:4]=0
print(a)

############################################################
# OUTPUT
# [[73 82 74 90 69]
#  [54 97 58 68 68]
#  [72 87 71 83 93]
#  [51 63 79 89 88]
#  [63 98 50 59 92]]
# [[73 82 74 90 69]
#  [54  0  0  0 68]
#  [72  0  0  0 93]
#  [51  0  0  0 88]
#  [63 98 50 59 92]]
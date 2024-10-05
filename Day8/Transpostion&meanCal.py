#Assignmet 7 Transposition and mean calculation
a = np.random.randint(10,100, size=(5,3))
print(a)
aTransposed = a.T
print(aTransposed)
print(a.mean())
print(aTransposed.mean())


######################################################################
# OUTPUT
# [[72 10 84]
#  [80 89 42]
#  [93 24 90]
#  [21 40 19]
#  [56 96 63]]
# [[72 80 93 21 56]
#  [10 89 24 40 96]
#  [84 42 90 19 63]]
# 58.6
# 58.6
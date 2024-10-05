# creating a series
data = pd.Series([10,20,20,20,30,40,40])
#ranking with different methods
print("Average rank :")
print(data.rank(method = 'average'))
print("\nMin Rank")
print(data.rank(method = 'min'))
print("\n Max Rank")
print(data.rank(method = 'max'))
print("\n First Rank : ")
print(data.rank(method='first'))
print("\n last rank ")
print(data.rank(method='dense'))

####################################################
# OUTPUT
# Average rank :
# 0    1.0
# 1    3.0
# 2    3.0
# 3    3.0
# 4    5.0
# 5    6.5
# 6    6.5
# dtype: float64

# Min Rank
# 0    1.0
# 1    2.0
# 2    2.0
# 3    2.0
# 4    5.0
# 5    6.0
# 6    6.0
# dtype: float64

#  Max Rank
# 0    1.0
# 1    4.0
# 2    4.0
# 3    4.0
# 4    5.0
# 5    7.0
# 6    7.0
# dtype: float64

#  First Rank : 
# 0    1.0
# 1    2.0
# 2    3.0
# 3    4.0
# 4    5.0
# 5    6.0
# 6    7.0
# dtype: float64

#  last rank 
# 0    1.0
# 1    2.0
# 2    2.0
# 3    2.0
# 4    3.0
# 5    4.0
# 6    4.0
# dtype: float64
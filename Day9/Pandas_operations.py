import pandas as pd
#creating a series from a list
data = [10,20,30,40,50]
series = pd.Series(data)
print(series)
#sum of all elements
print("Sum of series : ",series.sum())
#filtering values greater than 20
print("greater than 20 \n",series[series>20])
#creating a series with custom index
series = pd.Series(data, index=['a','b','c','d','e'])
print("Series with Custom index  :\n",series)
#creating a series form dictionary
data_dict = {'apple':3,'banana':2,'orange':4}
series = pd.Series(data_dict)
print("Dictionary series ", series)
#creating a series from a scalar value
series = pd.Series(10, index=['a','b','c'])        # here we can pass multiple values to a,b,c by passing a list like [10,20,30]
print("Scalar series : ",series)
#accessing element by index
print("element by index a : ",series['a'])
#slicing series
print("slicing of series : ",series['a':'c'])
#accessing element by position
print(series[1])



#########################################################
# OUTPUT

# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64
# Sum of series :  150
# greater than 20 
#  2    30
# 3    40
# 4    50
# dtype: int64
# Series with Custom index  :
#  a    10
# b    20
# c    30
# d    40
# e    50
# dtype: int64
# Dictionary series  apple     3
# banana    2
# orange    4
# dtype: int64
# Scalar series :  a    10
# b    30
# c    50
# dtype: int64
# element by index a :  10
# slicing of series :  a    10
# b    30
# c    50
# dtype: int64
# 30
# <ipython-input-12-766d49a088c4>:25: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
#   print(series[1])
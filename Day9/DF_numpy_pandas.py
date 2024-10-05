import numpy as np
import pandas as pd
#creating a dataframe from a dictionary

data = {'Name':['Alice','Bob','Charlie','David'],
        'Age':[25,30,22,28],
        'City':['New York','San Francisco','Los Angeles','Chicago']}
df = pd.DataFrame(data)
print(df)
#creating a dataframe from a list of dictionary
data = [
    {'Name':'Alice','Age':25,'City':'New York'},
    {'Name':'Bob','Age':30,'City':'San Francisco'},
    {'Name':'Charlie','Age':2,'City':'Los Angeles'}
]
df = pd.DataFrame(data)
print(df)
# ----------
names = ['Alice','Bob','Charlie','David']
ages = [25,30,22,28]
cities = ['New York','San Francisco','Los Angeles','Chicago']
df = pd.DataFrame(
    {'Name':names,
    'Age':ages,
    'City':cities}
    )
print(df)

#creating a dataframe from a numpy array
array = np.array([[25,'New York'],[30,'San Francisco'],[22,'Los Angeles']])
print(array, array.dtype, array.itemsize, array.nbytes, array.ndim)
df = pd.DataFrame(array,columns=['Age','City'])
print(df)

# # reading a dataframe from a csv file
# df = pd.read_csv('data.csv')
# print(df)

#creating a dataframe from series
names = pd.Series(['Alice','Bob','Charlie','David'], name = 'Name')
ages = pd.Series([25,30,22,28], name = 'Age')
df = pd.concat([names,ages],axis=1)
print(df)

#sample dataframe
data = {
    'Name':['Alice','Bob','Charlie','David'],
    'Age':[25,30,22,28],
    'City':['New York','San Francisco','Los Angeles','Chicago'],
    'Marks':[85,92,78,95]
}
df = pd.DataFrame(data)


###################################################################
# OUTPUT
#       Name  Age           City
# 0    Alice   25       New York
# 1      Bob   30  San Francisco
# 2  Charlie   22    Los Angeles
# 3    David   28        Chicago
#       Name  Age           City
# 0    Alice   25       New York
# 1      Bob   30  San Francisco
# 2  Charlie    2    Los Angeles
#       Name  Age           City
# 0    Alice   25       New York
# 1      Bob   30  San Francisco
# 2  Charlie   22    Los Angeles
# 3    David   28        Chicago
# [['25' 'New York']
#  ['30' 'San Francisco']
#  ['22' 'Los Angeles']] <U21 84 504 2
#   Age           City
# 0  25       New York
# 1  30  San Francisco
# 2  22    Los Angeles
#       Name  Age
# 0    Alice   25
# 1      Bob   30
# 2  Charlie   22
# 3    David   28
# Assignmnet 2 creating a dataframe with student data
data = {
    'roll no':[1,2,3,4,5],
    'name':['Alice','Bob','Charlie','David','Eve'],
    'class':[10,10,10,11,12],
    'marks':[85,45,78,97,92]
}

df = pd.DataFrame(data)
df.to_csv('student.csv', index= False)

df1 = pd.read_csv('student.csv')
print("Head of dataframe : \n",df1.head())
print("\nTail of data frame \n",df1.tail())
print("\n Info of dataframe \n",df1.info())
print("\n Describe the dataframe \n",df1.describe())

##############################################################
# OUTPUT
# Head of dataframe : 
#     roll no     name  class  marks
# 0        1    Alice     10     85
# 1        2      Bob     10     45
# 2        3  Charlie     10     78
# 3        4    David     11     97
# 4        5      Eve     12     92

# Tail of data frame 
#     roll no     name  class  marks
# 0        1    Alice     10     85
# 1        2      Bob     10     45
# 2        3  Charlie     10     78
# 3        4    David     11     97
# 4        5      Eve     12     92
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 4 columns):
#  #   Column   Non-Null Count  Dtype 
# ---  ------   --------------  ----- 
#  0   roll no  5 non-null      int64 
#  1   name     5 non-null      object
#  2   class    5 non-null      int64 
#  3   marks    5 non-null      int64 
# dtypes: int64(3), object(1)
# memory usage: 288.0+ bytes

#  Info of dataframe 
#  None

#  Describe the dataframe 
#          roll no      class      marks
# count  5.000000   5.000000   5.000000
# mean   3.000000  10.600000  79.400000
# std    1.581139   0.894427  20.525594
# min    1.000000  10.000000  45.000000
# 25%    2.000000  10.000000  78.000000
# 50%    3.000000  10.000000  85.000000
# 75%    4.000000  11.000000  92.000000
# max    5.000000  12.000000  97.000000
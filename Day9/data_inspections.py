# Assignmnet 3 Inspection of data set
data = {
    'roll no':[1,2,13,4,5,6,7,8,9],
    'name':['Alice','Bob','Charlie','David','Eve','Abhishek','jayesh','Sammak','Harish'],
    'class':[10,10,10,11,12,12,10,11,12],
    'marks':[85,45,78,97,92,87,98,45,96]
}

df = pd.DataFrame(data)
df.to_csv('student1.csv', index= False)
dataf = pd.read_csv('student1.csv')
print("First 5 row : ",dataf.head())
print("Specific colunms : ", dataf[['name','marks']])
print(dataf.loc[(dataf['class']==10) & (dataf['marks']>75)])
print("First 5 rows and 3 columns :\n ",dataf.iloc[0:5,[1,2,3]])
print("rows from 5 to 9 and column are name marks: ",dataf.loc[4:8,['name','marks']])

#######################################################################################
# OUTPUT
# First 5 row :     roll no     name  class  marks
# 0        1    Alice     10     85
# 1        2      Bob     10     45
# 2       13  Charlie     10     78
# 3        4    David     11     97
# 4        5      Eve     12     92
# Specific colunms :         name  marks
# 0     Alice     85
# 1       Bob     45
# 2   Charlie     78
# 3     David     97
# 4       Eve     92
# 5  Abhishek     87
# 6    jayesh     98
# 7    Sammak     45
# 8    Harish     96
#    roll no     name  class  marks
# 0        1    Alice     10     85
# 2       13  Charlie     10     78
# 6        7   jayesh     10     98
# First 5 rows and 3 columns :
#         name  class  marks
# 0    Alice     10     85
# 1      Bob     10     45
# 2  Charlie     10     78
# 3    David     11     97
# 4      Eve     12     92
# rows from 5 to 9 and column are name marks:         name  marks
# 4       Eve     92
# 5  Abhishek     87
# 6    jayesh     98
# 7    Sammak     45
# 8    Harish     96
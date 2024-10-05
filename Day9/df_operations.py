data = {
    'Name':['Alice','Bob','Charlie','David','Eve'],
    'Age':[25,30,35,40,22],
    'city':['abc','ABC','def','EFf','fasj'],
    'Score':[87,67,89,92,90]
}
df = pd.DataFrame(data)
print(df)
#selecting single column
print(df['Name'])
#multiple column
print(df[['Name','Score']])
#rows by inde position
print(df.iloc[0])
#selecting first 3 roe
print(df.iloc[:3])
#specific row and colunm
print(df.iloc[1:4,[0,2]])
#row by index lab
print(df.loc[2])
#column where age > 30
print(df.loc[df['Age']>30])
#column where marks >80
print(df.loc[df['Score']>80])
#colunm where city is either from below one
print(df['city'].isin(['def','EFf']))

#################################################
# OUTPUT
#       Name  Age  city  Score
# 0    Alice   25   abc     87
# 1      Bob   30   ABC     67
# 2  Charlie   35   def     89
# 3    David   40   EFf     92
# 4      Eve   22  fasj     90
# 0      Alice
# 1        Bob
# 2    Charlie
# 3      David
# 4        Eve
# Name: Name, dtype: object
#       Name  Score
# 0    Alice     87
# 1      Bob     67
# 2  Charlie     89
# 3    David     92
# 4      Eve     90
# Name     Alice
# Age         25
# city       abc
# Score       87
# Name: 0, dtype: object
#       Name  Age city  Score
# 0    Alice   25  abc     87
# 1      Bob   30  ABC     67
# 2  Charlie   35  def     89
#       Name city
# 1      Bob  ABC
# 2  Charlie  def
# 3    David  EFf
# Name     Charlie
# Age           35
# city         def
# Score         89
# Name: 2, dtype: object
#       Name  Age city  Score
# 2  Charlie   35  def     89
# 3    David   40  EFf     92
#       Name  Age  city  Score
# 0    Alice   25   abc     87
# 2  Charlie   35   def     89
# 3    David   40   EFf     92
# 4      Eve   22  fasj     90
# 0    False
# 1    False
# 2     True
# 3     True
# 4    False
# Name: city, dtype: bool
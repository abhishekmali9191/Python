data = {'Name':['Alice','Bob','Charlie','David'],
        'Age':[25,30,22,28],
        'City':['New York','San Francisco','Los Angeles','Chicago']
        }
df = pd.DataFrame(data)
print(df)
#adding a new column Score with default value
df['Score']=[90,87,98,56]
print("dataframe after adding values\n",df)
#Deleting the city column
df = df.drop('City',axis=1)
print("Dataframe after deleteing City column \n", df)
#sorting by age in ascending order
sorted_By_age = df.sort_values(by = 'Age')
print('\nDataframe sorted by age\n',sorted_By_age)
#renaming  score col to final score col
df= df.rename(columns={'Score':'Final Score'})
print('\n DataFrame after renamingg \n',df)
#creating a dataframe with missing value
data_with_nan= {
    'Name':['Alice','Bob','Charlie','David'],
    'Age':[25,None,35,None],
    'Score':[86,90,None,78]
}
df_nan = pd.DataFrame(data_with_nan)
#filing missing value in age with mean age
df_nan['Age']=df_nan['Age'].fillna(df_nan['Age'].mean())
print('\n Dataframe after filling missing values in Age with mean age \n',df_nan)
#filling missing value in 'Score' with fixed value (e.g 0)
df_nan['Score']=df_nan['Score'].fillna(0)
print('\n Dataframe after filling missing values in Score with 0 \n',df_nan)
#droping rows with any missing value
print("original ", df_nan)
df_dropped = df_nan.dropna()
print('\n Dataframe after dropping rows with missing values \n',df_dropped)
#replacing specific values in the 'name' column
df_nan['Name'] = df_nan['Name'].replace({'Alice':'John'})
print('\n Dataframe after replacing Alice with John \n',df_nan)


# #################################################################################
# OUTPUT
#       Name  Age           City
# 0    Alice   25       New York
# 1      Bob   30  San Francisco
# 2  Charlie   22    Los Angeles
# 3    David   28        Chicago
# dataframe after adding values
#        Name  Age           City  Score
# 0    Alice   25       New York     90
# 1      Bob   30  San Francisco     87
# 2  Charlie   22    Los Angeles     98
# 3    David   28        Chicago     56
# Dataframe after deleteing City column 
#        Name  Age  Score
# 0    Alice   25     90
# 1      Bob   30     87
# 2  Charlie   22     98
# 3    David   28     56

# Dataframe sorted by age
#        Name  Age  Score
# 2  Charlie   22     98
# 0    Alice   25     90
# 3    David   28     56
# 1      Bob   30     87

#  DataFrame after renamingg 
#        Name  Age  Final Score
# 0    Alice   25           90
# 1      Bob   30           87
# 2  Charlie   22           98
# 3    David   28           56

#  Dataframe after filling missing values in Age with mean age 
#        Name   Age  Score
# 0    Alice  25.0   86.0
# 1      Bob  30.0   90.0
# 2  Charlie  35.0    NaN
# 3    David  30.0   78.0

#  Dataframe after filling missing values in Score with 0 
#        Name   Age  Score
# 0    Alice  25.0   86.0
# 1      Bob  30.0   90.0
# 2  Charlie  35.0    0.0
# 3    David  30.0   78.0
# original        Name   Age  Score
# 0    Alice  25.0   86.0
# 1      Bob  30.0   90.0
# 2  Charlie  35.0    0.0
# 3    David  30.0   78.0

#  Dataframe after dropping rows with missing values 
#        Name   Age  Score
# 0    Alice  25.0   86.0
# 1      Bob  30.0   90.0
# 2  Charlie  35.0    0.0
# 3    David  30.0   78.0

#  Dataframe after replacing Alice with John 
#        Name   Age  Score
# 0     John  25.0   86.0
# 1      Bob  30.0   90.0
# 2  Charlie  35.0    0.0
# 3    David  30.0   78.0
import pandas as pd

data = pd.read_csv("C:/Users/diego/JetLearn/Data Science/Lesson 3/Titanic.csv")
print(data.head(886))

#data.loc allows you to get a specific column
adult_names = data.loc[data["Age"] > 18, "Name"]
print(adult_names.shape)

#Slicing -> the same as numpy's 2d slicing
#The first index (section) is for the rows and the second for the columns
#the last number is excluded
print(data.iloc[1:25, 2:5])
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

#changing the names of the passengers

#changes all names in the [] to Diego
data.iloc[0:4, 2] = "Diego"
print(data.iloc[0:4, 2])
#creates a new dataframe, with the modified data
data.to_csv("changed_data.csv")

#creating new columns in the dataframe

#says that the new column, Test, is equal to fare + 10
data["Test"] = data["Fare"] + 10
print(data.head())

#or you can multiply, or other things
data["Money_lost"] = data["Fare"] * data["Pclass"]
print(data.head())

#renaming a column
data_renamed = data.rename(columns = {"Pclass": "Passenger Class"})
print(data_renamed.info())

#printing the mean of a column
print(data["Age"].mean())

#or two or more
print(data[["Age", "Fare"]].mean())

#or you could do multiple different functions

print(data.agg({ # agg stands for aggregate
    "Age": ["min", "max", "median"],
    "Fare": ["min", "max", "median"] # you don't have to do the same for both, you can use different ones
}))

#by classifying the classes by gender using groupby, you can find the mean fare for each gender's class
print(data.groupby(["Sex", "Pclass"])["Fare"].mean())

#the amount of rows in each class

print(data["Pclass"].value_counts())

#sorting columns

#this allows you to sort example, name, by their example, ages
data_sort_ascending = data.sort_values(by = "Age")
print(data_sort_ascending[["Name", "Age"]])

#and this one does it in descending order
data_sort_descending = data.sort_values(by = "Age", ascending = False)
print(data_sort_descending[["Name", "Age"]])

#creating a column 2

#this one replaces male with M and female with F
data["Gender"] = data["Sex"].replace({"male":"M", "female": "F"})
print(data.head())

#this one makes all names lowercase
data["NameLowercase"] = data["Name"].str.lower()
print(data.head())

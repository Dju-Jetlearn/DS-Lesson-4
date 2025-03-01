import pandas as pd

data = pd.read_csv("C:/Users/diego/JetLearn/Data Science/Lesson 4/Titanic.csv")

class_2_and_3 = data[(data["Survived"] == 0) & (data["Age"] <= 18)]
print(class_2_and_3[["Name","Pclass",]].head())
print(class_2_and_3.shape)
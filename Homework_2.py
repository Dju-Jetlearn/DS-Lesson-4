import pandas as pd

data = pd.read_csv("C:/Users/diego/JetLearn/Data Science/Lesson 4/Titanic.csv")

print(data.groupby(["Sex", "Pclass"])["Age"].mean())

died = data[(data["Survived"] == 0)]

mean_died_age_sex = died.groupby("Sex")["Age"].mean()

print(mean_died_age_sex)

median_died_age_sex = died.groupby("Sex")["Age"].median()

print(median_died_age_sex)
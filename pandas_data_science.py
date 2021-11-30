import pandas as pd
titanic_df= pd.read_csv(r"C:\Users\chukw\PycharmProjects\Pandas_Data_science\Course_Materials_Part1\Coding_Exercises\titanic.csv")
# The pandas display
pd.options.display.min_rows= None
pd.options.display.max_rows =60
print(titanic_df)

print("Titanic datahead\n",titanic_df.head(20))
print("Titanic datatail\n",titanic_df.tail(20))

print(titanic_df.info()) # to show you the information of the dataset

print(titanic_df.describe()) # To describe the statistical distribution of the numerical columns of the dataset
print(titanic_df.describe(include="O"))

print(type(titanic_df))
print(len(titanic_df))
print(round(titanic_df,0))
print(min(titanic_df))

# Dataframe Attribute
print(titanic_df.shape)
print(titanic_df.size)
print(titanic_df.index)
print(titanic_df.columns)

# DATAFRAME ATTRIBUTES
print(titanic_df.head(n=2))
print(titanic_df.info())
print(titanic_df.min())

# Method Chaining
print(titanic_df.mean().sort_values().head(2))

print(titanic_df.sort_values(by = ['age'],ascending=False))


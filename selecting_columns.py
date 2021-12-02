import pandas as pd
titanic_df = pd.read_csv(r"C:\Users\chukw\PycharmProjects\Pandas_Data_science\Course_Materials_Part1\Coding_Exercises\titanic.csv")
print("Age column of the titanic_df:",titanic_df["age"]) # slicing age
print(type(titanic_df["age"]))
print(titanic_df[['age','sex']])
print(type(titanic_df[['age','sex','fare']]))
print(type(titanic_df[['age']]))

# Selecting one Column with dot notation
print(titanic_df.age.equals(titanic_df["age"]))

# Zero-based Indexing and Negative Indexing
summer = pd.read_csv(r"C:\Users\chukw\PycharmProjects\Pandas_Data_science\Course_Materials_Part1\Coding_Exercises\summer.csv", index_col= "Athlete")
pd.options.display.min_rows= None
pd.options.display.max_rows =30
print(summer)
print(summer.info())
print(summer.iloc[0])
print(summer.iloc[1])
print(summer.iloc[-1])
print(summer.iloc[[1,2,3]])
print(summer.iloc[-5:])
print(summer.iloc[:4])
print(summer.iloc[:])
print(summer.iloc[[2,45,5467],:])

# selecting one element, row and column
print(summer.iloc[0,4])
print(summer.iloc[0,:3])
print(summer.iloc[[34,39,60],[0,2,5,7]])
print(summer.loc["AHMADOV, Emin"])
print(summer.loc["PHELPS, Michael"])
print(summer.loc[["PHELPS, Michael", "LEWIS, Carl"], ["Medal", "Event"]])
print(summer.loc["DRIVAS, Dimitrios": "BLAKE, Arthur", "City":"Discipline"])

# Indexing and slicing and reindex()

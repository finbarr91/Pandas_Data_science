import pandas as pd
summer = pd.read_csv(r"C:\Users\chukw\PycharmProjects\Pandas_Data_science\Course_Materials_Part1\Coding_Exercises\summer.csv")
print(summer.head())

# Getting the first 5 rows an rows 354 and 765
rows = list(range(5)) + [354, 765]
print(rows)
print(summer.iloc[rows])


# Case 2: Getting the first three columns and the columns "Gender" and "Event"
summer.columns[:3].to_list() + ["Gender", "Event"]
col = summer.columns[:3].to_list() + ["Gender", "Event"]
print(summer.loc[:,col])

# Case 3: Combining position - and label-based indexing : Rows at Positions 200 and 300 and columns "Athlete"
# and "Medal"

print(summer)
print(summer.loc[[200,300], ["Athlete", "Medal"]])

# Case 4: Combining Position - and label-based indexing : Rows "PHELPS Michael" and positional columns 4 and 6
summer = pd.read_csv("summer.csv", index_col="Athlete")
col = summer.columns[[4,6]]
print(summer.loc["PHELPS, Michael", col])


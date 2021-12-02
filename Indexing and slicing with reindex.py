import pandas as pd
summer = pd.read_csv(r'C:\Users\chukw\PycharmProjects\Pandas_Data_science\Course_Materials_Part1\Coding_Exercises\summer.csv')
# print(summer.loc[[0,100,4000],["Athlete", "Medal", "Age"]])
print(summer.reindex(index=[0,100,40000],columns=["Athlete", "Medal", "Age"]))

summer = pd.read_csv(r'C:\Users\chukw\PycharmProjects\Pandas_Data_science\Course_Materials_Part1\Coding_Exercises\summer.csv', index_col="Athlete")
#print(summer.reindex(index=["PHELPS, Michael"], columns=["Medal", "Age"])) # It throws error because the Phelps Michael is a duplicate column, therefore for reindex to work, it has to take a unique column or row.



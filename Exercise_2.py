import pandas as pd
cars = pd.read_csv(r'C:\Users\chukw\PycharmProjects\Pandas_Data_science\Course_Materials_Part1\Coding_Exercises\cars.csv')
pd.options.display.min_rows= None
pd.options.display.max_rows = 60
print(cars)

print(cars.columns)
print(cars.name[393])
print(cars.iloc[393])
print(cars["name"])

print(cars.iloc[100,:])
print(cars.iloc[200]['name'])
print(cars.iloc[-10:,[0,3,7,8]])


cars = pd.read_csv(r'C:\Users\chukw\PycharmProjects\Pandas_Data_science\Course_Materials_Part1\Coding_Exercises\cars.csv',index_col='name')
print(cars.head(10))
print(cars.info())
print(cars.index)
print(cars.columns)
print(cars.loc['ford ranger']['weight'])
print(cars.loc['ford torino',['model_year', 'origin']])
print(cars.loc[:,['mpg','weight']])
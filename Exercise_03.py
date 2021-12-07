# Import Pandas (as pd),
# Import the Cars Dataset (cars.csv) and save the DataFrame in the variable cars and
# Inspect/Print cars!

import pandas as pd
cars = pd.read_csv(r"C:\Users\chukw\PycharmProjects\Pandas_Data_science\Course_Materials_Part1\Coding_Exercises\cars.csv")
pd.options.display.max_rows =400
print(cars)
print("Car Columns:\n", cars.columns)

# Select the column "name"
# with the attribute (dot) notation! What is the name of the car with index label 393?

print("Car column name\n", cars.name)
print("Name of the car with index location 393\n", cars.name.iloc[393])
# Apply also the second alternative to select the column "name"!
print("Car column name\n", cars['name'])

# Select the car/row at index position 100
# with the iloc operator (all columns)! How many cylinders does the car have?
print("Name of the car with index location 100\n", cars.iloc[100])

# Select the car/row at index position 200 with the iloc operator (and only the column "name")!
# What is the name of the car?
print("row at index position 200 and column name\n",cars.iloc[200,8])

# Select the last 10 rows and the columns mpg, horsepower, origin and name
# with the iloc operator! Fill in the Gaps!
# What is the mpg of the vw pickup?
last_10_rows = cars.iloc[-10:,[0,3,7,8]]
print("last 10 rows and the columns mpg, horsepower, origin and name\n", last_10_rows)

# Import the Cars Dataset one more time (save in the variable cars) and
# set the column "name" as the index!
cars = pd.read_csv(r"C:\Users\chukw\PycharmProjects\Pandas_Data_science\Course_Materials_Part1\Coding_Exercises\cars.csv", index_col='name')
print('Cars columns\n',cars.head(10))
print("Cars info\n ", cars.info())
# Inspect the new Index of the DataFrame by calling the index attribute!
print("Inspect the new Index of the DataFrame \n", cars.index)

# Select the row with the index label "ford ranger" (use the loc operator)!
# What is the weight?
print("row with the index label 'ford ranger'", cars.loc['ford ranger'])

# Select the Select the row with the index label "ford torino" and only the columns "model_year" and "origin"!
# What´s the model year?!
# What´s the model year?
print('row with the index label "ford torino" and only the columns "model_year" and "origin"!\n', cars.loc['ford torino', ['model_year','origin']])

# Select the columns "mpg" and "weight" (all rows) with the loc operator!
print('the columns "mpg" and "weight" (all rows)\n', cars.loc[:,['mpg','weight']])

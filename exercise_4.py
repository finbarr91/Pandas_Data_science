#run the cell!
import pandas as pd

#run the cell!
cars = pd.read_csv(r"C:\Users\chukw\PycharmProjects\Pandas_Data_science\Course_Materials_Part1\Coding_Exercises\cars.csv")
pd.options.display.max_rows = 400
print(cars)
print("Info of cars\n", cars.info())

# Select the index (row labels) of the DataFrame cars! What kind of index do we have
print("Select the index (row labels) of the DataFrame cars\n", cars.index)

# Set the "name" column as the new index of cars (save the changes)!
cars.set_index('name',inplace=True)
print(cars.head(10))

# Check whether the new index contains only unique values (no duplicates)! Is this the case?
print("Check whether the new index contains only unique values\n", cars.index.is_unique)

# Get the frequency/Counts of all unique values in the index! What is the most frequent value?
print("The frequency/Counts of all unique values in the index\n", cars.index.value_counts())
cars.index.name = 'car_model'
print(cars.head(10))
cars.reset_index(inplace=True)
print(cars.head(10))

# Inspect the column Index!
print("the column Index",cars.columns)

# Rename the column Labels "horsepower" and "origin" to "hp" and "country"!
cars.rename(columns={"horsepower": "hp", "origin" : "country" },inplace=True)
print(cars.head(10))
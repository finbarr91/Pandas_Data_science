import pandas as pd

#run the cell!
cars = pd.read_csv(r"C:\Users\chukw\PycharmProjects\Pandas_Data_science\Course_Materials_Part1\Coding_Exercises\cars.csv")
print("Head of cars\n", cars.head(n=10))

#run the cell!
print("Info of cars\n",cars.info())
print("Describe method of the cars dataframe\n", cars.describe(include='O'))
mpg = cars.mpg.copy()
print('MPG  column of cars\n', mpg)
print("Type of mpg of cars\n", type(mpg))

# Get some summary statistics on the Series mpg! What is the mpg of the least fuel efficient car?
print(cars.describe())

# Get the maximum Value in the Series mpg by explicitly calling the ... method!
# The most fuel efficient car has a mpg of...?
print("Maximum value in the series mpg \n", mpg[mpg.idxmax()])

# Get the Frequency/Counts of all unique values in the Series mpg!
# What is the most frequent value?
print("Frequency/Counts of all unique values in the Series mpg\n", mpg.value_counts() )

# Get the relative frequencies in the Series mpg!
# What is the relative frequency of the most frequent value?
print('The relative frequencies in the Series mpg\n',mpg.value_counts(normalize=True))

# Sort the Series mpg from low to high! What is the second lowest value?
print("Sort the Series mpg from low to high\n",mpg.sort_values(ascending=True))

# Sort the Series mpg from low to high! What is the second lowest value?
print("Sort the Series mpg from low to high\n",mpg.value_counts(ascending=True))

# Sort the Series mpg from high to low and
# save the changes by setting the inplace parameter to True!
# Fill in the gaps!

print("Sort the Series mpg from high to low", mpg.sort_values(ascending=False,inplace=True))
print("mpg head of 10\n",mpg.head(10))

# Sort the Series mpg by the Index and save the changes!
mpg= mpg.sort_index()
print("Sort the Series mpg by the Index and save the changes!\n",mpg)
print("mpg head of 10\n",mpg.head(10))

# Miles per Gallon (mpg) can be transformed into Liter per 100 Kilometer with the following formula:
# Liter per 100 Kilometer = 235.21 / mpg
# Create a new Pandas Series l_per_100 by applying the above formula!
# Round the results to 2 decimals! Fill in the gaps!
# l_per_100  = 235.21/mpg

l_per_100= round(235.21/mpg,2)
print("new Pandas Series l_per_100\n",l_per_100)
print(type(l_per_100))

# Get some summary statistics on the Series l_per_100! What is the average value?
print("summary statistics on the Series l_per_100\n",l_per_100.describe())

# Select the non-numerical column "origin",
# create a copy and save the column/Pandas Series in the variable origin!
origin = cars.origin.copy()
print("Origin series\n", origin)

# Call the describe() method on the non-numerical Series "origin"!
# What is the most frequent value?
print("The describe method on the non-numerical Series origin\n", origin.describe())

# Get all unique values in the Series origin!
# Apart from the value usa, there are also the values...?
print("Unique values in the Series Origin\n", origin.unique())

# Last but not least, count the frequencies in the Series origin!
# How often does the value europe appear?
print("count the frequencies in the Series origin\n", origin.value_counts())
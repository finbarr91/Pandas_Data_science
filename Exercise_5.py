import pandas as pd

#run the cell!
cars = pd.read_csv(r"C:\Users\chukw\PycharmProjects\Pandas_Data_science\Course_Materials_Part1\Coding_Exercises\cars.csv")
print(cars.head(10))

# Check for all elements in the column "origin" whether they are equal to "europe".
# Save the boolean Series in the variable mask1! Fill in the gaps!

mask1 = cars.origin.str.contains("Europe", case=False)
# mask1 = cars.origin =="europe"
print("elements in the column origin whether they are equal to europe\n", mask1, "\n")

# Check for all elements in the column mpg whether they are smaller than 20.
# Save the boolean Series in the variable mask2!
mask2 = cars.mpg<20
print("elements in the column mpg whether they are smaller than 20\n", mask2,"\n")

# Filter the cars DataFrame for all cars from europe (use mask1)
# and save the subset in the variable europe! Fill in the gaps!
europe = cars.loc[mask1,:]
print("cars DataFrame for all cars from europe \n", europe)

# Get some meta information on the DataFrame europe. How many cars are from europe?
print("Type of the Europe dataset\n",type(europe), "\n")
print("Get some meta information on the DataFrame europe\n", europe.info(), "\n")

# Filter the DataFrame cars for all cars from europe with low fuel efficiency (mpg lower than 20).
# Use mask1 and mask2!
# Save the subset in the variable europe_le! Fill in the gaps!

europe_le = cars.loc[(mask1&mask2),:]
print("DataFrame cars for all cars from europe with low fuel efficiency (mpg lower than 20)\n", europe_le.head(10))

# Filter the DataFrame cars for all cars with an mpg between 10 and 15 (both ends inclusive!).
# Save the subset in the variable mpg_10_15! Fill in the gaps!
mpg_10_15 = cars.loc[cars.mpg.between(10,15,inclusive=True)]
print(" DataFrame cars for all cars with an mpg between 10 and 15 (both ends inclusive!) \n", mpg_10_15.head(10))

# Inspect! How many cars are in the subset?
print("Info of the mpg_10_15 \n", mpg_10_15.info())

# Filter the Dataframe cars for all cars that are not built in the years 73 and 74,
# and only the columns "mpg" and "name"!
# Save the subset in the variable not_73_74. Fill in the gaps!

mask_3 = ~cars.model_year.isin([73,74])
print("Type of mask 3\n",type(mask_3))

not_73_74 = cars.loc[mask_3,['mpg','name']]
print("Dataframe cars for all cars that are not built in the years 73 and 74\n", not_73_74.head())

# Inspect! How many cars are in this subset?
print("Info of the not_73_74\n", not_73_74.info() )

# Drop the columns "displacement" and "cylinders" from the DataFrame cars! Save the change!
print(cars.drop(columns=['displacement','cylinders'], inplace=True))
# Drop all rows/cars from "usa" from the DataFrame cars! Use the loc operator and overwrite cars!
cars = cars.loc[cars.origin != 'usa']
print(" Drop all rows/cars from usa from the DataFrame cars\n",cars.head(10))

# Add the new column "l_per_100km"
# to the DataFrame cars by calculating 235.21/mpg. Round to 2 decimals.
# Fill in the gaps!

cars["l_per_100km"] = round(235.21/cars["mpg"],2)
print(cars.head(10))

print(cars.loc[cars.name=="audi 100 ls"])

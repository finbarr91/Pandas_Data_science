"""
Coding Exercises (Part 1)
Now, you will have the opportunity to analyze your own dataset.
Follow the instructions and insert your code! You are either requested to

Complete the Code and Fill in the gaps. Gaps are marked with "---" and are placeholders for your code fragment.
Write Code completely on your own
In some exercises, you will find questions that can only be answered, if your code is correct and returns the right output! The correct answer is provided below your coding cell. There you can check whether your code is correct.

If you need a hint, check the Hints Section at the end of this Notebook. Exercises and Hints are numerated accordingly.

If you need some further help or if you want to check your code, you can also watch the solutions videos or check the solutions notebook.

Have Fun!
"""
import pandas as pd
#Import the Cars Dataset and store the Pandas DataFrame in the variable cars! Fill in the gaps!
cars = pd.read_csv(r"C:\Users\chukw\PycharmProjects\Pandas_Data_science\Course_Materials_Part1\Coding_Exercises\cars.csv")



# Some more details on the Columns:
# mpg: Measures fuel efficiency in terms of miles per gallon. Higher mpg means higher efficiency
# cylinders: Number of cylinders in the car
# displacement: Technical feature (engine)
# horsepower: Unit of measurement for engine power
# weight: weight in lbs
# acceleration: time to accelerate from 0 to 60 mph (sec.)
# model_year: self explanatory
# origin: origin of the manufacturer/car
# name: model name

# 3a. Inspect the DataFrame cars by "printing" cars!
print(cars.head(10))

#3b. Inspect the first 10 Rows of the DataFrame cars! Fill in the gaps! What is the name of the very first car in the first row (index label/pos = 0)?

print(cars.head(10))


#3c. Also inspect the last 5 Rows! How many cars/rows do we have in the Dataset (mind the range index starting from 0!)?
print(cars.tail(5))
# 4 . Inspect the entire DataFrame (all rows)! Fill in the gaps!
pd.options.display.max_rows = 400
print(cars)
# Get some meta information on our DataFrame! In which Column do we have missing/NaN Values?
print(cars.info())
# We have 6 missing/NaN Values in the column ... horsepower!

# Let´s get some summary statistics on our DataFrame! What is the maximum value in the column horsepower?
print(cars.describe())
# The maximum value in the column horsepower is ... 230!

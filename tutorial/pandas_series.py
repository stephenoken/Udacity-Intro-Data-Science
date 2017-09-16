import pandas as pd

series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -1789710578])
print(series)

series = pd.Series(
        ['Dave', 'Cheng', 42, 95574],
        index=['Instructor', 'Curriculum Manager', 'Course Number', 'Power Level']
        )

print(series['Instructor'])
print(series[['Instructor', 'Curriculum Manager', 'Course Number']])

cuteness = pd.Series([1, 2, 3, 4, 5], index=['Cockroach', 'Fish', 'Mini Pig',
                                                 'Puppy', 'Kitten'])

print(cuteness > 3)
print('\n')
print(cuteness[cuteness > 3])

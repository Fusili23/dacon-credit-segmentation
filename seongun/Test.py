import numpy as np
import pandas as pd
#TEST
#TEST
#TEST
#TEST
#TEST
#TEST
#TEST

# Set a random seed for reproducibility
np.random.seed(0)

# Sample student names and subjects
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
subjects = ['Math', 'Science', 'History']

# Generate random grades (integers between 60 and 100)
grades = np.random.randint(60, 101, size=(len(students), len(subjects)))

# Create a DataFrame using Pandas
df = pd.DataFrame(grades, index=students, columns=subjects)

# Add an "Average" column
df['Average'] = df.mean(axis=1)

# Print the DataFrame
print("Student Grades:\n")
print(df)

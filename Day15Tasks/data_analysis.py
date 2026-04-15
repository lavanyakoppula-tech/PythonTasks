# Data Analysis 

import numpy as np
import pandas as pd

#Generate marks using NumPy
marks = np.random.randint(30, 100, 10)   # 10 students marks between 30–100

#Convert into Pandas DataFrame
df = pd.DataFrame(marks, columns=["Marks"])

# Filter passing students (marks >= 50)
passing_students = df[df["Marks"] >= 50]

# Step 4: Calculate mean using NumPy
mean_marks = np.mean(marks)

# Print results using loop
print("All Student Marks:")
print(df)

print("\nPassing Students:")
for index, row in passing_students.iterrows():
    print(f"Student {index + 1}: {row['Marks']}")

print("\nAverage Marks:", mean_marks)

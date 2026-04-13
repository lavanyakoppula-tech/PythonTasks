import numpy as np

# Given data
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [50, 65, 70],
    [90, 95, 85],
    [40, 55, 60]
])

# Calculate total marks of each student (row-wise sum)
total_marks = np.sum(marks, axis=1)

# Calculate class average (average of total marks)
class_average = np.mean(total_marks)

#Identify students with total marks above average
above_avg_students = total_marks[total_marks > class_average]

# Output results
print("Total Marks of Each Student:", total_marks)
print("Class Average:", class_average)
print("Students with Above Average Marks:", above_avg_students)

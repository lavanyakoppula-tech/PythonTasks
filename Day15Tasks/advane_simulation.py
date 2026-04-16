import random
import numpy as np
import pandas as pd
import math


# OOP: Student class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.grade = self.calculate_grade()

    # Assign grade using conditions
    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"


try:
    # Generate random marks
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    marks_list = [random.randint(0, 100) for _ in range(len(names))]

    # Store in NumPy array
    marks_array = np.array(marks_list)

    # Create Student objects using loop
    students = []
    for i in range(len(names)):
        students.append(Student(names[i], marks_array[i]))

    # Convert to Pandas DataFrame
    data = {
        "Name": [s.name for s in students],
        "Marks": [s.marks for s in students],
        "Grade": [s.grade for s in students]
    }

    df = pd.DataFrame(data)

    # Math module for statistics
    avg = sum(marks_array) / len(marks_array)
    highest = max(marks_array)
    lowest = min(marks_array)
    sqrt_avg = math.sqrt(avg)

    # Print report
    print("Student Report:\n")
    print(df)

    print("\nStatistics:")
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Square root of average:", sqrt_avg)

    # Save report to file
    df.to_csv("student_report.csv", index=False)
    print("\nReport saved to student_report.csv")


except Exception as e:
    print("An error occurred:", e)

import random
import numpy as np
import pandas as pd
import math


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.grade = self.assign_grade()

    def assign_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        elif self.marks >= 40:
            return 'D'
        else:
            return 'F'

    def to_dict(self):
        return {
            "Name": self.name,
            "Marks": self.marks,
            "Grade": self.grade
        }



# Main Simulation Function
def simulate_results(num_students):
    try:
        students = []
        marks_list = []

        # Generate random marks
        for i in range(num_students):
            name = f"Student_{i+1}"
            marks = random.randint(0, 100)
            student = Student(name, marks)

            students.append(student)
            marks_list.append(marks)

        # Convert to NumPy array
        marks_array = np.array(marks_list)

        # Math module statistics
        mean_marks = sum(marks_list) / len(marks_list)
        variance = sum((x - mean_marks) ** 2 for x in marks_list) / len(marks_list)
        std_dev = math.sqrt(variance)

        print(f"Mean Marks: {mean_marks:.2f}")
        print(f"Standard Deviation: {std_dev:.2f}")

        # Convert to Pandas DataFrame
        df = pd.DataFrame([s.to_dict() for s in students])

        return df

    except Exception as e:
        print(f"Error occurred: {e}")

def save_report(df, filename="report.csv"):
    try:
        df.to_csv(filename, index=False)
        print(f"Report saved successfully as {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")


if __name__ == "__main__":
    df = simulate_results(5)

    if df is not None:
        print("\nStudent Report:")
        print(df)

        save_report(df)

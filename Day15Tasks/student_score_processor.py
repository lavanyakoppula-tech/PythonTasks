import numpy as np
import pandas as pd
import math

#data
students = [("Ram", 45), ("ajay", 67), ("John", 55), ("sai", 30)]
#convert data into dictionary
student_dict = dict(students)
print("students data:\n",student_dict)

#Use a loop + condition to find students scoring above 50
above_50 = []
for name, marks in student_dict.items():
    if marks > 50:
        above_50.append(name)
print("Students scoring above 50:", above_50)

#Use math module to calculate average
marks_array = np.array(list(student_dict.values()))
average = np.mean(marks_array)

print("Average Marks:\n", average)

# Step 5: Convert to DataFrame
df = pd.DataFrame(students, columns=["Name", "Marks"])
print("dataframe:\n",df)

# Step 6: Write to file
with open("student_results.txt", "w") as file:
    file.write("Student Dictionary:\n")
    file.write(str(student_dict) + "\n\n")
    
    file.write("Students scoring above 50:\n")
    file.write(str(above_50) + "\n\n")
    
    file.write("Average Marks:\n")
    file.write(str(average))


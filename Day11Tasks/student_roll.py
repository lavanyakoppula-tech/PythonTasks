import numpy as np

roll_numbers = [101, 102, 103, 104, 105, 106]

# Convert to NumPy array
arr = np.array(roll_numbers)

# Slice index 2 to 4 (4 is excluded)
middle_students = arr[2:5]

print(middle_students)

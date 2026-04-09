import numpy as np

# Marks data
marks = [[78, 85],
         [90, 88],
         [67, 72]]

# Convert to NumPy array
arr = np.array(marks)

# Access second student's second subject mark
print(arr[1][1])

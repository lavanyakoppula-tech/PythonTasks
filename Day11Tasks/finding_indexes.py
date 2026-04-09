import numpy as np
codes = [2, 4, 1, 4, 3, 4, 5]

# Convert to NumPy array
arr = np.array(codes)

# Find indexes where value = 4
indexes = np.where(arr == 4)

print(indexes)

import numpy as np

# Generate 3x3 matrix (0–50)
matrix = np.random.randint(0, 51, (3, 3))

print(matrix)

# Filter elements greater than 25
filter_values = matrix[matrix > 25]

print("filtered",filter_values)

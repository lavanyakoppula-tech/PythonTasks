import numpy as np

# Given data
data = np.arange(1, 13)

# Reshape 3x4 matrix
matrix = data.reshape(3, 4)

#row-wise averages
row_averages = np.mean(matrix, axis=1)

# Output results
print("Original Data:", data)
print("Reshaped Matrix:\n", matrix)
print("Row Averages:", row_averages)

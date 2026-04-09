import numpy as np

# Image matrix
image = [[1, 2, 3],
         [4, 5, 6]]

# Convert to NumPy array
arr = np.array(image)

# Flatten to 1-D array
flat_arr = arr.flatten()

# Print flattened array
print(flat_arr)

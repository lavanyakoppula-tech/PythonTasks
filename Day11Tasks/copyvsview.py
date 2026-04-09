import numpy as np

# Original array
arr = np.array([10, 20, 30, 40])

# Create a copy
arr_copy = arr.copy()

# Modify original array
arr[0] = 100

print("Original array after modification:", arr)
print("Copy of array:", arr_copy)

# Create a view
arr_view = arr.view()

# Modify original array again
arr[1] = 200

print("Original array after second modification:", arr)
print("View of array:", arr_view)

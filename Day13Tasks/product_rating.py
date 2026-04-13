import numpy as np

# Given ratings
ratings = np.array([2, 3, 4, 5, 1])

#Findig min and max values
min_val = np.min(ratings)
max_val = np.max(ratings)

#Normalize ratings
normalized = (ratings - min_val) / (max_val - min_val)

# Output results
print("Original Ratings:", ratings)
print("Normalized Ratings:", normalized)

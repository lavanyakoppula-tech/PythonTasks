import numpy as np
data = np.array([1, 2, 2, 3, 1, 4, 2, 3])

#Finding unique values and counts
unique_values, counts = np.unique(data, return_counts=True)

# Output results
print("Unique Values:", unique_values)
print("Counts:", counts)

# Display as pairs
for val, count in zip(unique_values, counts):
    print(f"{val} occurs {count} times")

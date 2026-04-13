import numpy as np
values = np.array([10, 12, 15, 18, 100, 14, 13])

#mean and standard deviation
mean = np.mean(values)
std_dev = np.std(values)

#Filter values within 2 standard deviations
filtered_values = values[np.abs(values - mean) <= 2 * std_dev]

# Output results
print("Original Values:", values)
print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Filtered Values (without outliers):", filtered_values)

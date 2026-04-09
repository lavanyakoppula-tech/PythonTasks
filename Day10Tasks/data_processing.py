import numpy as np
arr = np.array([12, 7, 25, 3, 18, 10])
sorted_arr = np.sort(arr)

split_arrays = np.array_split(sorted_arr, 2)

# Step 4: Calculate sum of each part
sum_part1 = np.sum(split_arrays[0])
sum_part2 = np.sum(split_arrays[1])

# Output
print("Sorted array:", sorted_arr)
print("Split arrays:", split_arrays)
print("Sum of parts:", sum_part1, sum_part2)

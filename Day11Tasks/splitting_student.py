import numpy as np
scores = [50, 60, 70, 80, 90, 100, 110, 120]
arr = np.array(scores)
split_arrays = np.array_split(arr, 4)

# Print each part
for i, part in enumerate(split_arrays):
    print(f"Part {i+1}:", part)

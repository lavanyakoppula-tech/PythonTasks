import numpy as np

data = np.random.rand(8)

normalized = data * 100
filtered = normalized[normalized > 50]
sorted_vals = np.sort(filtered)

print("sorted:",sorted_vals)

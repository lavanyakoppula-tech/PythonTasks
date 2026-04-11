import numpy as np

salaries = np.array([25000, 40000, 15000, 50000, 30000])

filtered = salaries[salaries > 30000]

print("filter salaries:",filtered)
print("Count:", len(filtered))

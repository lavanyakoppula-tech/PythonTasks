import numpy as np

# Given temperature data
temps = np.array([28, 32, 35, 31, 29, 40, 38])

# Finding indices where temperature > 30
indices = np.where(temps > 30)

# Output results
print("Temperatures:", temps)
print("Indices where the temperature > 30:", indices[0])
print("Temperatures > 30:", temps[indices])

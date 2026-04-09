import numpy as np

# Temperature data
temps = [28, 31, 35, 27, 40, 22]

# Convert to NumPy array
arr = np.array(temps)

# Filter values greater than 30
high_temps = arr[arr > 30]

print(high_temps)

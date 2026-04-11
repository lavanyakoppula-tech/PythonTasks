import numpy as np

arr = [-5, 10, 15, -2, 20, 25, 30]

# Convert to NumPy array
a = np.array(arr)

# Filter positive and even numbers
result = a[(a > 0) & (a % 2 == 0)]

print(result)

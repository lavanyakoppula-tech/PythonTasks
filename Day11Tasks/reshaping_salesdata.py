import numpy as np
sales = [10,20,30,40,50,60,70,80,90,100,110,120]

# Convert to NumPy array
arr = np.array(sales)

# Reshape into 4 × 3 matrix
reshaped_arr = arr.reshape(4, 3)

print(reshaped_arr)

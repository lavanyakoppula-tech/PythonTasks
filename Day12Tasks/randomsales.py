import numpy as np

# Generate random sales for 10 days (100–500)
sales = np.random.randint(100, 501, 10)

print("sales:",sales)

# Find average sales
print("Average:", sales.mean())

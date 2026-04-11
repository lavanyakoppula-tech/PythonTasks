data = [[1, 2, 3], [4, 5], [6]]

# Flatten the list
flat_list = [x for sub in data for x in sub]

# Squares of even numbers
result = [x**2 for x in flat_list if x % 2 == 0]

print("flatted list:",flat_list)
print("final result:",result)
#First list  flattens nested lists into a single list
#Second list filters even numbers and computes their squares

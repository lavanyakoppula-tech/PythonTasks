# Define a list
a = [10, 25, 5, 40, 15]

# Remove duplicates (optional) and sort in descending order
list = list(set(a))
list.sort(reverse=True)

# Get the second largest element
second_largest = list[1]

# Print the result
print("The second largest number is:", second_largest)

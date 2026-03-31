# Define a tuple
my_tuple = (10, 20, 30, 20, 40, 20)

# Take input from the user
element = int(input("Enter an element to count: "))

# Count occurrences
count = my_tuple.count(element)

# Display result
print(f"{element} appears {count} time(s) in the tuple.")

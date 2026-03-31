# Define a tuple
tuple = (10, 20, 30, 40, 50)

# Take input from the user
element = int(input("Enter an element to check: "))

# Check if the element exists in the tuple
if element in tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")

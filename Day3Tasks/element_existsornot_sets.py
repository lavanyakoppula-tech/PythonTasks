# Define a set
my_set = {10, 20, 30, 40, 50}

# Take input from the user
element = int(input("Enter an element to check: "))

# Check if the element exists in the set
if element in my_set:
    print(f"{element} exists in the set.")
else:
    print(f"{element} does not exist in the set.")

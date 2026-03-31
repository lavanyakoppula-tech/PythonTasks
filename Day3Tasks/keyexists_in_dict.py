# Define a dictionary
student_marks = {
    "sai": 85,
    "ravi": 90,
    "Charan": 78
}

# Take input from the user
key_to_check = input("Enter the key to check: ")

# Check if the key exists
if key_to_check in student_marks:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")

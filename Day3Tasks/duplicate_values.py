# Define a list with duplicates
my_list = [10, 20, 20, 30, 10, 40]

# Remove duplicates by converting to a set and back to a list
unique_list = list(set(my_list))

# Print the result
print("List without duplicates:", unique_list)


unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

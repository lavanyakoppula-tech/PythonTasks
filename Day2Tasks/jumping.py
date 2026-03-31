# ---------------------------
# 1. Use break to stop printing numbers when the number reaches 5
print("1. Stop printing when number reaches 5:")
for i in range(1, 11):
    if i == 5:
        print("Reached 5, stopping the loop.")
        break
    print(i, end=" ")


# 2. Use continue to skip printing the number 3
print("2. Skip printing the number 3:")
for i in range(1, 11):
    if i == 3:
        continue
    print(i, end=" ")
print("\n" + "-" * 40)

# 3. Use pass inside a loop
print("3. Demonstrate pass inside a loop:")
for i in range(1, 6):
    if i == 3:
        pass  # Does nothing, just a placeholder
    print(i, end=" ")

# 4. Search for a number in a list and break when found
numbers = [2, 4, 6, 8, 10]
search = int(input("4. Enter a number to search in the list [2,4,6,8,10]: "))
found = False
for num in numbers:
    if num == search:
        found = True
        print(f"Number {search} found in the list!")
        break
if not found:
    print(f"Number {search} not found in the list.")

# 5. Print numbers from 1 to 10 but skip even numbers
print("5. Print numbers 1 to 10 but skip even numbers:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print("\n" + "-" * 40)

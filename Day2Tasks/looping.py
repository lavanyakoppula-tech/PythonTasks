
# 1. Print numbers from 1 to 10 using a for loop
print("1. Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
# 2. Print the multiplication table of a number
num = int(input("2. Enter a number to print its multiplication table: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
# 3. Find the sum of numbers from 1 to N
N = int(input("3. Enter N to find sum of numbers from 1 to N: "))
total = 0
for i in range(1, N + 1):
    total += i
print(f"Sum of numbers from 1 to {N} is: {total}")
#print("-" * 40)
# 4. Print all even numbers between 1 and 50
print("4. Even numbers between 1 and 50:")
for i in range(2, 51, 2):
    print(i, end=" ")
print("\n" + "-" * 40)
# 5. Calculate factorial of a number
num_fact = int(input("5. Enter a number to find its factorial: "))
factorial = 1
for i in range(1, num_fact + 1):
    factorial *= i
print(f"Factorial of {num_fact} is: {factorial}")
#print("-" * 40)

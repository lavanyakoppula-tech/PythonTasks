import random

#Use random to generate 10 numbers and store it in list
numbers = []

for i in range(10):  
    num = random.randint(1, 50)   
    numbers.append(num)          

print("Random Numbers:\n", numbers)

#Use loop + condition to count even/odd numbers

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:     
        even_count += 1
    else:                
        odd_count += 1

print("Even count:\n", even_count)
print("Odd count:\n", odd_count)


# Step 3: Remove duplicates using set
unique_numbers = set(numbers)

print("Unique numbers:\n", unique_numbers)

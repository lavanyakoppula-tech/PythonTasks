                    #OPERATORS


#a=2
#b=3
#c=a&b
#print(c)
#d=a|b
#print(d)
#e=a ^ b
#print(e)
#f=2
#gl=f<<2
#print(gl)
#gr=f>>2
#print(gr)
#h=4
#i =~h
#print(i)


# 1. Check whether a number is positive, negative, or zero
num = float(input("Enter a number to check positive/negative/zero: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#print("-" * 40)

# ---------------------------
# 2. Check if a person is eligible to vote
age = 28
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# 3. Find the largest of three numbers
x=2
y=3
z=4

if x >= y and x >= z:
    largest = n1
elif y >= x and y >= z:
    largest = y
else:
    largest = z
print(f"The largest number is: {largest}")

# 4. Check whether a number is even or odd
a=int (input("enter a number"))
if a % 2 == 0:
    print(f"{a} is even.")
else:
    print(f"{a} is odd.")

# 5. Assign grades based on marks
marks = float(input("Enter marks (0-100) to get grade: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"

print(f"Your grade is: {grade}")


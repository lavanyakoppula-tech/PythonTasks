# -------- calculator.py (module) --------
def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b


# -------- main program --------
# (Assume above functions are in calculator module)
import calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", add(a,b))
print("Subtraction:", sub(a,b))
print("Multiplication:", mul(a,b))
print("Division:", div(a,b))

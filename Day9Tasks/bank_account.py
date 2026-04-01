class Bank:
    def __init__(s,b): 
        s.b = b

    def deposit(s,x): 
        s.b += x

    def withdraw(s,x): 
        if x <= s.b:
            s.b -= x
        else:
            print("Insufficient balance")

b = Bank(1000)
b.deposit(500)
b.withdraw(300)
print(b.b)

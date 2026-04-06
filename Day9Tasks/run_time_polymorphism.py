# Base class
class Payment:
    def process_payment(self):
        print("Processing payment...")

# Derived class 1
class CreditCard(Payment):
    def process_payment(self):
        print("Payment done using Credit Card")

# Derived class 2
class UPI(Payment):
    def process_payment(self):
        print("Payment done using UPI")

# Derived class 3
class NetBanking(Payment):
    def process_payment(self):
        print("Payment done using Net Banking")


# Main function (predefined execution block)
def main():
    payments = [CreditCard(), UPI(), NetBanking()]

    for p in payments:
        p.process_payment()

# Predefined entry point
if __name__ == "__main__":
    main()

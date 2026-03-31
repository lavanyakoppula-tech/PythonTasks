# Q2: Shop Billing System

products = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5
}  # dictionary

cart = []              # list
categories = {"Stationery"}  # set
product_details = ("Name", "Price")  # tuple

# Recursive function for total
def calculate_total(cart_items):
    if len(cart_items) == 0:
        return 0
    return cart_items[0][1] + calculate_total(cart_items[1:])

# Display products
def display_products():
    print("Available Products:")
    for name, price in products.items():
        print(name, ":", price)

# Add to cart
def add_to_cart():
    try:
        name = input("Enter product name: ")

        if name not in products:
            raise NameError

        qty = int(input("Enter quantity: "))
        total_price = products[name] * qty

        cart.append((name, total_price))
        print("Item added to cart")

    except ValueError:
        print("Invalid quantity! Please enter a number.")
    except NameError:
        print("Product not found in store.")
    except TypeError:
        print("Cart data type error.")

# View bill
def view_bill():
    try:
        print("\nItems in Cart:")
        for item in cart:
            print(item[0], ":", item[1])

        total = calculate_total(cart)
        print("Total Bill:", total)

    except ZeroDivisionError:
        print("Calculation error: division by zero.")

# Menu
while True:
    print("\n1. Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_products()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        view_bill()
    elif choice == "4":
        break
    else:
        print("Invalid choice")

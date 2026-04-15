# Store items and prices
cart = []
prices = {
    "apple": 30,
    "banana": 10,
    "milk": 50,
    "bread": 40
}

# Take user input
n = int(input("Enter number of items: "))

for i in range(n):
    try:
        item = input("Enter item name: ").lower()
        
        if item in prices:
            cart.append(item)
        else:
            print("Item not available")
    
    except Exception as e:
        print("Invalid input:", e)

# Remove duplicates using set
unique_items = set(cart)

# Calculate total cost
total = 0
for item in unique_items:
    total += prices[item]

# Display results
print("Cart items:", cart)
print("Unique items:", unique_items)
print("Total cost:", total)

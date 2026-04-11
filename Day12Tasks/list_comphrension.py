prices = [100, 200, 300, 400]

updated_prices = [p * 0.9 if p > 200 else p for p in prices]

print("updated:",updated_prices)

#The list comprehension checks each price:

#If price is greater than 200 → apply 10% discount (p * 0.9)
#Otherwise → keep the price unchanged

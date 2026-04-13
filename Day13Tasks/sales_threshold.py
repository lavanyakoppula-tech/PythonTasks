import numpy as np
sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])
#Calculate average sales
average_sales = np.mean(sales)
#Filter values greater than average
filtered_sales = sales[sales > average_sales]

# Output results
print("Sales:", sales)
print("Average Sales:", average_sales)
print("Filtered Sales (greater than average):", filtered_sales)

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

# create dataframe
df = pd.DataFrame({"Products": products, "Sales": sales, "Profit": profit})

# line graph (sales trend)
plt.subplot(2,3,1)
plt.plot(df["Sales"])
plt.title("Line Graph")

# bar chart (product vs sales)
plt.subplot(2,3,2)
plt.bar(df["Products"], df["Sales"])
plt.title("Bar Graph")

# pie chart (sales contribution)
plt.subplot(2,3,3)
plt.pie(df["Sales"], labels=df["Products"])
plt.title("Pie Chart")

# histogram (profit distribution)
plt.subplot(2,3,4)
plt.hist(df["Profit"])
plt.title("Histogram")

# scatter plot (sales vs profit)
plt.subplot(2,3,5)
plt.scatter(df["Sales"], df["Profit"])
plt.title("Scatter Plot")

# layout fix
plt.tight_layout()

# display all in one window
plt.show()

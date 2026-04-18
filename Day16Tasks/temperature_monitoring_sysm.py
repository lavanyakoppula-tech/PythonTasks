import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# create dataframe
df = pd.DataFrame({"Days": days, "Temps": temps})

# line graph
plt.subplot(2,3,1)
plt.plot(df["Temps"])
plt.title("Line Graph")

# bar chart
plt.subplot(2,3,2)
plt.bar(df["Days"], df["Temps"])
plt.title("Bar Graph")

# pie chart (high vs low)
high = sum(df["Temps"] > 30)
low = sum(df["Temps"] <= 30)
plt.subplot(2,3,3)
plt.pie([high, low], labels=["High", "Low"])
plt.title("Pie Chart")

# histogram
plt.subplot(2,3,4)
plt.hist(df["Temps"])
plt.title("Histogram")

# scatter plot
plt.subplot(2,3,5)
plt.scatter(range(len(df)), df["Temps"])
plt.title("Scatter Plot")

# layout fix
plt.tight_layout()

# display all in one window
plt.show()

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

df = pd.DataFrame({"Months": months, "Sales": sales})

# line graph
plt.subplot(2,3,1)
plt.plot(df["Sales"])
plt.title("Line Graph")

# bar chart
plt.subplot(2,3,2)
plt.bar(df["Months"], df["Sales"])
plt.title("Bar Graph")

# pie chart
plt.subplot(2,3,3)
plt.pie(df["Sales"], labels=df["Months"])
plt.title("Pie Chart")

# histogram
plt.subplot(2,3,4)
plt.hist(df["Sales"])
plt.title("Histogram")

# scatter plot
plt.subplot(2,3,5)
plt.scatter(range(len(df)), df["Sales"])
plt.title("Scatter Plot")

# fix spacing (important)
plt.tight_layout()

# display everything in ONE window
plt.show()

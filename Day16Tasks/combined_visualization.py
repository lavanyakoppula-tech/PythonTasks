import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

sales = np.array([100, 200, 150, 300]) 
products = ["A", "B", "C", "D"]

df = pd.DataFrame({"Products": products, "Sales": sales})

plt.subplot(1,3,1)
plt.plot(df["Sales"])

plt.subplot(1,3,2)
plt.bar(df["Products"], df["Sales"])

plt.subplot(1,3,3)
plt.pie(df["Sales"], labels=df["Products"])

plt.show()

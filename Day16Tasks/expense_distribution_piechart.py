import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

expenses = np.array([500, 300, 200]) 
labels = ["Food", "Rent", "Travel"] 

df = pd.DataFrame({"Expenes": expenses, "Labels": labels})

#plt.pie(df["Expenses"], df["Labels"])
plt.pie(expenses, labels=labels, autopct='%1.1f%%')
plt.show()

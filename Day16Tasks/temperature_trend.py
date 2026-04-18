import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

temps = np.array([28, 30, 32, 31, 29])
series = pd.Series(temps)
plt.plot(series)
plt.title("Temperature Trend")
plt.grid()
plt.show()

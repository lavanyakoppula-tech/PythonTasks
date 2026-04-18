import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = np.array([100, np.nan, 200, 150, np.nan, 300])
series = pd.Series(data)
series.fillna(series.mean(), inplace=True)

plt.plot(series)
plt.show()

filtered = series[series > series.mean()]

plt.bar(range(len(filtered)), filtered)
plt.show()

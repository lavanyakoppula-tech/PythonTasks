import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

scores = np.array([40, 60, 80, 30, 90])
passcount = np.sum(scores > 50)
failcount = np.sum(scores <= 50)

plt.pie([passcount, failcount], labels=["Pass", "Fail"], autopct='%1.1f%%')
plt.show()

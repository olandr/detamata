#https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot
# Seaborn basically

'''
import numpy as np
import pandas as pd
import scipy
'''
import matplotlib.pyplot as plt
import seaborn as sns

dates = ['2018-10-08', '2018-10-09', '2018-10-10', '2018-10-11', '2018-10-12']
emptySpot= [[12, 13, 14, 17, 18, 19, 20], [10, 11, 12, 15, 16, 17, 18, 19, 20], [8, 9, 12, 13, 14, 20], [8, 9, 12, 15, 18, 19, 20], [12, 13, 14, 15, 16, 17, 18, 19, 20]]

sns.set(style="whitegrid")
ax = sns.stripplot(data=emptySpot, jitter=False)

plt.show()

#https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot
# Seaborn basically

'''
import numpy as np
import scipy
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from spotter import get_free_dataframe

superFrame = get_free_dataframe()
sns.set(style="whitegrid")
ax = sns.catplot(x='date', y='hour', hue ="room",data=superFrame)

plt.show()

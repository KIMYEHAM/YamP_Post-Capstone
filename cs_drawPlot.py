import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mp
import  seaborn as sb
#import plotnine as pn
#import folium
#import plot.ly
#import pyecharts


import cs_data



fig = plt.figure()
fig.suptitle('figure sample plots')

fig, ax_lst = plt.subplots(2, 2, figsize=(8,5))

# template: ax_lst[][].plot(x, y, 'type')

ax_lst[0][0].plot([1,2,3,4], 'ro-')
ax_lst[0][1].plot(np.random.randn(4, 10), np.random.randn(4,10), 'bo--')
ax_lst[1][0].plot(np.linspace(0.0, 5.0), np.cos(2 * np.pi * np.linspace(0.0, 5.0)))
ax_lst[1][1].plot([3,5], [3,5], 'bo:')
ax_lst[1][1].plot([3,7], [5,4], 'kx')
plt.show()


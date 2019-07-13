import cs_data as cs
# =========================================================
# Connection to Firebase App
# ---------------------------------------------------------
import firebase_admin
from firebase_admin import credentials

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mp
import seaborn as sb

cs.fb_start()


get_dataH = cs.fb_getData('H', '20190713/Humidity/humidity', 477)
dataH_list = get_dataH.download()

print(dataH_list)

fig = plt.figure()
fig, ax_lst = plt.subplots(1, 1, figsize=(8, 5))

# template: ax_lst[][].plot(x, y, 'type')

ax_lst.plot(dataH_list[0], dataH_list[1], 'ro-')
plt.show()

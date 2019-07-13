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

dataT = cs.loadData('T', '20190713')
dataT_lst = dataT.readFile()
temperature = cs.fb_loadData('T', dataT_lst, '20190713/Temperature/temperature')
temperature.upload()


dataH = cs.loadData('H', '20190713')
dataH_lst = dataH.readFile()
humidity = cs.fb_loadData('H', dataH_lst, '20190713/Humidity/humidity')
humidity.upload()
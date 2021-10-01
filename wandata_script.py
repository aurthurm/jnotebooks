#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime as dt

# Read th csv file
csv_file = pd.read_csv('wandata.csv', header=0)

def handle_empty_strings(x):
    if type(x) == str:
        if len(x) == 0:
            value = np.nan
        else:
            value = float(x)
    else:
        value = x
    return value

for index, col in csv_file.iteritems():
    if index == "Time" or index == "Date":
        pass
    else:
        csv_file[index].replace(regex=True, inplace=True, to_replace=r'[^0-9.^0-9]', value=r'')
        csv_file[index] = csv_file[index].map(lambda x: handle_empty_strings(x))
        csv_file[index].astype(float)        

indexed = csv_file.set_index("Time")

indexed.plot(alpha=1, linestyle='solid', figsize=(15, 60), subplots=True, logy=False, sharex=False, rot=30)
plt.subplots_adjust(hspace=1)
plt.savefig("WanData Graphs " + dt.now().strftime("%d-%m-%y"), papertype="a4", format="pdf", dpi=1000)
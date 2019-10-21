import pandas
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.dates import drange

data1 = pandas.read_csv("D:\\Air Pollution Mapping\\Self\\Data\\1022.csv", parse_dates=['Time'])
data2 = pandas.read_csv("D:\\Air Pollution Mapping\\Self\\Data\\chicuc.csv", parse_dates=['Time'])
criteria = ["", "PM10", "PM2.5", "CO", "NO2", "O3", "TEMP", "HUD", "SO2"]


def multipleplot(a, fig):
    plt.figure(fig)
    for i in range(1, 9):
        plt.subplot(4, 2, i)
        a[criteria[i]].index = pandas.date_range(start=data1['Time'][0], periods=data1.shape[0], freq='H')
        a[criteria[i]].plot()
        plt.ylabel(criteria[i])


multipleplot(data1, 1)
multipleplot(data2, 2)
plt.show()

import pandas
import numpy as np
from sklearn.linear_model import LinearRegression

data1 = pandas.read_csv("D:\\Air Pollution Mapping\\Self\\Data\\1022.csv")
data2 = pandas.read_csv("D:\\Air Pollution Mapping\\Self\\Data\\chicuc.csv")
criteria = ["", "PM10", "PM2.5", "CO", "NO2", "O3", "TEMP", "HUD", "SO2"]


def rsquared(a, b):
    x = np.array(a).reshape(-1, 1)
    y = b
    model = LinearRegression(n_jobs=-1).fit(x, y)
    return model.score(x, y)


def relation(a, b):
    results = []
    for i in range(1, 9):
        row = []
        name_of_x = a.columns[i]
        row.append(name_of_x)
        for j in range(1, 9):
            name_of_y = b.columns[j]
            row.append(rsquared(a[name_of_x], b[name_of_y]))
        results.append(row)
    return results


result1 = pandas.DataFrame(relation(data1, data2), columns=criteria)
result2 = pandas.DataFrame(relation(data2, data2), columns=criteria)
result1.to_csv("D:\\Air Pollution Mapping\\Self\\Data\\Relations_1022_CHICUC.csv", header=True, index=False)
result2.to_csv("D:\\Air Pollution Mapping\\Self\\Data\\Relations_CHICUC_CHICUC.csv", header=True, index=False)

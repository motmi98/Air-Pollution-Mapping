import pandas
import numpy as np
import datetime


def dateparse(x):
    times = datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S%z")
    return times.strftime("%Y-%m-%d")


data1 = pandas.read_csv("D:\\Air Pollution Mapping\\Self\\Data\\1022.csv")
data2 = pandas.read_csv("D:\\Air Pollution Mapping\\Self\\Data\\chicuc.csv")

#data1 = data1[['Time', 'PM2.5']]
#data2 = data2[['Time', 'PM2.5']]

#data1['Time'] = data1['Time'].apply(dateparse)
#data2['Time'] = data2['Time'].apply(dateparse)

#print(data1)

result = data1.merge(data2, left_on='Time', right_on='Time', suffixes=('_1022', '_chicuc'))

# month = []
# day = []
# for time in result['Time']:
#     format = datetime.datetime.strptime(time, "%Y-%m-%d")
#     month.append(format.month)
#     day.append(format.day)
# result.insert(1, "Day", day)
# result.insert(1, "Month", month)
# result_day = result[['Time', 'PM2.5_1022', 'PM2.5_chicuc']].groupby(['Time']).mean()

result.to_csv("D:\\Air Pollution Mapping\\Self\\Data\\Merged.csv", index=False, header=True)

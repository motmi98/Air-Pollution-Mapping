from matplotlib import pyplot as plt
import numpy as np
import pandas

data1 = pandas.read_csv("D:\\Air Pollution Mapping\\Self\\Data\\1022.csv")
data2 = pandas.read_csv("D:\\Air Pollution Mapping\\Self\\Data\\chicuc.csv")


def get_statistics(dataframe):
    statistics =[["Mean", np.mean(dataframe["PM10"]), np.mean(dataframe["PM2.5"]), np.mean(dataframe["CO"]),
                  np.mean(dataframe["NO2"]), np.mean(dataframe["O3"]), np.mean(dataframe["TEMP"]),
                  np.mean(dataframe["HUD"]), np.mean(dataframe["SO2"])],
                 ["Max", np.max(dataframe["PM10"]), np.max(dataframe["PM2.5"]), np.max(dataframe["CO"]),
                  np.max(dataframe["NO2"]), np.max(dataframe["O3"]), np.max(dataframe["TEMP"]),
                  np.max(dataframe["HUD"]), np.max(dataframe["SO2"])],
                 ["Min", np.min(dataframe["PM10"]), np.min(dataframe["PM2.5"]), np.min(dataframe["CO"]),
                  np.min(dataframe["NO2"]), np.min(dataframe["O3"]), np.min(dataframe["TEMP"]),
                  np.min(dataframe["HUD"]), np.min(dataframe["SO2"])],
                 ["Standard Deviation", np.std(dataframe["PM10"]), np.std(dataframe["PM2.5"]), np.std(dataframe["CO"]),
                  np.std(dataframe["NO2"]), np.std(dataframe["O3"]), np.std(dataframe["TEMP"]),
                  np.std(dataframe["HUD"]), np.std(dataframe["SO2"])],
                 ["Median", np.median(dataframe["PM10"]), np.median(dataframe["PM2.5"]), np.median(dataframe["CO"]),
                  np.median(dataframe["NO2"]), np.median(dataframe["O3"]), np.median(dataframe["TEMP"]),
                  np.median(dataframe["HUD"]), np.median(dataframe["SO2"])]]
    return statistics


frame1 = pandas.DataFrame(get_statistics(data1), columns=["", "PM10", "PM2.5", "CO", "NO2", "O3", "TEMP", "HUD", "SO2"])
frame1.to_csv("D:\\Air Pollution Mapping\\Self\\Data\\StatisticsFIMO.csv", header=True, index=False)

frame2 = pandas.DataFrame(get_statistics(data2), columns=["", "PM10", "PM2.5", "CO", "NO2", "O3", "TEMP", "HUD", "SO2"])
frame2.to_csv("D:\\Air Pollution Mapping\\Self\\Data\\StatisticsCHICUC.csv", header=True, index=False)




import pandas
import math

chuan = pandas.read_csv("D:\\Air Pollution Mapping\\Self\\Data\\10tramEPA.csv")
fairkit = pandas.read_csv("D:\\Air Pollution Mapping\\Self\\Data\\tramFAirKit.csv")
distances = [[0 for x in range(fairkit.shape[0]+1)] for y in range(chuan.shape[0]+1)]
distance = 0


def measure(lat1, lon1, lat2, lon2):
    R = 6378137
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + \
        math.cos(math.radians(lat1)) * \
        math.cos(math.radians(lat2)) * \
        math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d / 1000


for i in range(chuan.shape[0]):
    for j in range(fairkit.shape[0]):
        if i == 0:
            distances[i][j + 1] = fairkit["Abbr"][j]
        if j == 0:
            distances[i + 1][j] = chuan["Abbr"][i]
        distances[i+1][j+1] = measure(chuan["Lat"][i], chuan["Lon"][i], fairkit["Lat"][j], fairkit["Lon"][j])


data = pandas.DataFrame(distances)
data.to_csv("D:\\Air Pollution Mapping\\Self\\Data\\Distances.csv", index=False, header=False)

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt


# csv to dataframe
def backdf(el):
    csv = pd.read_csv(str(el))
    retdf = pd.DataFrame(csv)
    return retdf


# sorts the VI rows
def backViData(fileArr, rownum):
    data = np.array([])
    for x in np.nditer(fileArr):
        df = backdf(x)
        data = np.append(data, df.iloc[rownum, 1:-2])
    return data


# sorts the date and converts string to date
def backTimeData(fileArr):
    timedata = np.array([])
    strdata = np.array([])
    for x in np.nditer(fileArr):
        df = backdf(x)
        strdata = np.append(strdata, df.columns[1:-2])
    i = len(strdata) - 1
    while i >= 0:
        temp_obj = [datetime.strptime(strdata[i], '%Y_%m_%d').date()]
        timedata = np.append(timedata, temp_obj)
        i -= 1
    return timedata


# ndvi files
files_ndvi = np.array(['NDVI(2000-2003).csv'])
# evi files
files_evi = np.array(['EVI(2000-2003).csv'])

sundarbansNdvi = backViData(files_ndvi, 0)
sundarbansEvi = backViData(files_evi, 0)
years_ndvi=backTimeData(files_evi)
years_evi = backTimeData(files_evi)
ctgNdvi = backViData(files_ndvi, 1)
ctgEvi = backViData(files_evi, 1)
# test if there are any unmatched years
# print(years_evi[years_evi != years_ndvi])
# visualization
plt.plot(years_evi, sundarbansEvi, label="Sundarbans")
plt.plot(years_evi, ctgEvi, label="Khagrachari")
plt.title("MODIS EVI Time Series (2000-2020)", pad=20, fontdict={'fontsize': 18, 'fontweight': 'bold'})
plt.xlabel("Year", labelpad=15, fontdict={'fontsize': 12})
plt.ylabel("EVI", labelpad=15, fontdict={'fontsize': 12})
plt.legend()
plt.show()

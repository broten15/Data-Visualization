import csv 
from matplotlib import pyplot as plt
from datetime import datetime
import numpy as np


filename = 'chap16\\weather_data\\sitka_weather_2018_full.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    date_row = header_row.index("DATE")
    rain_row = header_row.index("PRCP")

    # Gets info
    dates, rainfalls = [], []
    for row in reader:
        try:
            date = datetime.strptime(row[date_row], "%Y-%m-%d")
            rainfall = float((row[rain_row]))
        except ValueError:
            print(date, 'Info not found')
        else:
            dates.append(date)
            rainfalls.append(rainfall)

# Plots data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, rainfalls, c='blue')

# formats plot
plt.title("Daily percipitation in sitka")
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Rainfall (in)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(bottom=0, top=3)


plt.show()


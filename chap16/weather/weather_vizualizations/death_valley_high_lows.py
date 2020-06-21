import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Gets information
filename = 'chap16\\weather\\weather_data\\death_valley_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            # Gets info
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[6])
            low = int(row[7])
        except ValueError:
            # if the info not found
            print(current_date, 'Information not found')
        else:
            # Appends info
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plots information
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
plt.title("Daily high temperatures in Death Valley in 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(bottom=0, top=130)

plt.show()

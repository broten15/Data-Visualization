import csv 
from matplotlib import pyplot as plt
from datetime import datetime

def plot_data(filenames):
    
    # Formats plot
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.title('Daily high and low temps for death valley and sitka', fontsize=16)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.ylim(bottom=0, top=130)

    for filename in filenames:
        # Gets information 
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            date_row = header_row.index("DATE")
            high_row = header_row.index("TMAX")
            low_row = header_row.index("TMIN")

            dates, highs, lows = [], [], []
            for row in reader:
                try:
                    # Get info
                    current_date = datetime.strptime(row[date_row], '%Y-%m-%d')
                    high = int(row[high_row])
                    low = int(row[low_row])
                except ValueError:
                    # if info does not exist
                    print(current_date, 'Information not found')
                else:
                    # Appends info
                    dates.append(current_date)
                    highs.append(high)
                    lows.append(low)

        # Plots information
        plt.plot(dates, highs, c='red', alpha=0.5)
        plt.plot(dates, lows, c='blue', alpha=0.5)
        plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

filenames = ['chap16\\weather_data\\sitka_weather_2018_full.csv', 
    'chap16\\weather_data\\death_valley_2018_full.csv']

plot_data(filenames)

plt.show()
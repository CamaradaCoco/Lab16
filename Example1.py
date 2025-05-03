from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('Data/sitka_weather_2018_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#for index, column_title in enumerate(header_row):
#    print(index, column_title)

dates = []
high_temps = []
low_temps = []

for row in reader:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        print(current_date)
        high = int(row[8])
        low = int(row[9])

        dates.append(current_date)
        high_temps.append(high)
        low_temps.append(low)
    except ValueError:
        continue

plt.style.use('dark_background')
fig, ax = plt.subplots()

ax.plot(dates, high_temps, color='red')
ax.plot(dates, low_temps, color='blue')
ax.fill_between(dates, high_temps, low_temps, color="yellow")

ax.set_title("Daily high temperatures, July 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
fig.autofmt_xdate()

plt.show()

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('Data/OHUR.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_title in enumerate(header_row):
    print(index, column_title)

dates = []
ohur = []

for row in reader:
    try:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        ohur_value = float(row[1])

        dates.append(current_date)
        ohur.append(ohur_value)
    except ValueError:
        continue

plt.style.use('dark_background')
fig, ax = plt.subplots()

ax.plot(dates, ohur, color='green')
ax.fill_between(dates, ohur, color="yellow")
ax.grid(which='major', color='white', linestyle='--', linewidth=0.5)

ax.set_title("Ohio Unemployment Rate", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Unemployment Rate", fontsize=16)
fig.autofmt_xdate()

plt.show()
"""
Lab 16 #1 -- Ohio Unemployment Rate Graph
Nicholas Smith
3 May 2025
"""

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Create a path object to the OHUR csv file
path = Path('Data/OHUR.csv')
lines = path.read_text(encoding='utf-8').splitlines()

# Read the csv file and create a reader object
reader = csv.reader(lines)

"""
# Enumerate the header row to see the column titles
header_row = next(reader)

for index, column_title in enumerate(header_row):
    print(index, column_title)
"""

# Create empty lists to store dates and unemployment rates
dates = []
ohur = []

# Loop through the rows in the csv file and add to lists. Deal with bad data with try/except block
for row in reader:
    try:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        ohur_value = float(row[1])

        dates.append(current_date)
        ohur.append(ohur_value)
    except ValueError:
        continue

# Create a plot of the unemployment rate data with dark background
plt.style.use('dark_background')
fig, ax = plt.subplots()

# Plot the unemployment rate data with fill and grid background
ax.plot(dates, ohur, color='green')
ax.fill_between(dates, ohur, color="yellow")
ax.grid(which='major', color='white', linestyle='--', linewidth=0.5)

# Set the title and labels for the plot
ax.set_title("Ohio Unemployment Rate (1976-2022)", fontsize=24)
ax.set_xlabel('Date', fontsize=16)
ax.set_ylabel("Unemployment Rate", fontsize=16)
fig.autofmt_xdate()

# Show the plot
plt.show()
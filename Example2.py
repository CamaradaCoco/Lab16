from pathlib import Path
import json
import matplotlib.pyplot as plt
import plotly.express as px

path = Path("Data/eq_data_30_day_m1.json")
contents = path.read_text(encoding="utf-8")
easier_to_read = json.loads(contents)

all_eq_data = easier_to_read["features"]

# path = Path("Data/world_fires_7_day.json")
# new_contents = json.dumps(easier_to_read_eq_data, indent=4)
# path.write_text(new_contents, encoding="utf-8")

mags = []
longs = []
lats = []
eq_titles = []

for eq_data in all_eq_data:
    try:
        mag = eq_data["properties"]["mag"]
        eq_title = eq_data["properties"]["title"]
        lon = eq_data["geometry"]["coordinates"][0]
        lat = eq_data["geometry"]["coordinates"][1]
    except ValueError:
        print("ValueError")
    else:
        mags.append(mag)
        eq_titles.append(eq_title)
        longs.append(lon)
        lats.append(lat)

title = "World Fires 7 Day"
fig = px.scatter_geo(
    lat=lats,
    lon=longs,
    size=mags,
    color = mags,
    projection="natural earth",
    color_continuous_scale="hot",
    labels={'color': "Magnitude"},
    hover_name = eq_titles
    )
fig.show()
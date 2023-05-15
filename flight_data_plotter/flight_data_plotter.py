import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

input_name = "EY421_3048f149.csv"
flight_data = pd.read_csv(input_name)

flight_data[["Latitude","Longitude"]] = flight_data.Position.str.split(
    ",", expand=True).replace('"',"")
flight_data["Latitude"] = flight_data["Latitude"].astype(float)
flight_data["Longitude"] = flight_data["Longitude"].astype(float)

cols_to_plot = [
    "Altitude",
    "Speed",
    "Direction",
    "Latitude",
    "Longitude"
]

callsign = flight_data.loc[0]['Callsign'].split("_")[0]

cols, rows = 1, len(cols_to_plot)

plt.subplots(figsize=(cols*16, rows*9))
plt.suptitle(callsign)

for counter, col in enumerate(cols_to_plot):
    plt.subplot(rows, cols, counter+1)
    
    ax1 = sns.lineplot(data = flight_data, x = "Timestamp", y = col)
    
    plt.xlabel("Timestamp")
    plt.ylabel(col)
    
    if counter+1 == rows:
        plt.savefig("Output/flight_data.png")
        print("Saved!")
        plt.clf()
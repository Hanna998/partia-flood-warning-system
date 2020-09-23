#Imports
from floodsystem.stationdata import build_station_list
from floodsystem import station
import flood
import analysis
from floodsystem import datafetcher
import matplotlib.dates
import datetime

#Build station list
stations = build_station_list()

#defines severity in this function
def stations_in_danger(stations_danger):
    severe = list()
    moderate = list()
    low = list()
    none = list()

    for danger_station in stations_danger:
        if danger_station[1] > 0.5 or danger_station[1] == 0.5:
            low.append(danger_station[0])
        if danger_station[1] > 1.0 or danger_station[1] == 1.0:
            moderate.append(danger_station[0])
        if danger_station[1] > 2.0 or danger_station[1] == 2.0:
            severe.append(danger_station[0])
        if danger_station[1] < 0.5:
            none.append(danger_station[0])
        else:
            continue
    return severe, moderate, low, none

#Check which stations have a water level above their typical maximum level
stations_current_danger = flood.stations_above_max_level(stations)

#get severity
current_danger = stations_in_danger(stations_current_danger)

print ("**RIVERS CURRENTLY IN SEVERE DANGER OF FLOODING**\n")
print(current_danger[0])
print("\n**RIVERS CURRENTLY IN MODERATE DANGER OF FLOODING**\n")
print(current_danger[1])
print("\n**RIVERS CURRENTLY IN LOW DANGER OF FLOODING\n")
print(current_danger[2])


#PREDICTING FUTURE FLOODING
stations_future_names = list()
stations_future_levels = list()
dt = 10

#retrieves two lists of stations above their max level and their levels
for station in stations[:20]:
    dates, levels = datafetcher.fetch_measure_levels(station.measure_id, datetime.timedelta(days = dt))
    #plot_water_level_with_fit(station, dates, levels, 1)
    if dates != [] and levels!= []:
        future_level = analysis.future_levels(dates, levels, 1)
        if station.typical_range != None:
            max_level = station.typical_range[0]
            stations_future_names.append(station.name)
            stations_future_levels.append(future_level)

#zips the two lists into a list of tuples
stations_future = list(zip(stations_future_names, stations_future_levels))

#returns severity of risk of future flooding
future_danger = stations_in_danger(stations_future)

print ("**RIVERS PREDICTED TO BE IN SEVERE DANGER OF FLOODING IN 2 DAYS**\n")
print(current_danger[0])
print("\n**RIVERS PREDICTED TO BE IN MODERATE DANGER OF FLOODING IN 2 DAYS**\n")
print(current_danger[1])
print("\n**RIVERS PREDICTED TO BE IN LOW DANGER OF FLOODING IN 2 DAYS**\n")
print(current_danger[2])


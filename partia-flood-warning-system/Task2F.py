#imports
import numpy as np
import matplotlib.dates
import datetime
from floodsystem import datafetcher
from floodsystem.stationdata import build_station_list
from analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
from flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    highest_levels_stations = stations_highest_rel_level(stations, 5)
    dt = 10
    
    #returns a list of top 5 stations 
    i=0
    stations_to_plot = []
    for n in range(0, len(highest_levels_stations)):
        for station in stations:
            if station.name == highest_levels_stations[i][0]:
                print(highest_levels_stations[i][0])
                stations_to_plot.append(station)
                n+=1
        i+=1

    for station in stations_to_plot:
        dates, levels = datafetcher.fetch_measure_levels(station.measure_id, datetime.timedelta(days = dt))
        plot_water_level_with_fit(station, dates, levels, 4)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
"""
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt
import datetime
from floodsystem.flood import stations_highest_rel_level
from plot import plot_water_levels

"""
#imports
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from flood import stations_highest_rel_level
import matplotlib.pyplot as plt
import datetime


#Provide a program file Task2E.py that plots the water levels over the past 10 days 
#for the 5 stations at which the current relative water level is greatest.
def run():
    #Requirements for Task2E
    n = 6
    dt =10
    stations = build_station_list()
    update_water_levels(stations)
    #build list of tuples of stations
    b_tuples = stations_highest_rel_level(stations, n)

    #Let"s convert the list of tuples into a list of stations!
    b=[]
    for station in stations:        #maybe change the order of these two functions?
        for station_tuple in b_tuples:

            if station.name == station_tuple[0]:
                b.append(station)
                break

    print(b)

    # plot data for each station
    for station in b:
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        if len(dates) == 0 or len(levels) == 0:
            continue  # Test for the stations with incorrect datafetcher responses
        plot_water_levels(station, dates, levels)
        plt.show()

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System *** \n")

    # Run Task2E
    run()
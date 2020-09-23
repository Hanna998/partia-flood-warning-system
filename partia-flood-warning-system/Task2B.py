#Provide a program file Task2B.py that prints the name of each station at which the current relative level is over 0.8, 
#with the relative level alongside the name (do not forget to handle the cases of inconsistent range data).
from floodsystem.stationdata import build_station_list, update_water_levels 
from floodsystem.station import *
from flood import *

def run():
    #Requirements for Task2B
    #we build a list of stations
    stations = build_station_list()
    #update them with the latest water levels
    update_water_levels(stations)
    #a list of stations for which the current relative level is over 0.8
    a= stations_level_over_threshold(stations, 0.8)
    print(a)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
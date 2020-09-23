#Provide a program file Task2C.py that prints the names of the 10 stations at which the current relative level is highest, 
# with the relative level beside each station name. 

from floodsystem.stationdata import *
from floodsystem.station import *
from flood import *

def run():
    #Requirements for Task 2C

    #we build a list of stations
    stations = build_station_list()
    #update them with the water levels
    update_water_levels(stations)
    #prints the names of the 10 stations at which the current relative level is highest
    print(stations_highest_rel_level(stations, 10))     #2 was before...

if __name__=="__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
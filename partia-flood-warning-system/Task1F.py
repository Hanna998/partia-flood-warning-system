from floodsystem import geo
from floodsystem import stationdata
from floodsystem import station
import haversine        #from haversine


def run():
    #builds a list of all stations
    stations = stationdata.build_station_list()     #use_cache=True argument?
    # with inconsistent typical range data

    #gets inconsistent_data
    inconsistent_data = station.inconsistent_typical_range_stations(stations)

    #list with objectums where typical range is bad
    inconsistent_station_names=[]   #empty list
    for i in inconsistent_data:
        inconsistent_station_names.append(i.name) 
        #filling up the list with the names of inconst data
    
    #orders the list of names of inconst stations alphabetically
    order_inconsistent = sorted(inconsistent_station_names)

    print(order_inconsistent)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
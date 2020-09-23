from floodsystem import geo
from floodsystem import stationdata

def run():
    #builds a list of stations
    stations = stationdata.build_station_list(use_cache=True)
    #builds a list of rivers that have at least one monitoring station
    rivers = geo.rivers_with_station(stations)
    #builds a dictionary of rivers matched with their monitoring stations
    rivers_stations = geo.stations_by_river(stations)

    #counts the number of rivers that have at least one monitoring station
    number_rivers = len(rivers)
    print(number_rivers)

    #orders the list of rivers with monitoring stations alphabetically
    order_rivers = sorted(rivers)
    #creates an empty list
    rivers_first = list()
    #adds the first 10 rivers alphabetically to the empty list
    for i in range(0,10):
        rivers_first.append(order_rivers[i])

    print(rivers_first)

    #returns the monitoring stations for River Aire in alphabetical order
    river_aire = rivers_stations["River Aire"]
    print("RIVER AIRE:", sorted(river_aire))

    #returns the monitoring stations for River Cam in alphabetical order
    river_cam = rivers_stations["River Cam"]
    print("RIVER CAM:", sorted(river_cam))

    #returns the monitoring stations for River Thames in alphabetical order
    river_thames = rivers_stations["River Thames"]
    print("RIVER THAMES", sorted(river_thames))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()

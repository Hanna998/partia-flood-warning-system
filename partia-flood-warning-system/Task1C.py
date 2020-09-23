from floodsystem import geo
from floodsystem import stationdata

def run():
    #builds list of stations
    stations = stationdata.build_station_list(use_cache=True)

    #gets a list of stations that are within a radius of a point
    radius_stations = geo.stations_within_radius(stations, (52.2053,0.1218), 10)

    #sorts the list of stations alphabetically
    radius_stations.sort()

    print(radius_stations)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
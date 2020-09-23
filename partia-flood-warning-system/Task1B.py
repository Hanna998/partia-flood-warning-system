from floodsystem import geo
from floodsystem import stationdata

def run():
    "Requirements for Task 1B"
    #Builds a list of stations 
    stations = stationdata.build_station_list(use_cache=True)

    #builds list of tuples of the stations with their distances from the coordinate
    stations_names_distances = geo.stations_by_distance(stations, (52.2053,0.1218))

    #prints the 10 stations that are closest to the coordinate
    print("CLOSEST 10 STATIONS:", stations_names_distances[:10])
    
    #prints the 10 stations that are furthest from the coordinate
    print("FURTHEST 10 STATIONS:", stations_names_distances[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
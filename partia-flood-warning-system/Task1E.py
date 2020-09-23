from floodsystem import geo
from floodsystem import stationdata

def run():
    #builds list of stations
    stations = stationdata.build_station_list(use_cache=True)

    #gets rivers with the 9 most stations
    top_rivers = geo.rivers_by_station_number(stations, 9)

    print(top_rivers)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
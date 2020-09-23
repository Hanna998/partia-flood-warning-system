"""Unit tests for the flood module"""
#imports
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from flood import stations_level_over_threshold
from flood import stations_highest_rel_level

#testing 2b
def test_stations_level_over_threshold():
    #we build a list of stations
    stations = build_station_list()
    stations_above_threshold = stations_level_over_threshold(stations, 1)
    #we check if all the stations in stations_above_threshold has greater water level then 1
    for station in stations_above_threshold:
        assert station[1] > 1
    print("It works!")

#testing 2c
def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    for N in [1, 10, 500]:
        flooded_stations = stations_highest_rel_level(stations, N)
        assert len(flooded_stations) == N
        assert flooded_stations[0][1] >= flooded_stations[-1][1]
    print("It works too!")


if __name__ == "__main__":
    print("*** Test 2C and 2B: CUED Part IA Flood Warning System ***")
    test_stations_highest_rel_level()
    test_stations_level_over_threshold()
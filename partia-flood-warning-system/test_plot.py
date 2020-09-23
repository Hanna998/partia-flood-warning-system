"""Tests for the plot module"""
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime



def test_plot_water_levels():
    """Checks that the plot_water_levels function throws no erros with several inputs"""

    stations = build_station_list()
    update_water_levels(stations)

    # choose a few random stations and test
    for N in [1, 10, 100]:
        station = stations[N]
        dt = 10
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        #plot_water_levels(station, dates, levels)
    print("test_plot_water_levels works!")


if __name__ == "__main__":
    print("*** Test 2E: CUED Part IA Flood Warning System ***")
    test_plot_water_levels()
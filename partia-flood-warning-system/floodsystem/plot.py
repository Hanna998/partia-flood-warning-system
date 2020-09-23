
import matplotlib.pyplot as plt
#import matplotlib.dates
from datetime import datetime, timedelta
import matplotlib
from .stationdata import build_station_list
import dateutil.parser
import floodsystem.geo
from analysis import polyfit
import numpy as np

#2F
def plot_water_level_with_fit(station, dates, levels, p):
    floats_dates = matplotlib.dates.date2num(dates) 
    plt.plot(floats_dates, levels, '.')
    dates1 = np.linspace(floats_dates[0], floats_dates[-1], 30)
    poly = polyfit(dates, levels, p)[0]
    plt.plot(dates1, poly(dates1 - floats_dates[0]))

    levels_min = station.typical_range[0]
    levels_max = station.typical_range[1]
    plt.axhline(y=levels_min, color = "r")
    plt.axhline(y=levels_max, color = "g")

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.show()
    print(poly(polyfit(dates, levels, p)[1]))



#Implement in a submodule plot a function that displays a plot (using Matplotlib) of 
"""This module contains functions which create plots of river level data"""
# the water level data against time for a station, and include on the plot lines for 
# the typical low and high levels. The axes should be labelled and use the station name 
# as the plot title. The function should have the signature:

def plot_water_levels(station, dates, levels):
    #t = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
    #     datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4),
    #     datetime(2017, 1, 5)]
    #level = [0.2, 0.7, 0.95, 0.92, 1.02, 0.91, 0.64]

    # Plot
    plt.plot(dates, levels, label="$water level$")
    # add lines of typical high and low
    #1.0 corresponds to a level at the typical high and a ratio of 0.0 corresponds to a level at the typical low
    plt.plot([dates[-1], dates[0]], [station.typical_range[0],
                                     station.typical_range[0]], color='g', label="$typical low$")
    plt.plot([dates[-1], dates[0]], [station.typical_range[1],
                                     station.typical_range[1]], color='r', label="$typical high$")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title("Station " + station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend(loc=2)  # move labels to upper left
    plt.show()
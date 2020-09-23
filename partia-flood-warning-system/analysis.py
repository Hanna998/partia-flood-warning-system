#imports
import numpy as np
import matplotlib
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def polyfit(dates, levels, p):
    "returns polynomial that estimate the shape of the correlation"
    floats_dates = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(floats_dates - floats_dates[0], levels, p)
    poly = np.poly1d(p_coeff)

    d0 = floats_dates[0]
    return poly, d0

def future_levels(dates, levels, p):
    'returns level for a date two days into the future'
    floats_dates = matplotlib.dates.date2num(dates)
    try:
        p_coeff = np.polyfit(floats_dates - floats_dates[0], levels, p)
    except:
        p_coeff = 0
    poly = np.poly1d(p_coeff)

    test_date = datetime.datetime.now() + datetime.timedelta(days=2)
    float_test_date = matplotlib.dates.date2num(test_date)

    return(poly(float_test_date-floats_dates[0]))
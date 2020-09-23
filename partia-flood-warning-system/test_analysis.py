import analysis
import numpy as np
import matplotlib.dates
import datetime
from dateutil.tz import tzutc

def test_analysis():
    #create dates and levels to a give a line
    dates = [datetime.datetime(2020, 2, 16, 15, 15, tzinfo=tzutc()), datetime.datetime(2020, 2, 16, 15, 0, tzinfo=tzutc()), datetime.datetime(2020, 2, 16, 14, 45, tzinfo=tzutc()), datetime.datetime(2020, 2, 16, 14, 30, tzinfo=tzutc())]
    levels = [0, 1, 2, 3]

    equation = analysis.polyfit(dates, levels, 1)[0]
    
    assert equation(0) == 2.235174934028805e-09
    assert equation(10) == -960.0000003553928

if __name__ == "__main__":
    print("*** test_analysis.py: CUED Part IA Flood Warning System ***")
    #test_analysis()
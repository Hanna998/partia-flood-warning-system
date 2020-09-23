# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}\n".format(self.typical_range)
        d += "   current water levels: {}\n".format(self.latest_level)
        return d


    def typical_range_consistent(self):
        #method that checks the typical high/low range data for consistency. 
        #typical range is a tuple. It is bad if none existent or typical range[0]<typical range [1]
        #inconsistent data=
        # (i) no data is available; or 
        # (ii) the reported typical high range is less than the reported typical low
        if self.typical_range==None:
            return False
        elif self.typical_range[0]<=self.typical_range[1]:
            return True
        else:
            return False
        #returns True if the data is consistent
        #returns False if the data is inconsistent or unavailable


    #Task 2B
    #Method of MonitoringStation
    def relative_water_level(self):
        if MonitoringStation.typical_range_consistent(self) == True:
            if self.latest_level != None:
                a= float((self.latest_level-self.typical_range[0])/(self.typical_range[1]-self.typical_range[0]))    
                #return latest_level/typical_range
                #i.e. a ratio of 1.0 corresponds to a level at the typical high and a ratio of 0.0 corresponds to a level at the typical low.
                return a
        else:
            return None
            #If the necessary data is not available or is inconsistent, the function should return None

            




#a function that, given a list of station objects, returns  
#a list of stations that have inconsistent data.
def inconsistent_typical_range_stations(stations):
    #list inconsistent data
    inconsistent=[]  #empty list
    for i in stations:
        if i.typical_range_consistent()==False:
            inconsistent.append(i)      #if station is inconsistent then adds it to the list
    return inconsistent
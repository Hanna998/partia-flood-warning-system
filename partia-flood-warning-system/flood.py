#Task 2B
#In the submodule flood, implement a function that returns a list of tuples, where each tuple holds (i) a station (object) 
#at which the latest relative water level is over tol and (ii) the relative water level at the station. 
#The returned list should be sorted by the relative level in descending order. 
#imports
from floodsystem.stationdata import *
from floodsystem.station import *

#stations is a list of MonitoringStation objects. 
#we create a tuple where each tuple holds (i) a station (object) 
#at which the latest relative water level is over tol and (ii) the relative water level at the station. 

def stations_level_over_threshold(stations, tol):
    update_water_levels(stations)
    names = list()
    levels = list()     
    for station in stations:       #station is a better iterative name then i since it is more descriptive
        if station.typical_range != None:
            station_range = station.typical_range[1]-station.typical_range[0]
            if station.latest_level != None:
                relative_level = float(station.latest_level/station_range)  #a is the relative water level of the station (object)
                if relative_level > tol:             # if the latest relative water level is over tol
                    names.append(station.name)    #we add the name of the station and the relative water level at the station              
                    levels.append(relative_level)            
            else:
                relative_level = 0 
        else:
            continue
    lst1 = list(zip(names, levels))
    return sorted(lst1,key=lambda x: x[1],reverse=True)
#Consider only stations with consistent typical low/high data.


#Task 2C
#Implement a function in the submodule flood that returns a list of the N stations (objects) at which the water level, 
# relative to the typical range, is highest. The list should be sorted in descending order by relative level.

def stations_highest_rel_level(stations, N):
    update_water_levels(stations)
    names = list()
    current_levels = list()
    for station in stations:
        if station.typical_range != None:
            levels_min = station.typical_range[0]
            levels_max = station.typical_range[1]
            range_levels = levels_max - levels_min

            if station.latest_level != None:
                relative_level = float(station.latest_level/range_levels)
            
                names.append(station.name)
                current_levels.append(relative_level)
            else:
                relative_level = 0
                names.append(station.name)
                current_levels.append(relative_level)
        else:
            continue
    
    stations_with_levels = list(zip(names, current_levels))
    stations_with_levels.sort(key=lambda x:x[1], reverse = True)

    return stations_with_levels[:N]

def stations_above_max_level(stations):
    update_water_levels(stations)
    names = list()
    levels = list()
    for station in stations:
        if station.typical_range != None:
            max_level = station.typical_range[1]
            if station.latest_level != None:
                if station.latest_level > max_level:
                    danger_level = station.latest_level - max_level
                    names.append(station.name)
                    levels.append(danger_level)
                else:
                    continue
            else:
                level = 0
                names.append(station.name)
                levels.append(level)
        else:
            continue

    immediate_danger = list(zip(names, levels))
    immediate_danger.sort(key=lambda x:x[1], reverse = True)

    return immediate_danger

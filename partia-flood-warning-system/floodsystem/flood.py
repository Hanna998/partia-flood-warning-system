#Task 2B
#In the submodule flood, implement a function that returns a list of tuples, where each tuple holds (i) a station (object) 
#at which the latest relative water level is over tol and (ii) the relative water level at the station. 
#The returned list should be sorted by the relative level in descending order. 
from stationdata import *
from floodsystem.station import *

#stations is a list of MonitoringStation objects. 
#we create a tuple where each tuple holds (i) a station (object) 
#at which the latest relative water level is over tol and (ii) the relative water level at the station. 

def stations_level_over_threshold(stations, tol):
    update_water_levels(stations)
    lst1 = []       #empty list
    for station in stations:        #station is a better iterative name then i since it is more descriptive
        try:
            a = float(MonitoringStation.relative_water_level(station))  #a is the relative water level of the station (object)
            if a > tol:             # if the latest relative water level is over tol
                lst1.append((station, a))       #we add the name of the station and the relative water level at the station
        except:                 #if the station has no relative water level data
            continue            #the iteration continues
        #if (i.latest_level>tol):
        #    station_over_tol.append(i)      #if the latest relative water level is over tol then adds it to the list
        #    station_over_tol.sort(reverse=True)      #sorting tuple by the relative level in descending order.
    return sorted(lst1,key=lambda x: x[1],reverse=True)

#Consider only stations with consistent typical low/high data.




#Task 2C
#Implement a function in the submodule flood that returns a list of the N stations (objects) at which the water level, 
# relative to the typical range, is highest. The list should be sorted in descending order by relative level.

def stations_highest_rel_level(stations, N):
    update_water_levels(stations)
    lst1 = [] #we create two empty lists here
    lst2 = []
    for station in stations:
        try:
            a = float((station.latest_level)/(station.typical_range[1]-station.typical_range[0] ))    
            #latest_level/typical_range
            lst1.append((station.name,a))
        except:
            continue
        lst2 = sorted(lst1, key=lambda x: x[1], reverse=True)         
        #sorting tuple by the relative level in descending order.
    return lst2[:N]   


    #    if (i.latest_level>tol):
    #        station_over_tol.append(i)      #if the latest relative water level is over tol then adds it to the list
    #        station_over_tol.sort(reverse=True)      #sorting tuple by the relative level in descending order.
    #return highest_water_level
#where stations is a list of MonitoringStation objects.

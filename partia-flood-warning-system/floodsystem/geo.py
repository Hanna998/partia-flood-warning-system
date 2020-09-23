# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit
from .utils import sorted_by_key  # noqa
from floodsystem import station
from collections import defaultdict

def stations_by_distance(stations, p):
    'build list of tuples (station, distance) where distance is the distance from a coordinate p'
    #Creates empty lists for station names, distances from the coordinate and towns
    stations_names = list()
    stations_distances = list()
    stations_towns = list()
    for station in stations:
        #gets the name, town and position of each station
        name = station.name
        town = station.town
        coord = station.coord
        #calculates the distance in kilometres of the station from p
        distance = haversine(coord, p, unit=Unit.KILOMETERS)
        #adds the name to the name list
        stations_names.append(name)
        #adds the distance to the distance list
        stations_distances.append(distance)
        #adds the town to the town list
        stations_towns.append(town)
    #makes the three lists into a list of tuples (name, town, distance)    
    stations_name_distance = zip(stations_names, stations_towns, stations_distances)
    #sorts the list by the distances of the stations from p
    return sorted_by_key(stations_name_distance, 2, reverse = False)

def stations_within_radius(stations, centre, r):
    'returns stations that are within a given radius of a centre point'
    #creates an empty list 
    radius_stations= list()
    for station in stations:
        #gets the name and position of each station
        name = station.name
        coord = station.coord
        #calculates the distance of the station from the centre coord
        distance = haversine(coord, centre, unit=Unit.KILOMETERS)
        if distance < r:
            #adds names of stations that are within a given radius of the centre to the list
            radius_stations.append(name)
        else:
            #ignores stations that are outside the radius
            pass
    return radius_stations

def rivers_with_station(stations):
    'returns a set of rivers that have at least one monitoring station'
    #rivers_list = list() -- test
    #creates an empty set - a set does not allow duplicates
    rivers = set()
    for station in stations:
        #gets the river for each station
        river = station.river
        #only runs below code if the station has a river
        if river != None:
            #adds rivers that have monitoring stations to the list
            rivers.add(river)
            #rivers_list.append(river) -- test
    #return len(rivers), len(rivers_list) -- test
        else:
            #if station does not have a river, ignore its
            pass
    return rivers

def stations_by_river(stations):
    'returns a dictionary of rivers matched with its monitoring stations'
    #creates a dictionary that has keys matched to lists using defaultdict
    rivers_dict = defaultdict(list)
    for station in stations:
        #gets the name and river for each station
        name = station.name
        river = station.river
        if river != None:
            #runs if the station has a river
            if river not in rivers_dict:
                #if the river is not already a key create a new key for that river
                rivers_dict[river] = []
                #add the name of the station to the list for that river
                rivers_dict[river].append(name)
            elif river in rivers_dict:
                #add the name of the station to the existing list of that river
                rivers_dict[river].append(name)
    return rivers_dict


def rivers_by_station_number(stations, N):
    "determines the N rivers with the greatest number of monitoring stations"
    #calls the previous function
    river_dict = stations_by_river(stations)
    #creates an empty list 
    rivers_to_num=[]
  
    for river, station in river_dict.items():
        rivers_to_num.append([river,len(station)])
    #adds tuples of river:number of corresponding stationsto the rivers_to_num

    rivers_to_num=sorted_by_key(rivers_to_num,1,reverse=True)
    #sorts the rivers in order of station numbers 

    rivers_stations = rivers_with_station(stations)
    number_rivers = len(rivers_stations) 

    #Checks if N is greater than the number of rivers - if it isn't, the list returned is just the 
    #whole list
    if number_rivers > N:
        #if the river after the Nth river has the same number of stations as the Nth river, N increases
        #to include that river as well - this continues until the number of stations of the next river
        #is no longer equal to the Nth one
        while rivers_to_num[N-1][1]==rivers_to_num[N][1]:
            N+=1
    else:
        #returns an array of the first N rivers with the most stations, including rivers that have the
        #same number of stations even if there are more than N rivers returned
        return rivers_to_num[0:N]
    
    #increases N such that the next return gives the right thing
    return rivers_to_num[0:N]

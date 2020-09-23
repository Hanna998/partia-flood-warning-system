# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

#Testing task 1F
def test_typical_range_consistent():       
    new_monitoring_station = MonitoringStation(None, None, None, None, [5, 0], None, None)    #this is inconsistent      #we instantiate a dummy monitoring station
    #print(new_monitoring_station.typical_range_consistent)
    assert new_monitoring_station.typical_range_consistent()==False     #asserting if inconsistent data is inconsistent
    
    new_monitoring_station2 = MonitoringStation(None, None, None, None, [0, 5], None, None)   #this is consistent        #checking for low < second
    #print(new_monitoring_station2.typical_range_consistent)
    assert new_monitoring_station2.typical_range_consistent()==True     #asserting if consistent data is consistent
  
    new_monitoring_station3 = MonitoringStation(None, None, None, None, None, None, None)   #this is inconsistent        #checking for None
    #print(new_monitoring_station3.typical_range_consistent)
    assert new_monitoring_station3.typical_range_consistent()==False     #asserting if no data is inconsistent

    new_monitoring_station4 = MonitoringStation(None, None, None, None, [5, 5], None, None)   #this is consistent        #checking for equality
    #print(new_monitoring_station4.typical_range_consistent)
    assert new_monitoring_station4.typical_range_consistent()==True     #asserting if equality is consistent

    print("it works")

def test_inconsistent_typical_range_stations():        
    #create some station data
    new_monitoring_station = MonitoringStation(None, None, None, None, [5, 0], None, None)
    new_monitoring_station2 = MonitoringStation(None, None, None, None, [0, 5], None, None)
    new_monitoring_station3 = MonitoringStation(None, None, None, None, None, None, None)
    new_monitoring_station4 = MonitoringStation(None, None, None, None, [5, 5], None, None)

    #create an empty list
    dummy_data=[]
    #add the station data to a list
    dummy_data.append(new_monitoring_station)
    dummy_data.append(new_monitoring_station2) 
    dummy_data.append(new_monitoring_station3)
    dummy_data.append(new_monitoring_station4)    

    print(inconsistent_typical_range_stations(dummy_data))

    assert inconsistent_typical_range_stations(dummy_data)==[new_monitoring_station,new_monitoring_station3]
    #check if inconsistent_typical_range_stations(dummy_data)
    print("it works too")
    
if __name__=="__main__":
    print("*** testing 1F: CUED Part IA Flood Warning System ***")
    test_typical_range_consistent()
    test_inconsistent_typical_range_stations()
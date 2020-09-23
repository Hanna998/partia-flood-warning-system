from floodsystem import geo
from floodsystem.station import MonitoringStation
from haversine import haversine, Unit

def test_geo():

# Create a station
    s_id = "test-s-id-1"
    m_id = "test-m-id-1"
    label = "Station X"
    coord = (-1.0,2.0)
    trange = (-2.0, 3.5)
    river = "River X"
    town = "Town X"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

#Create a second station
    s_id = "test-s-id-2"
    m_id = "test-m-id-2"
    label = "Station Y"
    coord = (-2.0,4.0)
    trange = (-4.0, 7.0)
    river = "River Y"
    town = "Town Y"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

#Create a third station with no river
    s_id = "test-s-id-2"
    m_id = "test-m-id-2"
    label = "Station Z"
    coord = (-3.0,5.0)
    trange = (-5.0, 8.0)
    town = "Town Z"
    river = None
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

#Create a fourth station with same river as second river
    s_id = "test-s-id-2"
    m_id = "test-m-id-2"
    label = "Station V"
    coord = (-6.0,10.0)
    trange = (-5.0, 8.0)
    river = "River Y"
    town = "Town V"
    s4 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

#Creates a list of the above four stations
    stations = (s1, s2, s3, s4)

#Returns a list of tuples of the four stations with their distances from the coordinate (-0.5, 0.5)
    stations_distance = geo.stations_by_distance(stations, (-0.5, 0.5))

#Checks the output is as expected
    assert stations_distance[0]==("Station X", "Town X", 175.80079981056087)
    assert stations_distance[1]==("Station Y", "Town Y", 423.32287103817487)
    assert stations_distance[2]==("Station Z", "Town Z", 572.1728231982844)
    assert stations_distance[3]==("Station V", "Town V", 1218.7887493406365)

#Returns a list of rivers within a radius of 200 from the coordinate (-0.5, 0.5)
    stations_radius = geo.stations_within_radius(stations, (-0.5, 0.5), 200)
#Checks the output is as expected - station X is the only one within range    
    assert stations_radius[0] == "Station X"

#gets a set of rivers with at least one monitoring station
    rivers_stations = sorted(geo.rivers_with_station(stations))

#checks the output is as expected - Station Z has no river and Station V has same river as Station Y
    assert rivers_stations == ["River X", "River Y"]

#returns a dictionary of the rivers matched with their stations
    stations_rivers = geo.stations_by_river(stations)

#checks the output is as expected
    assert stations_rivers == {"River X": ["Station X"], "River Y": ["Station Y", "Station V"]}

#Create a fifth station with a new river 
    s_id = "test-s-id-1"
    m_id = "test-m-id-1"
    label = "Station W"
    coord = (-1.0,2.0)
    trange = (-2.0, 3.5)
    river = "River W"
    town = "Town W"
    s5 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

#Create a sixth station with the same river as station X
    s_id = "test-s-id-1"
    m_id = "test-m-id-1"
    label = "Station A"
    coord = (-1.0,2.0)
    trange = (-2.0, 3.5)
    river = "River X"
    town = "Town A"
    s6 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    stations = (s1, s2, s3, s4, s5, s6)

#returns a list of the river with the greatest number of stations -- unless some of the other rivers
# also have the same number of stations, in which case they are also included 
    rivers_number_stations = geo.rivers_by_station_number(stations, 1)
    
#checks the output is correct
    assert rivers_number_stations == [["River X", 2], ["River Y", 2]]

#checks whether the list is just returned if the number of rivers is less than or equal to N --
#here the list of rivers with stations is 3, so trying to get the first 3 stations will be the entire
#list, hence we just return the whole list
    rivers_number_stations_2 = geo.rivers_by_station_number(stations, 4) #N is greater than number of rivers
    rivers_number_stations_3 = geo.rivers_by_station_number(stations, 3) #N is the same as the number of rivers

#checks the output is correct - i.e. the entire list of rivers with number of stations if N is greater
#or the same as the number of rivers
    assert rivers_number_stations_2 == [["River X", 2], ["River Y", 2], ["River W", 1]]
    assert rivers_number_stations_3 == [["River X", 2], ["River Y", 2], ["River W", 1]]

test_geo()


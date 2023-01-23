import matplotlib.pyplot as plt
from DataExtractor import *
from Stations import *
from Graph import *
from Dijkstra import *
from A_Star import *

stations_reader = Extractor("./_dataset/london.stations.csv")
connection_reader = Extractor("./_dataset/london.connections.csv")
station_datas = stations_reader.Extract()
station_datas.pop(0)
connection_datas = connection_reader.Extract()
connection_datas.pop(0)

station_id = []
station_latitude = []
station_longitude = []
station_name = []
station_display_name = []
station_zone = []
station_total_line = []
station_rail = []
station_ones = []
station_twos = []
station_lines = []

for i in range(0,len(station_datas)):
    station_id.append(int(station_datas[i][0]))
    station_latitude.append(float(station_datas[i][1]))
    station_longitude.append(float(station_datas[i][2]))
    station_name.append(station_datas[i][3])
    station_display_name.append(station_datas[i][4])
    station_zone.append(station_datas[i][5])
    station_total_line.append(station_datas[i][6])
    station_rail.append(station_datas[i][7])


for j in range(0,len(connection_datas)):
    station_ones.append(int(connection_datas[j][0]))
    station_twos.append(int(connection_datas[j][1]))
    station_lines.append(int(connection_datas[j][2]))

all_stations = stations(station_id,station_latitude,station_longitude,station_name,station_display_name,station_zone,station_total_line,station_rail)

london_map = graph(station_id,connection_datas)
map_stations, map_matrix, station_index = london_map.make_map()

A_star_alg = A_Star(london_map,all_stations)
A_star_path = A_star_alg.shortest_path(1,10)
print(A_star_path)
one2ten_path, one2ten_time = Dijkstra(map_stations, map_matrix, station_index, 1, 10)
print(one2ten_path)
print(one2ten_time)

plt.scatter(station_latitude, station_longitude, color = "g",s = 3)
line_index = 0
while (station_lines[line_index]) == 1:
    plt.plot([all_stations.get_station_location(station_ones[line_index])[0],all_stations.get_station_location(station_twos[line_index])[0]], 
    [all_stations.get_station_location(station_ones[line_index])[1],all_stations.get_station_location(station_twos[line_index])[1]],'#AE6017')
    line_index += 1
while (station_lines[line_index]) == 2:
    plt.plot([all_stations.get_station_location(station_ones[line_index])[0],all_stations.get_station_location(station_twos[line_index])[0]], 
    [all_stations.get_station_location(station_ones[line_index])[1],all_stations.get_station_location(station_twos[line_index])[1]],"#FFE02B")
    line_index += 1

for m in A_star_path:
    plt.plot([all_stations.get_station_location(m)[0],all_stations.get_station_location(m)[0]], 
    [all_stations.get_station_location(m)[1],all_stations.get_station_location(m)[1]],'#FFE02B')

for n in one2ten_path:
    plt.plot([all_stations.get_station_location(n)[0],all_stations.get_station_location(n)[0]], 
    [all_stations.get_station_location(n)[1],all_stations.get_station_location(n)[1]],'#FFE02B')

plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('London subway', fontsize = 20)
plt.show()
#print(london_map.connection_matrix)
#print(get_connected_stations(map_matrix, station_index,1))
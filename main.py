import matplotlib.pyplot as plt
from DataExtractor import *
from Stations import *
from Graph import *
from Dijkstra import *
from A_Star import *
from Week1_benchmark import *
from transprotation_island import *
def main():
    stations_reader = Extractor("./_dataset/london.stations.csv")
    connection_reader = Extractor("./_dataset/london.connections.csv")
    lines_reader = Extractor("./_dataset/london.lines.csv") 
    station_datas = stations_reader.Extract()
    station_datas.pop(0)
    connection_datas = connection_reader.Extract()
    connection_datas.pop(0)
    lines_datas = lines_reader.Extract()
    lines_datas.pop(0)
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

    line_numbers = []
    line_names = []
    line_colour = []
    line_stripe = []

    for i in range(0,len(station_datas)):
        station_id.append(int(station_datas[i][0]))
        station_latitude.append(float(station_datas[i][1]))
        station_longitude.append(float(station_datas[i][2]))
        station_name.append(station_datas[i][3])
        station_display_name.append(station_datas[i][4])
        station_zone.append(float(station_datas[i][5]))
        station_total_line.append(station_datas[i][6])
        station_rail.append(station_datas[i][7])


    for j in range(0,len(connection_datas)):
        station_ones.append(int(connection_datas[j][0]))
        station_twos.append(int(connection_datas[j][1]))
        station_lines.append(int(connection_datas[j][2]))

    for k in range(0,len(lines_datas)):
        line_numbers.append(int(connection_datas[k][0]))
        line_names.append(connection_datas[k][1])
        line_colour.append(connection_datas[k][2])
        line_stripe.append(connection_datas[k][3])

    all_stations = stations(station_id,station_latitude,station_longitude,station_name,station_display_name,station_zone,station_total_line,station_rail)

    london_map = graph(station_id,connection_datas)
    london_map.make_map()

    A_star_alg = A_Star(london_map,all_stations)
    A_star_path = A_star_alg.shortest_path(1,10)
    print("A* path is       ", A_star_path)
    Dijk_alg = Dijkstra(london_map)
    one2ten_path, one2ten_time = Dijk_alg.Dijkstra_shortest_path(84,186)
    print("Dijkstra path is ", one2ten_path)
    print(one2ten_time)
    
    plt.scatter(station_latitude, station_longitude, color = "g",s = 3)
    for i in line_numbers:
        for j in range(len(station_lines)):
            if station_lines[j] == i:
                plt.plot([all_stations.get_station_location(station_ones[j])[0],all_stations.get_station_location(station_twos[j])[0]], 
                [all_stations.get_station_location(station_ones[j])[1],all_stations.get_station_location(station_twos[j])[1]],"#AE6017")
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.title('London subway', fontsize = 20)
    plt.show()
    '''
    bench = benchmarking(map_stations,map_matrix,station_index,london_map,all_stations)
    bench.shortest_path_KPI_no_lane_change()
    bench.shortest_path_KPI_lane_change()
    bench.shortest_path_KPI_unexist_station()
    bench.shortest_path_KPI_start_end_same_station()
    bench.input_KPI_Ctype_Camount()
    bench.input_KPI_Wtype_Camount()
    bench.input_KPI_Ctype_Wamount()
    bench.input_KPI_Wtype_Wamount()
    '''
    islands = transport_islands(london_map,all_stations)
    zone1_islands = islands.find_islands_in_zone(1)
    island_connection = islands.islands_connections(1)
    print(island_connection)
    print("the islands in zone1 are: ", zone1_islands)

main()
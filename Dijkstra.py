from Graph import *
'''
def get_connected_station_distance(map_matrix,station_index,station1,station2):
    return map_matrix[station_index[station1]][station_index[station2]]

def get_connected_stations(map_matrix,station_index,station1):
    connected_stations = []
    index = 0
    for i in map_matrix[station_index[station1]]:
        if i != 0:
            connected_stations.append(list(station_index.keys())[list(station_index.values()).index(index)])
            index += 1
        else:
            index += 1
    return connected_stations
'''
class Dijkstra:
    def __init__(self,graph):
        self.graph = graph

    def Dijkstra_shortest_path(self,start_station,final_station):
        station_record = {} #dictionary with {node : [previous_nodes, distance]}
        unvisitied_station = []
        current_station = start_station

        for i in self.graph.existing_stations:
            station_record[i] = [[], float('inf')]
            unvisitied_station.append(i)
        station_record[current_station][1] = 0
        station_record[current_station][0].append(current_station)

        while unvisitied_station != []:
            neibor_stations = self.graph.get_connected_stations(current_station).copy()
            for i in neibor_stations:
                if ((self.graph.get_connected_station_distance(current_station,i) + station_record[current_station][1]) < station_record[i][1]):
                    station_record[i][1] = self.graph.get_connected_station_distance(current_station,i) + station_record[current_station][1]
                    station_record[i][0] = station_record[current_station][0].copy()
                    station_record[i][0].append(i)
            unvisitied_station.remove(current_station)
            if unvisitied_station != []:
                current_station = unvisitied_station[0]
            for i in unvisitied_station:
                if station_record[i][1] < station_record[current_station][1]:
                    current_station = i
        final_path = station_record[final_station][0].copy()
        final_path_length = station_record[final_station][1]
        return final_path, final_path_length
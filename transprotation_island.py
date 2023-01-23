from Graph import *
from Stations import *
from Dijkstra import *

class transport_islands:
    def __init__(self,graph,stations):
        self.graph = graph
        self.stations = stations
        self.transportation_zones = {}
        self.zones = []
        for i in range(len(self.stations.zone)):
            if self.stations.zone[i] not in self.zones:
                self.zones.append(self.stations.zone[i])
        for j in self.zones:
            self.transportation_zones[j] = []
        for k in range(len(self.stations.id)):
            self.transportation_zones[self.stations.zone[k]].append(self.stations.id[k])
    
    def find_neighbor_stations_in_zone(self,station_id):
        connected_statations_in_zone = []
        zone_number = self.stations.zone[self.stations.id.index(station_id)]
        neighbor_stations = self.graph.get_connected_stations(station_id)
        for i in neighbor_stations:
            if self.stations.zone[self.stations.id.index(i)] == zone_number:
                connected_statations_in_zone.append(i)
        return connected_statations_in_zone

    def find_connected_stations(self,connected_stations,current_station,station_visit_stat):
        station_visit_stat[current_station] = True
        connected_stations.append(current_station)
        for i in self.find_neighbor_stations_in_zone(current_station):
            if station_visit_stat[i] == False:
                connected_stations = self.find_connected_stations(connected_stations, i, station_visit_stat)
        return connected_stations
    
    def find_islands_in_zone(self,zone_number):
        visit_stat = {}
        islands = []
        for i in self.transportation_zones[zone_number]:
            visit_stat[i] = False
        for j in self.transportation_zones[zone_number]:
            if visit_stat[j] == False:
                connected_stations = []
                island = self.find_connected_stations(connected_stations, j, visit_stat)
                islands.append(island)
        return islands
                
    def islands_connections(self,zone_number):
        zone_islands = self.find_islands_in_zone(zone_number)
        if len(zone_islands) >= 2:
            Dijk_alg = Dijkstra(self.graph)
            all_island_connections = {}
            shortest_path, shortest_time = Dijk_alg.Dijkstra_shortest_path(zone_islands[0][0],zone_islands[1][0])
            for i in range(len(zone_islands)):
                for j in range(i+1,len(zone_islands)):
                    for m in zone_islands[i]:
                        for n in zone_islands[j]:
                            this_path, this_time = Dijk_alg.Dijkstra_shortest_path(m,n)
                            this_temp_path = this_path.copy()
                            this_temp_path.pop(0)
                            this_temp_path.pop(len(this_temp_path)-1)
                            temp_passed_zones = []
                            for station in this_temp_path:
                                if self.stations.zone[self.stations.id.index(station)] not in temp_passed_zones:
                                    temp_passed_zones.append(self.stations.zone[self.stations.id.index(station)])
                            if zone_number not in temp_passed_zones:
                                if this_time < shortest_time:
                                    shortest_time = this_time
                                    shortest_path = this_path.copy()
                                    passed_zones = temp_passed_zones.copy()
                                    all_island_connections["island"+str(i)+" to island"+str(j)] = passed_zones 
        return all_island_connections
class graph:
    def __init__(self,station_ids,conncections):
        self.station_ids = station_ids
        self.connections = conncections
        self.existing_stations = []
        self.map_matrix = []
        self.station_index = {}

    def is_connected(self,s1,s2):
        if (s1 in self.existing_stations and s2 in self.existing_stations):
            if (self.map_matrix[self.station_index[s1]][self.station_index[s2]] != 0) or (self.map_matrix[self.station_index[s2]][self.station_index[s1]] != 0):
                return True
        return False
    
    def get_connected_stations(self,station_id):
        connected_stations = []
        index = 0
        for i in self.map_matrix[self.station_index[station_id]]:
            if i != 0:
                connected_stations.append(list(self.station_index.keys())[list(self.station_index.values()).index(index)])
                index += 1
            else:
                index += 1
        return connected_stations
    
    def get_connected_station_distance(self,station1,station2):
        return self.map_matrix[self.station_index[station1]][self.station_index[station2]]

    def add_station(self,station_id):
        if (station_id not in self.existing_stations):
            self.existing_stations.append(station_id)
            for elements in self.map_matrix:
                elements.append(0)
            self.map_matrix.append([0]*(1+len(self.map_matrix)))
            self.station_index[station_id] = len(self.station_index)
    
    def add_connection(self,station1,station2,time):
        if self.is_connected(station1,station2):
            return
        else:
            self.map_matrix[self.station_index[station1]][self.station_index[station2]] = time
            self.map_matrix[self.station_index[station2]][self.station_index[station1]] = time

    def make_map(self):
        for i in self.station_ids:
            self.add_station(i)
        for j in self.connections:
            self.add_connection(int(j[0]),int(j[1]),int(j[3]))
        return self.existing_stations, self.map_matrix, self.station_index
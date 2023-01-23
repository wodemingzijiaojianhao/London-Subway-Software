import Graph, Stations, math

class A_Star:
    #line_info is an array consist of 3 sub-arrays, [station1, station2, line]. The order of the sub-array
    #has to be the same with the original csv file. The type for all of them has to be int.
    def __init__(self, graph, stations, line_info):
        self.graph = graph
        self.stations = stations
        self.line_info = line_info
        self.red_nodes = []
        self.green_nodes = []
        # Structure [previous_node, h_value, g_value, f_value]
        self.node_info = [0,0,0,0]*(len(self.graph.existing_stations)+1)

    # This method compute the adjacent node of an given node
    def adjacent_nodes(self, node_id):
        result = []
        for item in self.graph.existing_stations:
            if self.graph.is_connected(node_id, item):
                result.append(item)
        return result

    # This method compute the distance between two given stations
    def distance(self, node1, node2):
        location1 = self.stations.get_station_location(node1)
        location2 = self.stations.get_station_location(node2)
        result = abs(math.sqrt(math.pow(float(location2[0])-float(location1[0]),2)+math.pow(float(location2[1])-float(location1[1]),2)))
        return result

    # This method marks all green nodes adjacent to the given node
    def mark_green(self,node,known_distance,destination_node):
        adj = self.adjacent_nodes(node)
        for item in adj:
            if (item not in self.green_nodes) and (item not in self.red_nodes) and (item != destination_node):
                self.green_nodes.append(item)
                dist = self.distance(node, item)
                self.node_info[int(item)*4+0] = node
                self.node_info[int(item)*4+1] = self.distance(item, destination_node)
                self.node_info[int(item)*4+2] = known_distance+dist
                self.node_info[int(item)*4+3] = self.node_info[int(item)*4+1]+self.node_info[int(item)*4+2]
            elif item == destination_node:
                self.node_info[int(item)*4+0] = node
                return True
        return False
    
    # This method find the next red_node
    def next_node(self):
        min_node = 'not found'
        min_f = 10000.00
        for item in self.green_nodes:
            if self.node_info[int(item)*4+3] < min_f:
                min_node = item
                min_f = self.node_info[int(item)*4+3]
        return min_node

    # This method compute whether two nodes are on the same line. If yes, return the line number. 
    #If no, return 0
    def same_line(self,s1,s2):
        s1_lines = []
        s2_lines = []
        s_line = 0
        for i in range(0, len(self.line_info[0])):
            if int(s1) == self.line_info[0][i] or int(s1) == self.line_info[1][i]:
                s1_lines.append(self.line_info[2][i])
        for i in range(0, len(self.line_info[0])):
            if int(s2) == self.line_info[0][i] or int(s2) == self.line_info[1][i]:
                s2_lines.append(self.line_info[2][i])
        for item1 in s1_lines:
            for item2 in s2_lines:
                if item1 == item2:
                    s_line = item2
        return s_line

    # This method return the shortest path between two stations as a list of station numbers that draw 
    # the path.
    def shortest_path(self,s1,s2):
        if (s1 == s2):
            return [s1,s2]
        s_line = self.same_line(s1,s2)
        if s_line != 0:
            message = 'Same Line: Follow line '+str(s_line)
            return [message]
        result = []
        self.red_nodes.append(s1)
        current_node = s1
        self.mark_green(s1, 0, s2)
        while len(self.green_nodes) != 0:
            g = self.node_info[int(current_node)*4+2]
            if self.mark_green(current_node,g,s2):
                break
            nextNode = self.next_node()
            self.red_nodes.append(nextNode)
            self.green_nodes.remove(nextNode)
            current_node = nextNode
        result.append(s2)
        current_node = s2
        while self.node_info[int(current_node)*4] != 0:
            current_node = self.node_info[int(current_node)*4]
            result.append(current_node)
        result = list(reversed(result))
        self.red_nodes = []
        self.green_nodes = []
        # Structure [previous_node, h_value, g_value, f_value]
        self.node_info = [0,0,0,0]*(len(self.graph.existing_stations)+1)
        return result

# Test code if you need :)
"""        
gra = Graph.graph([],[])
gra.add_station('1')
gra.add_station('2')
gra.add_station('3')
gra.add_station('4')
gra.add_station('5')
gra.add_station('6')
gra.add_station('7')
gra.add_connection('1','2',1)
gra.add_connection('1','3',1)
gra.add_connection('1','6',1)
gra.add_connection('2','6',1)
gra.add_connection('2','3',1)
gra.add_connection('3','4',1)
gra.add_connection('3','5',1)
gra.add_connection('4','5',1)
gra.add_connection('6','7',1)
gra.add_connection('4','7',1)
stat = Stations.stations(['1','2','3','4','5','6','7'],[1,2,2,3,3,1,2],[1,2,1,3,1,4,3],[],[],[],[],[])
line_info = [[1,2,3,4,5,6,7],[2,1,4,3,6,5,7],[1,1,1,2,2,2,2]]
sample = A_Star(gra, stat, line_info)
#print(gra.is_connected('1','3'))
#print(sample.adjacent_nodes('3'))
#print(sample.distance('1','6'))
print(sample.shortest_path('7','3'))
print(sample.shortest_path('6','3'))
print(sample.shortest_path('7','7'))
"""
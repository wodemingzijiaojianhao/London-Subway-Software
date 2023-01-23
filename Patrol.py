import Graph, Stations, A_Star, math
class Patrol:
    def __init__(self, Graph, Stations, line_info):
        self.graph = Graph
        self.stations = Stations
        self.line_info = line_info
        self.algorithm = A_Star.A_Star(self.graph, self.stations, [[],[],[]])
    #This method compute the distance between two stations
    def distance(self, node1, node2):
        location1 = self.stations.get_station_location(node1)
        location2 = self.stations.get_station_location(node2)
        result = abs(math.sqrt(math.pow(float(location2[0])-float(location1[0]),2)+math.pow(float(location2[1])-float(location1[1]),2)))
        return result
    #This method get two arguments, the array of station numbers you want to patrol, and the station 
    # you want to start with
    def get_route(self, nodes, start_node):
        if start_node not in nodes:
            return ['The start node is not in patrolling nodes']
        elif len(nodes) == 0:
            return['The patrolling nodes is not provided.']
        elif len(nodes) == 1:
            return nodes
        station_name = []
        latitudes = []
        longitudes = []
        red_nodes = []
        green_nodes = []
        shortest_distance = 100000
        shortest_node = '0'
        distance = 0
        result = []
        for item in nodes:
            green_nodes.append(item)
            latitudes.append(float((self.stations.get_station_location(item))[0]))
            longitudes.append(float((self.stations.get_station_location(item))[1]))
        red_nodes.append(start_node)
        green_nodes.remove(start_node)
        while len(green_nodes) != 0:
            current_node = red_nodes[len(red_nodes)-1]
            for item in green_nodes:
                path = self.algorithm.shortest_path(current_node, item)
                for i in range (0, len(path)-1):
                    distance += self.distance(path[i], path[i+1])
                if distance < shortest_distance:
                    shortest_distance = distance
                    shortest_node = item
                distance = 0
            red_nodes.append(shortest_node)
            green_nodes.remove(shortest_node)
            shortest_distance = 100000
            shortest_node = '0'
        for i in range (0, len(red_nodes)-1):
            array = self.algorithm.shortest_path(red_nodes[i], red_nodes[i+1])
            if i != 0:
                array.pop(0)
            result += array
        return result

#Test code if you need :)        

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
sample = Patrol(gra, stat, line_info)
#print(gra.is_connected('1','3'))
#print(sample.adjacent_nodes('3'))
#print(sample.distance('1','6'))
print(sample.get_route(['8'], '8'))
"""
        


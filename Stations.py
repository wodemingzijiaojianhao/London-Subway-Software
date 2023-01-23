class stations:
    def __init__(self,id,latitude,longitude,name,display_name,zone,total_line,rail):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.display_name = display_name
        self.zone = zone
        self.total_line = total_line
        self.rail = rail

    def get_id(self):
        return self.id
    
    def get_station_location(self,station_id):
        index = self.id.index(station_id)
        location = [self.latitude[index],self.longitude[index]]
        return location
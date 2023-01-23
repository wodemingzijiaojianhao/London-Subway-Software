import csv
class Extractor:
    def __init__(self, filePath):
        self.filePath = filePath

    def Extract(self):
        Totaldata = []
        with open(self.filePath,'r') as csvfile:
                data = csv.reader(csvfile, delimiter = ',')
                for column in data:
                    Totaldata.append(column)
        return Totaldata

        
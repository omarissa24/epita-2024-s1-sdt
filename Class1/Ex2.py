import csv

class Station:
    def __init__(self, rank, network, name, number_of_users, connections, city, district):
        self.rank = rank
        self.network = network
        self.name = name
        self.number_of_users = number_of_users
        self.connections = connections # 5 connections split on ;
        self.city = city
        self.district = district

    def __str__(self):
        return f"Rank: {self.rank}, Network: {self.network}, Name: {self.name}, Number of users: {self.number_of_users}, Connections: {self.connections}, City: {self.city}, District: {self.district}"
    
    def __repr__(self):
        return f"Rank: {self.rank}, Network: {self.network}, Name: {self.name}, Number of users: {self.number_of_users}, Connections: {self.connections}, City: {self.city}, District: {self.district}"
    

def parse_row(row):
  rank = row[0]
  network = row[1]
  name = row[2]
  number_of_users = row[3]
  connections = row[4:9]
  connections = list(filter(None, connections))
  city = row[9]
  district = int(row[10]) if row[10] else None
  return Station(rank, network, name, number_of_users, connections, city, district)

with open('resources/csv/ratp.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=';')
  next(reader)  # Skip the first line
  
  stations = [parse_row(row) for row in reader]

  for station in stations:
    print(station)
    print()
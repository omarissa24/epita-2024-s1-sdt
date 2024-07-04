import json

JSON_FILE_PATH = 'resources/json/french-cities.json'

#     {
    #     "city": "Paris",
    #     "lat": "48.8566",
    #     "lng": "2.3522",
    #     "country": "France",
    #     "iso2": "FR",
    #     "admin_name": "\u00cele-de-France",
    #     "capital": "primary",
    #     "population": "11020000"
    # },

class City:
    def __init__(self, city, lat, lng, country, iso2, admin_name, capital, population):
        self.city = city
        self.lat = lat
        self.lng = lng
        self.country = country
        self.iso2 = iso2
        self.admin_name = admin_name
        self.capital = capital
        self.population = population

    def __str__(self):
        return f"City: {self.city}, Lat: {self.lat}, Lng: {self.lng}, Country: {self.country}, ISO2: {self.iso2}, Region: {self.admin_name}, Capital: {self.capital}, Population: {self.population}"
    
    def __repr__(self):
        return f"City: {self.city}, Lat: {self.lat}, Lng: {self.lng}, Country: {self.country}, ISO2: {self.iso2}, Region: {self.admin_name}, Capital: {self.capital}, Population: {self.population}"
    

def parse_row(row):
    city = row['city']
    lat = float(row['lat'])
    lng = float(row['lng'])
    country = row['country']
    iso2 = row['iso2']
    admin_name = row['admin_name']
    capital = row['capital']
    population = int(row['population']) if row['population'] else 0
    return City(city, lat, lng, country, iso2, admin_name, capital, population)

def get_num_cities_by_region(cities):
    regions = {}
    for city in cities:
        if city.admin_name in regions:
            regions[city.admin_name] += 1
        else:
            regions[city.admin_name] = 1
    return regions

def population_by_region(cities):
    regions = {}
    for city in cities:
        if city.admin_name in regions:
            regions[city.admin_name] += city.population
        else:
            regions[city.admin_name] = city.population
    return regions

with open(JSON_FILE_PATH) as jsonfile:
    cities = json.load(jsonfile)
    cities = [parse_row(row) for row in cities]

    print("Number of cities by region:\n")
    regions = get_num_cities_by_region(cities)
    print(regions)

    print("\nPopulation by region:\n")
    regions = population_by_region(cities)
    print(regions)
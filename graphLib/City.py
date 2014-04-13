'''
@author: Abel
'''
city_dic = {}
citiesInContinent = {}

''' City object holds all the information for a city/airport. 
    Each City object is stored in a City dictionary as a value
    for a key that holds the city's code. '''
class City(object):
    def __init__(self, code, name, country, continent, timezone, coordinates, population, region):
        self.code = code
        self.name = name
        self.country = country
        self.continent = continent
        self.timezone = timezone
        self.coordinates = coordinates
        self.population = population
        self.region = region
        self.flights = {}
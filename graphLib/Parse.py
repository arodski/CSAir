'''

@author: Abel
'''
import City
import json

class Parse(object):
    def __init__(self, data):
        self.parseMetros(data)
        self.parseRoutes(data)
        
    ''' Parse the data in JSON into a dictionary data structure.
    Every city object is inserted into a city dictionary with 
    the code being the key.'''    
    def parseMetros(self, data):
        for metro in data["metros"]:
            cityEntry = City.City(metro["code"], metro["name"], metro["country"], metro["continent"], 
                             metro["timezone"], metro["coordinates"], metro["population"], metro["region"])
            
            City.city_dic[metro["code"]] = cityEntry
            
            self.parseCitiesIntoContinents(metro["continent"], metro["name"])
    
    ''' Routes are parsed under the dictionary 
    flight, it holds the cities that are accessible via a single flight '''       
    def parseRoutes(self, data):
        for route in data["routes"]:
            departureCityCode = route["ports"][0]
            arrivalCityCode = route["ports"][1]
            distance = route["distance"]
            
            City.city_dic[departureCityCode].flights[arrivalCityCode] = distance
            City.city_dic[arrivalCityCode].flights[departureCityCode] = distance
    
    ''' Parse each city name into a 
    different dictionary that has key continents and holds cities
    located in the continent. ''' 
    def parseCitiesIntoContinents(self, continent, city):
        if continent == "Africa":
            City.citiesInContinent.setdefault(continent, []).append(city)
        elif continent == "Asia":
            City.citiesInContinent.setdefault(continent, []).append(city)
        elif continent == "Australia":
            City.citiesInContinent.setdefault(continent, []).append(city)
        elif continent == "Europe":
            City.citiesInContinent.setdefault(continent, []).append(city)
        elif continent == "North America":
            City.citiesInContinent.setdefault(continent, []).append(city)
        else:
            City.citiesInContinent.setdefault(continent, []).append(city)
            
    def saveToDisk(self):
        root = {}
        metros = []
        routes = []
        
        for city in City.city_dic.itervalues():
            cityDic = {}
            cityDic["code"] = city.code
            cityDic["name"] = city.name
            cityDic["country"] = city.country
            cityDic["continent"] = city.continent
            cityDic["timezone"] = city.timezone
            cityDic["coordinates"] = city.coordinates
            cityDic["population"] = city.population
            cityDic["region"] = city.region
            metros.append(cityDic)
            
            for destCity in city.flights:
                routeDic = {}
                distance = city.flights[destCity]
                routeDic["distance"] = distance
                routeDic["ports"] = [city.code, destCity]
                routes.append(routeDic)
            
        root["routes"] = routes
        root["metros"] = metros
            
        with open('saveFile.txt', 'w') as outfile:
            json.dump(root, outfile, sort_keys = True, indent = 4)
            
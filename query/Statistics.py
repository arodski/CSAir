'''

@author: Abel
'''
import graphLib.City
cityDic = graphLib.City.city_dic

""" Return the longest single flight in the network """
def longestFlight():
    longestDistance = 0
    longestFlight = []
    for city in cityDic.itervalues():
        for cityCode in city.flights.keys():
            if(city.flights[cityCode] > longestDistance):
                longestDistance = city.flights[cityCode]
                longestFlight = [city.name, cityCode, longestDistance]
    return longestFlight
       
""" Return the shortest single flight in the network """           
def shortestFlight():
    shortestDistance = 1000000
    shortestFlight = []
    for city in cityDic.itervalues():
        for cityCode in city.flights.keys():
            if(city.flights[cityCode] < shortestDistance):
                shortestDistance = city.flights[cityCode]
                shortestFlight = [city.name, cityCode, shortestDistance]
    return shortestFlight
   
""" Return the average distance of all the flights in the network """
def averageDistance():
    totalDistance = 0
    totalFlights = 0
    for city in cityDic.itervalues():
        for cityCode in city.flights.keys():
            totalDistance += city.flights[cityCode]
            totalFlights += 1
    return totalDistance / totalFlights
    
''' Return the biggest city served by CSAir '''
def biggestCity():
    biggestPopulation = 0
    biggestCity = []
    for city in cityDic.itervalues():
        if(city.population > biggestPopulation):
            biggestPopulation = city.population
            biggestCity = [city.name, biggestPopulation]
    return biggestCity
    
''' Return the smallest city served by CSAir '''
def smallestCity():
    smallestPopulation = 1000000
    smallestCity = []
        
    for city in cityDic.itervalues():
        if(city.population < smallestPopulation):
            smallestPopulation = city.population
            smallestCity = [city.name, smallestPopulation]
    return smallestCity
    
''' Return the average size of all the cities served by CSAir '''
def averageSizeCities():
    totalSize = 0
    totalCities = 0
        
    for city in cityDic.itervalues():
        totalSize += city.population
        totalCities += 1
    return totalSize / totalCities
    
''' Return a list of continents served by CSAir and which cities are in them '''
def citiesListContinents():
    return graphLib.City.citiesInContinent
    
''' Return a list of cities that have the most direct connections '''
def hubCities():
    connections = 0
    hubCities = []
    for city in cityDic.itervalues():
        if(len(city.flights) > connections):
            connections = len(city.flights)
            hubCities.append(city.name)
    return hubCities
    

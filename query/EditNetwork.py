'''
Created on Oct 3, 2013

@author: Abel
'''
import graphLib.City
cityDic = graphLib.City.city_dic

''' Take in a parameter that specifies the code
    of the city to be deleted from the dictionary.
    Next, iterate through every city's flights and
    delete the code if it exists as a route. '''
def removeCity(cityCode):
    del cityDic[cityCode]
        
    for city in cityDic.itervalues():
        for flightCode in city.flights.keys():
            if(flightCode == cityCode):
                del city.flights[flightCode]
                
''' Take in two parameters, one is the code for the
    city where the route begins, the second is holds
    the code for the city where the route ends. 
    Delete the path between the two cities. '''    
def removeRoute(cityCode, destCityCode):
    del cityDic[cityCode].flights[destCityCode]

''' Allows the user to enter in the information necessary
    to create a new airport in a city. Create a city object
    for the new airport and add it to the dictionary.'''    
def addCity():
    cityCoordinates = {}
    cityName = raw_input("Enter name of new city: ")
    cityCode = raw_input("Enter code of new city: ")
    cityCountry = raw_input("Enter country of new city: ")
    cityContinent = raw_input("Enter continent of new city: ")
    cityTimezone = int(raw_input("Enter timezone of new city: "))
            
    cityNorthSouthDir = raw_input("North or South Coordinate? ")
    cityNorthSouthValue = int(raw_input("Enter coordinate value: "))
    cityEastWestDir = raw_input("East or West Coordinate? ")
    cityEastWestValue = int(raw_input("Enter coordinate value: "))
    
    while (True):        
        cityPopulation = int(raw_input("Enter population of new city: "))
        if cityPopulation > 0:
            break
        
    cityRegion = int(raw_input("Enter region of new city: "))
            
    cityCoordinates[cityNorthSouthDir] = cityNorthSouthValue
    cityCoordinates[cityEastWestDir] = cityEastWestValue
        
    cityEntry = graphLib.City.City(cityCode, cityName, cityCountry, cityContinent, cityTimezone, cityCoordinates, cityPopulation, cityRegion)
    cityDic[cityCode] = cityEntry
    print "Added city " + cityName + " to network."

''' Given a code that holds the starting city for a route, 
    a city that represents the destination of the route, 
    and the distance between the two cities/airports, 
    add the new route to the dictionary for the city where
    the route begins.'''    
def addRoute(cityCode, newDestCity, distance):
    cityDic[cityCode].flights[newDestCity] = distance

''' Given a code for the city to be edited and a new population
    value, overwrite the current population for the city. '''    
def editPopulation(cityCode, newPopulation):
    cityDic[cityCode].population = newPopulation
    print cityDic[cityCode].name + "'s population has been changed to " + str(newPopulation)
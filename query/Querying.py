'''

@author: Abel
'''
import graphLib.City
cityDic = graphLib.City.city_dic

''' This class returns values for a specified city
    in the dictionary that is given by the code sent
    as a parameter to each get function '''
def getListOfCities():
    for k in cityDic.itervalues():
        print k.name
    
def getCode(cityCode):
    return cityCode
    
def getName(cityCode):
    return cityDic[cityCode].name
    
def getCountry(cityCode):
    return cityDic[cityCode].country
    
def getContinent(cityCode):
    return cityDic[cityCode].continent
    
def getTimeZone(cityCode):
    return cityDic[cityCode].timezone
    
def getLatLong(cityCode):
    return cityDic[cityCode].coordinates
    
def getPopulation(cityCode):
    return cityDic[cityCode].population
    
def getRegion(cityCode):
    return cityDic[cityCode].region
    
def getFlightsAvailable(cityCode):
    return cityDic[cityCode].flights
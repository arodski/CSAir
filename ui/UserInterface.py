'''

@author: Abel
'''
import json
import urllib2
import graphLib.Parse
import graphLib.City
import query.Statistics
import query.Querying
import query.EditNetwork
import query.RouteInfo

cityDic = graphLib.City.city_dic

url1 = "https://wiki.engr.illinois.edu/download/attachments/227740359/map_data.json?version=1&modificationDate=1377303775000"
url2 = "https://wiki.engr.illinois.edu/download/attachments/227740360/cmi_hub.json?version=1&modificationDate=1377303775000"

data = json.load(urllib2.urlopen(url1))
parseData = graphLib.Parse.Parse(data)
data = json.load(urllib2.urlopen(url2))
parseData = graphLib.Parse.Parse(data)

def main():   
    print "                   CSAir                       "
    print "-----------------------------------------------"
    checkUserInput()  

def showMainMenu():
    print ""
    print "                 Main Menu                     "
    print("Please Select a choice:")
    print("1 - Get list of cities CSAir flies to")
    print("2 - Get information about a City in the CSAir route network")
    print("3 - Show statistical information about CSAir's route network")
    print("4 - Edit Route Network")
    print("5 - Save Route Network to Disk")
    print("6 - Get Information About A Route")
    print("0 - Exit")
    
def showQueryMenu():
    print ""
    print("Please Select a choice:")
    print("1 - Code")
    print("2 - Country")
    print("3 - Continent")
    print("4 - Timezone")
    print("5 - Coordinates")
    print("6 - Population")
    print("7 - Region")
    print("8 - Flights")
    print("0 - Exit")
    
def showStatsMenu():
    print ""
    print("Please Select a choice:")
    print("1 - Longest Single Flight")
    print("2 - Shortest Single Flight")
    print("3 - Average Distance of All Flights")
    print("4 - Biggest City Population")
    print("5 - Smallest City Population")
    print("6 - Average Population of All Cities")
    print("7 - List of Continent and Cities in Them")
    print("8 - Hub City")
    print("0 - Exit")

def showEditNetworkMenu():
    print ""
    print("Please Select a choice")
    print("1 - Remove city")
    print("2 - Remove a route")
    print("3 - Add a city and all its information")
    print("4 - Add route to city")
    print("5 - Edit population")
    print("0 - Exit")
    
def showEditOrAdd():
    print ("")
    print ("Please Select A Choice: ")
    print ("1 - Edit Existing City")
    print ("2 - Add City to Network")
    print ("0 - Exit")
 
def getListCities():    
    print ""
    query.Querying.getListOfCities()
    raw_input("")
    return
    
def getCityInformation():
    queryCity = ""
    cityName = raw_input("Enter the name of the city you are interested in getting more info about: ")
    for city in graphLib.City.city_dic.values():
        if city.name == cityName:
            queryCity = city.code
            break
    else:
        print "Sorry CSAir doesn't fly to that location"
        return
    
    while (True): 
        showQueryMenu()
        print ""
        selection = raw_input("Selection: ")
                             
        if(selection == "1"):
            print "Code: " + query.Querying.getCode(queryCity)
            raw_input("")
        elif(selection == "2"):
            print "Country: " + query.Querying.getCountry(queryCity)
            raw_input("")
        elif(selection == "3"):
            print "Continent: " + query.Querying.getContinent(queryCity)
            raw_input("")
        elif(selection =="4"):
            print "Timezone: " + str(query.Querying.getTimeZone(queryCity))
            raw_input("")
        elif(selection =="5"):
            print "Coordinates: " + str(query.Querying.getLatLong(queryCity))
            raw_input("")
        elif(selection =="6"):
            print "Population: " + str(query.Querying.getPopulation(queryCity))
            raw_input("")
        elif(selection =="7"):
            print "Region: " + str(query.Querying.getRegion(queryCity))
            raw_input("")
        elif(selection == "8"):
            print "Flights Available: " + str(query.Querying.getFlightsAvailable(queryCity))
            raw_input("")
        elif(selection == "0"):
            break
        else:
            print("That's not an option. Select Again.")
            
def getStatsInformation():
    while(True):
        showStatsMenu()
        print""
        selection = raw_input("Selection: ")
        
        if(selection == "1"):
            print "Longest Flight: " + str(query.Statistics.longestFlight())
            raw_input("")
        elif(selection == "2"):
            print "Shortest Flight: " + str(query.Statistics.shortestFlight())
            raw_input("")
        elif(selection =="3"):
            print "Average Distance: " + str(query.Statistics.averageDistance())
            raw_input("")
        elif(selection =="4"):
            print "Biggest City: " + str(query.Statistics.biggestCity())
            raw_input("")
        elif(selection =="5"):
            print "Smallest City: " + str(query.Statistics.smallestCity())
            raw_input("")
        elif(selection =="6"):
            print "Average City Size: " + str(query.Statistics.averageSizeCities())
            raw_input("")
        elif(selection == "7"):
            print "Cities in Continents: " + str(query.Statistics.citiesListContinents())
            raw_input("")
        elif(selection == "8"):
            print "Hub Cities: " + ", ".join(query.Statistics.hubCities())
            raw_input("")
        elif(selection == "0"):
            break
        else:
            print ("That's not an option. Select Again.")

def getEditOrAdd():
    while (True):        
        showEditOrAdd()
        print ""
        selection = raw_input("Selection: ")
        if(selection == "1"):
            getEditNetwork()
        elif(selection == "2"):
            query.EditNetwork.addCity()
            raw_input("")
        elif(selection == "0"):
            break
           
def getEditNetwork():
    city = raw_input("Please enter the name of the city you are interested in editing: ")
    queryCity = checkValidCity(city)
    if queryCity == "":
        print "CSAir doesn't fly to that city"
        return
    
    while (True):
        showEditNetworkMenu()
        print ""
        selection = raw_input("Selection: ")
        
        if(selection == "1"):
            query.EditNetwork.removeCity(queryCity)
            print (city + " has been removed")
            raw_input("")
            break
        elif(selection == "2"):
            destCity = raw_input("Please enter name of destination to remove route to: ")
            arrivingCity = checkValidCity(destCity)
            if arrivingCity == "":
                print "CSAir doesn't fly to that city"
            elif checkRouteExists(queryCity, arrivingCity):
                query.EditNetwork.removeRoute(queryCity, arrivingCity)
                print "Removed route to " + destCity
                raw_input("")
            else:
                print "Flight not available to that city"
        elif(selection == "3"):
            newRouteCity = raw_input("Please enter name of city for new route: ")
            newRouteCode = checkValidCity(newRouteCity)
            if newRouteCode == "":
                print "CSAir doesn't fly to that city"
            else:
                newRouteDistance = int(raw_input("Please enter distance of new route: "))
                if newRouteDistance > 0:
                    query.EditNetwork.addRoute(queryCity, newRouteCode, newRouteDistance)
                    print "Flight has been added to " + newRouteCity
                    raw_input("")
                else:
                    print "Not a valid distance."
        elif(selection == "4"):
            newPopulation = int(raw_input("Enter new population: "))
            if newPopulation > 0:
                query.EditNetwork.editPopulation(queryCity, newPopulation)
                print "Changed population of " + city + " to " + str(newPopulation)
                raw_input("")
            else:
                print "Not a valid population."
        elif(selection == "0"):
            break
        else:
            print ("That's not an option. Select Again.")
            
def getRouteInformation():
    cityRoute = []
    city = raw_input("Enter city to begin route from: ")
    queryCity = checkValidCity(city)
    if queryCity == "":
        print "CSAir doesn't fly to that city"
        return
    cityRoute.append(queryCity)
    
    while (True):
        nextDest = raw_input("Enter next city for route (Enter 0 to finish): ")
        nextCity = checkValidCity(nextDest)
        if nextDest == "0":
            print cityRoute
            query.RouteInfo.getTotalDistance(cityRoute)
            query.RouteInfo.getTotalCost(cityRoute)
            query.RouteInfo.getTotalTime(cityRoute)
            raw_input("")
            break
        elif nextCity == "":
            print "Not a valid city, not added to list."
        else:
            if (checkRouteExists(cityRoute[len(cityRoute)-1], nextCity)):
                cityRoute.append(nextCity)
            else:
                print "No route exists between these two cities, not added to list."

def getSaveToDisk():
    parseData.saveToDisk()
    print "File has been saved"
            
def checkRouteExists(startingCity, endingCity):
    for route in cityDic[startingCity].flights.keys():
        if route == endingCity:
            return True
    return False

def checkValidCity(cityName):
    for code in graphLib.City.city_dic.values():
        if code.name == cityName:
            queryCity = code.code
            return queryCity
    else:
        return ""
         
def checkUserInput():
    while (True):
        showMainMenu()
        print ""
        selection = raw_input("Selection: ")
        
        if(selection == "1"):
            getListCities()
        elif(selection == "2"):
            getCityInformation()
        elif(selection == "3"):
            getStatsInformation()
        elif(selection == "4"):
            getEditOrAdd()
        elif(selection == "5"):
            getSaveToDisk()
        elif(selection == "6"):
            getRouteInformation()
        elif(selection == "0"):
            break;
        else:
            print("That's not an option. Select Again.")

if __name__ == '__main__':
    main()

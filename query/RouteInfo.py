'''
Created on Oct 4, 2013

@author: Abel
'''
import math
import graphLib.City
cityDic = graphLib.City.city_dic

ACCELERATION = 1406.25
TOP_VELOCITY = 750.0
FIRST_LEG_COST = 0.35
ACEL_TIME = 8/15.0

''' Take in a list of cities that has been confirmed to be
    a valid route. Calculate and print the total distance
    after traveling to every city. '''
def getTotalDistance(cityRouteList):
    totalDistance = 0
    for index in range(len(cityRouteList)-1):
        currentCity, nextCity = cityRouteList[index], cityRouteList[index+1]
        totalDistance += cityDic[currentCity].flights[nextCity]
    print "Total Distance is " + str(totalDistance)   
    return totalDistance 

''' Take in a list of cities that has been confirmed to be
    a valid route. Calculate and print the total cost to
    fly the route given by the list. The first lef of the flight
    will cost .35 per km and each additional leg will cost .05
    less per km. If leg of route becomes free, keep the cost free
    for the remainder of the route. '''
def getTotalCost(cityRouteList):
    totalCost = 0
    for index in range(len(cityRouteList)-1):
        currentCity, nextCity = cityRouteList[index], cityRouteList[index+1]
        distance = cityDic[currentCity].flights[nextCity]
        if index >= 7:
            break  
        totalCost += distance * (FIRST_LEG_COST - (index * .05))
    print "Total Cost is " + str(totalCost)
    return totalCost

''' Take in a list of cities that has been confirmed to be
    a valid route. Calculate and print the time it will take
    to travel the route. If flight is more than 400km, the jet
    accelerates from 0 to 750kph for the first 200km, then cruises
    at 750kph, then decelerates to 0kph during last 200km of flight.
    If flight is less than 400km, jet accelerates for first half of 
    flight and the decelerates for the second half. Layover is taken
    into account, layover is 2hrs if 1 outbound flight, 10 min less for
    outbound flight after that. '''
def getTotalTime(cityRouteList):
    totalTime = 0.0
    
    for i in range(len(cityRouteList)-1):
        currentCity, nextCity = cityRouteList[i], cityRouteList[i+1]
        distance = cityDic[currentCity].flights[nextCity]
        if distance >= 400:
            distanceTopVel = distance - 400.0
            time = distanceTopVel / TOP_VELOCITY
            totalTime += (ACEL_TIME * 2) + time
        else:
            halfFlightDistance = distance / 2.0
            time = math.sqrt((halfFlightDistance * 2.0) / ACCELERATION)
            totalTime += (time * 2.0)
        
        numOutboundFlights = len(cityDic[currentCity].flights)
        totalTime += (120 - ((numOutboundFlights-1) * 10)) / 60.0
    
    print "Total Time is " + str(totalTime) + " hours"
    return totalTime
    
def findShortestRoute(startCityCode, endCityCode):
    pass
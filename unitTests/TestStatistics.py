'''
Created on Oct 4, 2013

@author: Abel
'''
import unittest
import json
import urllib2
import graphLib.City
import graphLib.Parse
import query.Statistics
import query.EditNetwork

cityDic = graphLib.City.city_dic

class Test(unittest.TestCase):

    def setUp(self):
        url1 = "https://wiki.engr.illinois.edu/download/attachments/227740359/map_data.json?version=1&modificationDate=1377303775000"
        url2 = "https://wiki.engr.illinois.edu/download/attachments/227740360/cmi_hub.json?version=1&modificationDate=1377303775000"
        data = json.load(urllib2.urlopen(url1))
        graphLib.Parse.Parse(data)
        data = json.load(urllib2.urlopen(url2))
        graphLib.Parse.Parse(data)

    def test_longestFlight(self):
        flightList = []
        flightList.append(query.Statistics.longestFlight())
        self.assertTrue(int(flightList[0][2]) == 12051, "Default longest flight")
    
    def test_shortestFlight(self):
        flightList = []
        flightList.append(query.Statistics.shortestFlight())
        self.assertTrue(int(flightList[0][2]) == 132, "Default shortest flight chicago to champaign")
    
    def test_averageDistance(self):
        self.assertTrue(int(query.Statistics.averageDistance()) == 2183, "Default average distance")
    
    def test_biggestCity(self):
        flightList = []
        flightList.append(query.Statistics.biggestCity())
        self.assertTrue(int(flightList[0][1]) == 34000000, "Default biggest city Tokyo")
        query.EditNetwork.editPopulation("CHI", "34100000")
        
        newFlightList = []
        newFlightList.append(query.Statistics.biggestCity())
        self.assertTrue(int(newFlightList[0][1]) == 34100000, "Chicago new biggest city")
        pass
    
    def test_smallestCity(self):
        flightList = []
        flightList.append(query.Statistics.smallestCity())
        self.assertTrue(int(flightList[0][1]) == 226000, "Default smallest city champaign")
        pass
    
    def test_averageSizeCities(self):
        self.assertTrue(query.Statistics.averageSizeCities() == 11560018, "Default average size")
    
    def test_hubCities(self):
        flightList = []
        flightList.append(query.Statistics.hubCities())
        self.assertTrue((flightList[0][2]) == "Champaign", "Champaign is in hub list")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
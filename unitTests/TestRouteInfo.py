'''
Created on Oct 4, 2013

@author: Abel
'''
import unittest
import json
import urllib2
import graphLib.City
import graphLib.Parse
import query.RouteInfo
cityDic = graphLib.City.city_dic
routeList1 = ["PAR", "MIL", "IST", "MOW"]
routeList2 = ["CHI"]

class Test(unittest.TestCase):

    def setUp(self):
        url1 = "https://wiki.engr.illinois.edu/download/attachments/227740359/map_data.json?version=1&modificationDate=1377303775000"
        url2 = "https://wiki.engr.illinois.edu/download/attachments/227740360/cmi_hub.json?version=1&modificationDate=1377303775000"
        data = json.load(urllib2.urlopen(url1))
        graphLib.Parse.Parse(data)
        data = json.load(urllib2.urlopen(url2))
        graphLib.Parse.Parse(data)
        
    def test_getTotalDistance(self):
        totalDistance = int(query.RouteInfo.getTotalDistance(routeList1))
        self.assertTrue(totalDistance == 4071, "643 + 1665 + 1763")
    
    def test_getTotalCost(self):
        totalCost = float(query.RouteInfo.getTotalCost(routeList1))
        self.assertTrue(totalCost == 1165.3, ".35*643 + .3*1665 + .25*1763")
    
    def test_getTotalTime(self):
        totalTime = str(query.RouteInfo.getTotalTime(routeList1))
        self.assertTrue(totalTime == "11.1946666667", "16/5 * 33 + 80/6")  
        
    def test_getTotalDistanceOneCity(self):
        totalDistance = int(query.RouteInfo.getTotalDistance(routeList2))
        self.assertTrue(totalDistance == 0, "No cities to fly to.")
        
    def test_getTotalCostOneCity(self):
        totalCost = float(query.RouteInfo.getTotalCost(routeList2))
        self.assertTrue(totalCost == 0, "No cities to fly to.")
    
    def test_getTotalTimeOneCity(self):
        totalTime = int(query.RouteInfo.getTotalTime(routeList2))
        self.assertTrue(totalTime == 0, "No cities to fly to.")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
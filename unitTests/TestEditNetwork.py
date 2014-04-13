'''
Created on Oct 4, 2013

@author: Abel
'''
import unittest
import json
import urllib2
import graphLib.City
import query.EditNetwork
import graphLib.Parse
cityDic = graphLib.City.city_dic

class Test(unittest.TestCase):

    def setUp(self):
        url1 = "https://wiki.engr.illinois.edu/download/attachments/227740359/map_data.json?version=1&modificationDate=1377303775000"
        url2 = "https://wiki.engr.illinois.edu/download/attachments/227740360/cmi_hub.json?version=1&modificationDate=1377303775000"
        data = json.load(urllib2.urlopen(url1))
        graphLib.Parse.Parse(data)
        data = json.load(urllib2.urlopen(url2))
        graphLib.Parse.Parse(data)

    def test_RemoveCity(self):
        self.assertTrue("MIA" in cityDic, "MIA exists in dictionary")
        query.EditNetwork.removeCity("MIA")
        self.assertFalse("MIA" in cityDic, "MIA has been removed from dictionary")
    
    def test_RemoveRoute(self):
        self.assertTrue("LIM" in cityDic["MEX"].flights, "LIM exists in MEX")
        query.EditNetwork.removeRoute("MEX", "LIM")
        self.assertFalse("LIM" in cityDic["MEX"].flights, "LIM has been removed")
    
    def test_AddRoute(self):
        self.assertFalse("ESS" in cityDic["BOG"].flights, "ESS not a flight in BOG")
        query.EditNetwork.addRoute("BOG", "ESS", 20)
        self.assertTrue("ESS" in cityDic["BOG"].flights, "ESS is now a flight in BOG")
    
    def test_EditPopulation(self):
        self.assertFalse(int(cityDic["SCL"].population) == 10, "Population not equal to 10")
        query.EditNetwork.editPopulation("SCL", "10")
        self.assertEqual(int(cityDic["SCL"].population), 10, "Population changed")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
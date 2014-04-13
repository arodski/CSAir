'''
Created on Oct 4, 2013

@author: Abel
'''
import unittest
import json
import urllib2
import graphLib.City
import graphLib.Parse
import query.Querying
cityDic = graphLib.City.city_dic

class Test(unittest.TestCase):

    def setUp(self):
        url1 = "https://wiki.engr.illinois.edu/download/attachments/227740359/map_data.json?version=1&modificationDate=1377303775000"
        url2 = "https://wiki.engr.illinois.edu/download/attachments/227740360/cmi_hub.json?version=1&modificationDate=1377303775000"
        data = json.load(urllib2.urlopen(url1))
        graphLib.Parse.Parse(data)
        data = json.load(urllib2.urlopen(url2))
        graphLib.Parse.Parse(data)

    def test_getListOfCities(self):
        pass

    def test_getCode(self):
        self.assertEqual(str(query.Querying.getCode("LED")),"LED", "LED code returns itself, LED ")
        
    def test_getName(self):
        self.assertEqual(str(query.Querying.getName('WAS')), "Washington", "City name for WAS is Washington")
    
    def test_getCountry(self):
        self.assertEqual(str(query.Querying.getCountry("YYZ")), "CA", "Toronto is in CA")
        
    def test_getContinent(self):
        self.assertEqual(str(query.Querying.getContinent("MIA")), "North America", "Miami is in North America")
    
    def test_getTimeZone(self):
        self.assertEqual(int(query.Querying.getTimeZone("CHI")), -6)
                
    def test_getPopulation(self):
        self.assertEqual(int(query.Querying.getPopulation("LAX")), 17900000)
        
    def test_getRegion(self):
        self.assertEqual(int(query.Querying.getRegion("MNL")), 4, "Manila region is 4")      

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
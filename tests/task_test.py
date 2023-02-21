import unittest
from models.task import *

class TestTask(unittest.TestCase):

    def setUp(self):

        self.test1 = {
            "title":"Perform Testing",
            "description":"A test for the test",
            "user":"George", 
            "project":"Trenello",
            "completed":False
        }
        
        
        
    
    # @unittest.skip("delete this line to run the test")  
    def test_getting_title(self):
        result = get_title(self.test1)
        self.assertEqual("Perform Testing", result)
        
    # @unittest.skip("delete this line to run the test")     
    def test_getting_description(self):
        result = get_description(self.test1)
        self.assertEqual("A test for the test", result)
        
    # @unittest.skip("delete this line to run the test")     
    def test_getting_user(self):
        result = get_user(self.test1)
        self.assertEqual("George", result)
        
    # @unittest.skip("delete this line to run the test")     
    def test_getting_project(self):
        result = get_project(self.test1)
        self.assertEqual("Trenello", result)
        
    # @unittest.skip("delete this line to run the test")     
    def test_getting_completed(self):
        result = get_completed(self.test1)
        self.assertEqual(False, result)
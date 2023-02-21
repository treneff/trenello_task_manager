import unittest
from models.project import *

class TestProject(unittest.TestCase):

    def setUp(self):

        self.project1 = {
            "name":"Trenello"
        }
        
        
        
        
    # @unittest.skip("delete this line to run the test")  
    def test_getting_name(self):
        result = get_name(self.project1)
        self.assertEqual("Trenello", result)
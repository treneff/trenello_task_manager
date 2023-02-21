import unittest
from models.user import *

class TestUser(unittest.TestCase):

    def setUp(self):

        self.user1 = {
            "name":"George"
        }
        
        
        
        
    # @unittest.skip("delete this line to run the test")  
    def test_getting_name(self):
        result = get_name(self.user1)
        self.assertEqual("George", result)
        
import unittest
import requests
import json
from pdb import set_trace as st

class TestDatatype(unittest.TestCase):
    '''
    Tests inputs and ouputs ensuring they are the correct type.
    '''

    def test_strains_type(self):
        '''
        Tests that the strains route url response is a json object
        '''
        url = "http://127.0.0.1:5000/strains"
        response = requests.get(url)
        # st()

        self.assertIsInstance(response.json(), list)

    def test_strains_notnull(self):
        '''
        Tests that the strains route url response is not null
        '''
        url = "http://127.0.0.1:5000/strains"
        response = requests.get(url)
        # st()
        self.assertTrue(response.json())
        
    def test_output(self):
        pass

if __name__ == "__main__":
    # breakpoint()
    unittest.main()
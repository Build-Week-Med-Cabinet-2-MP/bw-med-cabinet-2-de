import unittest
import requests
import json
from pdb import set_trace as st


class TestDatatype(unittest.TestCase):
    '''
    Tests inputs and ouputs ensuring they are the correct type.
    '''
    def test_strains_response_type(self):
        '''
        Tests that the /strains route url response is a json object
        '''
        url = "http://127.0.0.1:5000/strains"
        response = requests.get(url)
        self.assertIsInstance(response.json(), list)

    def test_strains_response_notnull(self):
        '''
        Tests that the /strains route url response is not null
        '''
        url = "http://127.0.0.1:5000/strains"
        response = requests.get(url)
        self.assertTrue(response.json())

    def test_web_layout_strains_response_type(self):
        '''
        Tests that the /web_layout_strains route url response is a json object
        '''
        url = "http://127.0.0.1:5000/web_layout_strains"
        response = requests.get(url)
        self.assertIsInstance(response.json(), list)

    def test_web_layout_strains_response_notnull(self):
        '''
        Tests that the /web_layout_strains route url response is not null
        '''
        url = "http://127.0.0.1:5000/web_layout_strains"
        response = requests.get(url)
        self.assertTrue(response.json())

    def test_model_response_notnulle(self):
        '''
        Tests that the /model route url response is a json object
        '''
        json_request = {
            "Flavors": ["Blueberry", "Apple", "Skunk"],
            "Effects": ["Focused", "Happy", "Relaxed"]
        }
        url = "http://127.0.0.1:5000/model"
        response = requests.get(url, json=json_request)
        self.assertIsInstance(response.json(), list)

    def test_model_response_length(self):
        '''
        Tests that the /model route url response is a json object length is 3
        '''
        json_request = {
            "Flavors": ["Blueberry", "Apple", "Skunk"],
            "Effects": ["Focused", "Happy", "Relaxed"]
        }
        url = "http://127.0.0.1:5000/model"
        response = requests.get(url)
        self.assertEqual(len(response.json(), 3))


if __name__ == "__main__":
    # breakpoint()
    unittest.main()
import unittest
import requests
import json
from pdb import set_trace as st
from dotenv import load_dotenv
from os import environ as os_environ


# base_url = ""

# load_dotenv()
# _HEROKU_ENV = os_environ.get("_HEROKU_ENV")
# if _HEROKU_ENV == "yes":
#     "http://127.0.0.1:5000/"


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

    def test_model_response_notnull(self):
        '''
        Tests that the /model route json object is not null
        '''
        json_request = {
            "Flavors": ["Blueberry", "Apple", "Skunk"],
            "Effects": ["Focused", "Happy", "Relaxed"]
        }
        url = "http://127.0.0.1:5000/model"
        response = requests.post(url, json=json_request)
        self.assertIsInstance(response.json(), list)

    def test_flavor_length(self):
        '''
        Tests that the flavors are length 1 <= 3
        '''
        json_request = {
            "Flavors": ["Blueberry", "Apple", "Skunk"],
            "Effects": ["Focused", "Happy", "Relaxed"]
        }
        url = "http://127.0.0.1:5000/model"
        response = requests.post(url, json=json_request)
        
        # loop through the list of flavors
        for i in range(len(response.json())):
            self.assertTrue((len(response.json()[i]['Flavors']) >= 1) & (len(response.json()[i]['Flavors']) <= 3))

    def test_effect_length(self):
        '''
        Tests that the effects are length 1 <= 3
        '''
        json_request = {
            "Flavors": ["Blueberry", "Apple", "Skunk"],
            "Effects": ["Focused", "Happy", "Relaxed"]
        }
        url = "http://127.0.0.1:5000/model"
        response = requests.post(url, json=json_request)
        
        # loop through the list of effects
        for i in range(len(response.json())):
            self.assertTrue((len(response.json()[i]['Effects']) >= 1) & (len(response.json()[i]['Flavors']) <= 3))


if __name__ == "__main__":
    log_file = '_log_file.txt'
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
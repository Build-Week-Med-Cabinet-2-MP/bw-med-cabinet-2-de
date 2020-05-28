import unittest
import requests
import json

class TestData(unittest.TestCase):

    def test_url(self):
        url = "http://127.0.0.1:5000/strains"
        response = requests.get(url)
        self.assertIsInstance(response.json().to_dict(orient="records"), dict)

    def test_input(self):
        #self.assertIsInstance(self.json_input, json)
        pass
    def test_output(self):
        pass

if __name__ == "__main__":
    # breakpoint()
    unittest.main()
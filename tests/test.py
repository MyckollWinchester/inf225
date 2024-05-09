import unittest
import requests

class TestEndpoints(unittest.TestCase):
    valid_source_destination_request_data = None
    invalid_source_destination_request_data = None

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://localhost:8000/buscar-persona-en-db/?prompt="

        cls.valid_source_destination_request_data = {
            "source_easting": "https://cl.linkedin.com/in/paola-saffirio-022058195",
            "destination_easting": True,
            "source_northing": "https://cl.linkedin.com/in/luciaborquez",
            "destination_northing": False
        }

        cls.invalid_source_destination_request_data = {
            "source_easting": "",
            "destination_easting": "Err",
            "source_northing": "",
            "destination_northing": "Err"
        }

    @classmethod
    def tearDownClass(cls):
        del cls.valid_source_destination_request_data
        del cls.invalid_source_destination_request_data

    def test_existence(self):
        response = requests.get(self.base_url + self.valid_source_destination_request_data["source_easting"])

        self.assertEqual("true", response.text)

    def test_existence_invalid_prompt(self):
        response = requests.get(self.base_url + self.invalid_source_destination_request_data["source_easting"])

        self.assertEqual(400, response.status_code)

if __name__ == '__main__':
    unittest.main()
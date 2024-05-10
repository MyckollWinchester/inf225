import unittest
import requests

class TestEndpoints(unittest.TestCase):
    valid_marcador_tallerista_request_data = None
    valid_insumo_request_data = None
    invalid_request_data = None

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://localhost:8000/"

        cls.valid_marcador_tallerista_request_data = {
            "url_paola": "https://cl.linkedin.com/in/paola-saffirio-022058195",
            "url_daniela": "https://www.linkedin.com/in/daniela-sala-2b913964/",
        }

        cls.valid_insumo_request_data = {
            "insumo": "leche",
        }

        cls.invalid_request_data = {
            "url_vacio": "",
        }

    @classmethod
    def tearDownClass(cls):
        del cls.valid_marcador_tallerista_request_data
        del cls.valid_insumo_request_data
        del cls.invalid_request_data

    def test_marcadores_valid_prompt(self):
        response = requests.get(self.base_url + "buscar-persona-en-db/?prompt=" + self.valid_marcador_tallerista_request_data["url_paola"])
        self.assertEqual("true", response.text)

    def test_marcadores_invalid_prompt(self):
        response = requests.get(self.base_url + "buscar-persona-en-db/?prompt=" + self.invalid_request_data["url_vacio"])
        self.assertEqual(400, response.status_code)

    def test_buscar_insumo_valid_prompt(self):
        response = requests.get(self.base_url + "buscar-insumo/?prompt=" + self.valid_insumo_request_data["insumo"])
        self.assertEqual(200, response.status_code)

    def test_buscar_insumo_invalid_prompt(self):
        response = requests.get(self.base_url + "buscar-insumo/?prompt=" + self.invalid_request_data["url_vacio"])
        self.assertEqual(400, response.status_code)
    



if __name__ == '__main__':
    unittest.main()
import unittest
import requests

class TestEndpoints(unittest.TestCase):
    base_url = None
    valid_marcador_tallerista_request_data = None
    valid_insumo_request_data = None
    invalid_request_data = None
    valid_tallerista = None
    valid_dict_propuesta = None
    invalid_dict_propuesta = None
    valid_tallerista_description = None

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://localhost:8000/"

        cls.valid_tallerista = {
            "titulo": "Paola Saffirio - Tallerista de Arte Terapia - Proyecto Raices Temuco ...",
            "enlace": "https://cl.linkedin.com/in/paola-saffirio-022058195",
            "verificado": True,
            "foto_perfil": "https://media.licdn.com/dms/image/C4D03AQG0gfCLvXj-GQ/profile-displayphoto-shrink_800_800/0/1605754196259?e=2147483647&v=beta&t=NdqZsMbgrTrsfU0TOLztTZIiA71egMemdz-41gj8u34"
        }

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

        cls.valid_tallerista_description = {
            "prompt": "tallerista de arte"
        }

        cls.valid_dict_propuesta = {
            "nombre": "John",
            "apellidos": "Dou",
            "experiencia": "str",
            "correo": "str@test.cl",
            "telefono": "+56933665588",
            "linkedin": "str",
            "instagram": "str",
            "tiktok": "str",
            "nombre-taller": "str",
            "descripcion": "str",
            "modalidad": "online",
            "materiales": "str",
            "vacantes": 2,
            "sesiones": 5
        }

        cls.invalid_dict_propuesta = {
            "nombre": "John",
            "apellidos": "Dou",
            "experiencia": "str",
            "correo": "strtest.cl",
            "telefono": "+56933665588",
            "linkedin": "str",
            "instagram": "str",
            "tiktok": "str",
            "nombre-taller": "str",
            "descripcion": "str",
            "modalidad": "online",
            "materiales": "str",
            "vacantes": "2",
            "sesiones": 5
        }

    @classmethod
    def tearDownClass(cls):
        del cls.valid_marcador_tallerista_request_data
        del cls.valid_insumo_request_data
        del cls.invalid_request_data

    def test_talleristas(self):
        response = requests.get(self.base_url + "talleristas/")
        self.assertEqual(200, response.status_code)

    def test_verificar_tallerista_valid_prompt(self):
        requests.post(self.base_url + "marcar-tallerista/", json=self.valid_tallerista)
        response = requests.post(self.base_url + "verificar-tallerista/", json=self.valid_tallerista)
        self.assertEqual(200, response.status_code)

    def test_verificar_tallerista_invalid_prompt(self):
        requests.post(self.base_url + "desmarcar-tallerista/", json=self.valid_tallerista)
        response = requests.post(self.base_url + "verificar-tallerista/", json=self.valid_tallerista)
        self.assertEqual(404, response.status_code)

    def test_buscar_tallerista_valid_prompt(self):
        response = requests.get(self.base_url + "buscar-tallerista/?prompt=" + self.valid_tallerista_description["prompt"])
        self.assertEqual(200, response.status_code)

    def test_marcadores_valid_prompt(self):
        requests.post(self.base_url + "marcar-tallerista/", json=self.valid_tallerista)
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
    
    def test_marcar_tallerista_valid_prompt(self):
        requests.post(self.base_url + "desmarcar-tallerista/", json=self.valid_tallerista)
        response = requests.post(self.base_url + "marcar-tallerista/", json=self.valid_tallerista)
        self.assertEqual(200, response.status_code)

    def test_marcar_tallerista_invalid_prompt(self):
        requests.post(self.base_url + "marcar-tallerista/", json=self.valid_tallerista)
        response = requests.post(self.base_url + "marcar-tallerista/", json=self.valid_tallerista)
        self.assertEqual(409, response.status_code)

    def test_desmarcar_tallerista_valid_prompt(self):
        requests.post(self.base_url + "marcar-tallerista/", json=self.valid_tallerista)
        response = requests.post(self.base_url + "desmarcar-tallerista/", json=self.valid_tallerista)
        self.assertEqual(200, response.status_code)

    def test_desmarcar_tallerista_invalid_prompt(self):
        requests.post(self.base_url + "desmarcar-tallerista/", json=self.valid_tallerista)
        response = requests.post(self.base_url + "desmarcar-tallerista/", json=self.valid_tallerista)
        self.assertEqual(404, response.status_code)
    
    def test_propuestas_valid(self):
        response = requests.post(self.base_url + "propuestas/", json=self.valid_dict_propuesta)
        self.assertEqual(200, response.status_code)
    
    def test_propuestas_invalid(self):
        response = requests.post(self.base_url + "propuestas/", json=self.invalid_dict_propuesta)
        self.assertEqual(400, response.status_code)


if __name__ == '__main__':
    unittest.main()
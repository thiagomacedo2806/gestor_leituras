import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "manage")
django.setup()

from django.test import TestCase, Client
from leituras import Leitura

class LeiturasTestCase(TestCase):
    """
    Conjunto de testes automatizados para verificar as operações do Gestor de Leituras.
    """
    def setUp(self) -> None:
        self.client = Client()

    def test_fluxo_gerenciamento_leituras(self) -> None:
        payload = {
            "titulo": "O Programador Pragmático",
            "autor": "Andrew Hunt"
        }
        response_criar = self.client.post(
            "/criar/",
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(response_criar.status_code, 201)
        self.assertIn("id", response_criar.json())

        response_listar = self.client.get("/")
        self.assertEqual(response_listar.status_code, 200)
        leituras = response_listar.json()
        self.assertEqual(len(leituras), 1)
        self.assertEqual(leituras[0]["titulo"], "O Programador Pragmático")

        response_invalido = self.client.post(
            "/criar/",
            data=json.dumps({"autor": "Sem titulo"}),
            content_type="application/json"
        )
        self.assertEqual(response_invalido.status_code, 400)
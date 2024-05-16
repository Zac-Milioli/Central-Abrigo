import sys
import os
import unittest
from flask import Flask, request, jsonify, render_template

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.routes.routes import Routes

class TestRoutes(unittest.TestCase):
    """
    Testes unitários para as rotas do aplicativo.

    Testa as funcionalidades CRUD das rotas /abrigo e /estoque.
    """

    def setUp(self):
        """
        Configuração inicial para os testes.
        """
        self.app = Flask(__name__)
        self.routes = Routes()
        self.app.register_blueprint(self.routes.app)

        self.client = self.app.test_client()

    def test_create_abrigo(self):
        """
        Testa a criação de um novo abrigo.
        """
        data = {
            "endereco": "Rua das Flores",
            "nome_responsavel": "João",
            "cpf_responsavel": "12345678901",
            "telefone_responsavel": "999999999",
            "email": "joao@example.com",
            "ocupacao_maxima": 10,
            "ocupacao_animais": 5,
            "feminino": True
        }
        response = self.client.post('/abrigo', json=data)
        self.assertEqual(response.status_code, 201)

    def test_read_abrigo(self):
        """
        Testa a leitura de um abrigo existente.
        """
        response = self.client.get('/abrigo/1')
        self.assertEqual(response.status_code, 200)

    def test_update_abrigo(self):
        """
        Testa a atualização de um abrigo existente.
        """
        data = {
            "endereco": "Nova Rua",
            "nome_responsavel": "Maria",
            "cpf_responsavel": "98765432101",
            "telefone_responsavel": "888888888",
            "email": "maria@example.com",
            "ocupacao_maxima": 20,
            "ocupacao_animais": 8,
            "feminino": False
        }
        response = self.client.put('/abrigo/1', json=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_abrigo(self):
        """
        Testa a exclusão de um abrigo existente.
        """
        response = self.client.delete('/abrigo/1')
        self.assertEqual(response.status_code, 200)

    def test_create_produto(self):
        """
        Testa a criação de um novo produto no estoque.
        """
        data = {
            "id_abrigo": 1,
            "id_produto": 1,
            "descricao_produto": "Comida"
        }
        response = self.client.post('/estoque', json=data)
        self.assertEqual(response.status_code, 201)

    def test_read_produto(self):
        """
        Testa a leitura de um produto existente no estoque.
        """
        response = self.client.get('/estoque/1')
        self.assertEqual(response.status_code, 200)

    def test_update_produto(self):
        """
        Testa a atualização de um produto existente no estoque.
        """
        data = {
            "id_abrigo": 2,
            "id_produto": 2,
            "descricao_produto": "Remédio"
        }
        response = self.client.put('/estoque/1', json=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_produto(self):
        """
        Testa a exclusão de um produto existente no estoque.
        """
        response = self.client.delete('/estoque/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
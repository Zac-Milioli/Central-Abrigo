import sys
import os
import unittest

# Importa os módulos necessários para execução dos testes unitários.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.obj.abrigo import Abrigo

class TestAbrigo(unittest.TestCase):
    """
    Classe de teste para os métodos da classe Abrigo.

    Testes unitários para as funções de formatação de dados da classe Abrigo.
    """

    def test_format_for_database_with_id(self):
        """
        Verifica o método format_for_database quando um id_abrigo é fornecido.
        """
        abrigo = Abrigo(endereco='Rua Teste 123', nome_responsavel='João', cpf_responsavel='123.456.789-00', telefone_responsavel='(00) 1234-5678', email='joao@example.com', ocupacao_maxima=20, ocupacao_animais=10, feminino=True)
        expected_output = ('Rua Teste 123', 'João', '123.456.789-00', '(00) 1234-5678', 'joao@example.com', 20, 10, True, 1)
        self.assertEqual(abrigo.format_for_database(id_abrigo=1), expected_output)

    def test_format_for_database_without_id(self):
        """
        Verifica o método format_for_database quando nenhum id_abrigo é fornecido.
        """
        abrigo = Abrigo(endereco='Rua Teste 456', nome_responsavel='Maria', cpf_responsavel='987.654.321-00', telefone_responsavel='(00) 9876-5432', email='maria@example.com', ocupacao_maxima=30, ocupacao_animais=15, feminino=False)
        expected_output = ('Rua Teste 456', 'Maria', '987.654.321-00', '(00) 9876-5432', 'maria@example.com', 30, 15, False)
        self.assertEqual(abrigo.format_for_database(), expected_output)

if __name__ == '__main__':
    unittest.main()
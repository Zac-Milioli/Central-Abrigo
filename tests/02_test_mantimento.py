import sys
import os
import unittest

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Agora é seguro importar a classe Mantimento
from utils.obj.mantimento import Mantimento

class TestMantimento(unittest.TestCase):
    """
    Classe de teste para testar os métodos da classe Mantimento.

    Esta classe define métodos de teste para as funções da classe Mantimento
    que formatam os dados para serem inseridos em um banco de dados.
    """

    def test_format_for_database_with_id(self):
        """
        Testa o método format_for_database quando um id_estoque é fornecido.

        Este teste verifica se o método format_for_database da classe Mantimento
        retorna a tupla correta quando um id_estoque é fornecido.
        """
        mantimento = Mantimento(id_abrigo=1, id_produto=2, descricao_produto='Ração para Cães')
        expected_output = (1, 2, 'Ração para Cães', 1)
        self.assertEqual(mantimento.format_for_database(id_estoque=1), expected_output)

    def test_format_for_database_without_id(self):
        """
        Testa o método format_for_database quando nenhum id_estoque é fornecido.

        Este teste verifica se o método format_for_database da classe Mantimento
        retorna a tupla correta quando nenhum id_estoque é fornecido.
        """
        mantimento = Mantimento(id_abrigo=1, id_produto=2, descricao_produto='Ração para Gatos')
        expected_output = (1, 2, 'Ração para Gatos')
        self.assertEqual(mantimento.format_for_database(), expected_output)

if __name__ == '__main__':
    unittest.main()
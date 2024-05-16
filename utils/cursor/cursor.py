import sqlite3

class Cursor(sqlite3):
    def __init__(self, **args):
        super().__init__(**args)
        connection = sqlite3.connect(r'db/live_peixe.sql')
        self.cursor = connection.cursor()

    def insert_abrigo(self, values):
        query = f"INSERT INTO abrigo (endereco, nome_responsavel, cpf_responsavel, telefone_responsavel, email, ocupacao_maxima, ocupacao_animais, feminino) VALUES {values}"
        self.cursor.execute(query)

    def get_abrigo(self, id):
        query = f"SELECT * FROM abrigo WHERE id_abrigo = {id}"
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def update_abrigo(self, values):
        query = "UPDATE abrigo SET endereco = %s, nome_responsavel = %s, cpf_responsavel = %s, telefone_responsavel = %s, email = %s, ocupacao_maxima = %s, ocupacao_animais = %s, feminino = %s WHERE id_abrigo = %s"
        self.cursor.execute(query, values)
        return self.cursor.rowcount

    def delete_abrigo(self, id):
        query = f"DELETE FROM abrigo WHERE id_abrigo = {id}"
        self.cursor.execute(query)
        return self.cursor.rowcount

    def insert_mantimento(self, values):
        query = f"INSERT INTO estoque (id_abrigo, id_produto, descricao_produto) VALUES {values}"
        self.cursor.execute(query)

    def get_mantimento(self, id):
        query = f"SELECT * FROM estoque WHERE id_estoque = {id}"
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def update_mantimento(self, values):
        query = "UPDATE estoque SET id_abrigo = %s, id_produto = %s, descricao_produto = %s WHERE id_estoque = %s"
        self.cursor.execute(query, values)
        return self.cursor.rowcount

    def delete_mantimento(self, id):
        query = f"DELETE FROM estoque WHERE id_estoque = {id}"
        self.cursor.execute(query)
        return self.cursor.rowcount

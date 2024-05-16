import mysql.connector

class Cursor:
    def __init__(self, host='localhost', user='root', password='jogo21', database='live_peixe'):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as e:
            print("Erro ao conectar ao banco de dados MySQL:", e)

    def insert_abrigo(self, values):
        query = "INSERT INTO abrigo (endereco, nome_responsavel, cpf_responsavel, telefone_responsavel, email, ocupacao_maxima, ocupacao_animais, feminino) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_abrigo(self, id):
        query = "SELECT * FROM abrigo WHERE id_abrigo = %s"
        self.cursor.execute(query, (id,))
        return self.cursor.fetchone()

    def update_abrigo(self, values):
        query = "UPDATE abrigo SET endereco = %s, nome_responsavel = %s, cpf_responsavel = %s, telefone_responsavel = %s, email = %s, ocupacao_maxima = %s, ocupacao_animais = %s, feminino = %s WHERE id_abrigo = %s"
        self.cursor.execute(query, values)
        self.connection.commit()
        return self.cursor.rowcount

    def delete_abrigo(self, id):
        query = "DELETE FROM abrigo WHERE id_abrigo = %s"
        self.cursor.execute(query, (id,))
        self.connection.commit()
        return self.cursor.rowcount

    def insert_mantimento(self, values):
        query = "INSERT INTO estoque (id_abrigo, id_produto, descricao_produto) VALUES (%s, %s, %s)"
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_mantimento(self, id):
        query = "SELECT * FROM estoque WHERE id_estoque = %s"
        self.cursor.execute(query, (id,))
        return self.cursor.fetchone()

    def update_mantimento(self, values):
        query = "UPDATE estoque SET id_abrigo = %s, id_produto = %s, descricao_produto = %s WHERE id_estoque = %s"
        self.cursor.execute(query, values)
        self.connection.commit()
        return self.cursor.rowcount

    def delete_mantimento(self, id):
        query = "DELETE FROM estoque WHERE id_estoque = %s"
        self.cursor.execute(query, (id,))
        self.connection.commit()
        return self.cursor.rowcount

    def __del__(self):
        self.connection.close()

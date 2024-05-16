from flask import Flask, request, jsonify, render_template
from utils.cursor.cursor import Cursor
from utils.obj.abrigo import Abrigo
from utils.obj.mantimento import Mantimento


class Routes():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def main_page(self):
        self.cursor = Cursor()
        return render_template('teste')


    @app.route('/abrigo', methods=['POST'])
    def create_abrigo(self):
        data = request.get_json()
        try:
            abrigo = Abrigo(endereco=data['endereco'], nome_responsavel=data['nome_responsavel'], cpf_responsavel=data['cpf_responsavel'],
                            telefone_responsavel=data['telefone_responsavel'], email=data['email'], ocupacao_maxima=data['ocupacao_maxima'], 
                            ocupacao_animais=data['ocupacao_animais'], feminino=data['feminino'])
            # Insira o novo abrigo no banco de dados
            query = f"INSERT INTO abrigo (endereco, nome_responsavel, cpf_responsavel, telefone_responsavel, email, ocupacao_maxima, ocupacao_animais, feminino) VALUES {abrigo.format_for_database()}"
            self.cursor.execute(query)
            return jsonify({"message": "Abrigo criado com sucesso!"}), 201
        except:
            return jsonify({"message": "Erro ao criar abrigo"}), 500
    

    @app.route('/abrigo/<int:id_abrigo>', methods=['GET'])
    def read_abrigo(self, id_abrigo):
        # Busque o abrigo pelo ID no banco de dados
        query = f"SELECT * FROM abrigo WHERE id_abrigo = {id_abrigo}"
        self.cursor.execute(query)
        abrigo = self.cursor.fetchone()
        if abrigo:
            return jsonify({
                "endereco": abrigo[1],
                "nome_responsavel": abrigo[2],
                "cpf_responsavel": abrigo[3],
                "telefone_responsavel": abrigo[4],
                "email": abrigo[5],
                "ocupacao_maxima": abrigo[6],
                "ocupacao_animais": abrigo[7],
                "feminino": abrigo[8]
            })
        else:
            return jsonify({"message": "Abrigo não encontrado."}), 404
        

    @app.route('/abrigo/<int:id_abrigo>', methods=['PUT'])
    def update_abrigo(self, id_abrigo):
        data = request.get_json()
        abrigo = Abrigo(endereco=data['endereco'], nome_responsavel=data['nome_responsavel'], cpf_responsavel=data['cpf_responsavel'],
                telefone_responsavel=data['telefone_responsavel'], email=data['email'], ocupacao_maxima=data['ocupacao_maxima'], 
                ocupacao_animais=data['ocupacao_animais'], feminino=data['feminino'])
        # Atualize o abrigo no banco de dados
        query = "UPDATE abrigo SET endereco = %s, nome_responsavel = %s, cpf_responsavel = %s, telefone_responsavel = %s, email = %s, ocupacao_maxima = %s, ocupacao_animais = %s, feminino = %s WHERE id_abrigo = %s"
        self.cursor.execute(query, abrigo.format_for_database(id_abrigo=id_abrigo))
        
        if self.cursor.rowcount > 0:
            return jsonify({"message": "Abrigo atualizado com sucesso!"}), 200
        else:
            return jsonify({"message": "Abrigo não encontrado."}), 404
        

    @app.route('/abrigo/<int:id_abrigo>', methods=['DELETE'])
    def delete_abrigo(self, id_abrigo):
        # Delete o abrigo do banco de dados
        query = "DELETE FROM abrigo WHERE id_abrigo = %s"
        self.cursor.execute(query, id_abrigo)
        if self.cursor.rowcount > 0:
            return jsonify({"message": "Abrigo deletado com sucesso!"}), 200
        else:
            return jsonify({"message": "Abrigo não encontrado."}), 404
        

    @app.route('/estoque', methods=['POST'])
    def create_produto(self):
        data = request.get_json()
        try:
            mantimento = Mantimento(id_abrigo=data['id_abrigo'], id_produto=data['id_produto'], descricao_produto=data['descricao_produto'])
            # Insira o novo produto no estoque no banco de dados
            query = f"INSERT INTO estoque (id_abrigo, id_produto, descricao_produto) VALUES {mantimento.format_for_database()}"
            self.cursor.execute(query)
            return jsonify({"message": "Produto adicionado ao estoque com sucesso!"}), 201
        except:
            return jsonify({"message": "Falha ao adicionar produto ao estoque"}), 500
            

    @app.route('/estoque/<int:id_estoque>', methods=['GET'])
    def read_produto(self, id_estoque):
        # Busque o produto pelo ID no banco de dados
        query = f"SELECT * FROM estoque WHERE id_estoque = {id_estoque}"
        self.cursor.execute(query)
        produto = self.cursor.fetchone()
        if produto:
            return jsonify({
                "id_abrigo": produto[1],
                "id_produto": produto[2],
                "descricao_produto": produto[3]
            })
        else:
            return jsonify({"message": "Produto não encontrado."}), 404


    @app.route('/estoque/<int:id_estoque>', methods=['PUT'])
    def update_produto(self, id_estoque):
        data = request.get_json()
        mantimento = Mantimento(id_abrigo=data['id_abrigo'], id_produto=data['id_produto'], descricao_produto=data['descricao_produto'])
        # Atualize o produto no estoque no banco de dados
        query = "UPDATE estoque SET id_abrigo = %s, id_produto = %s, descricao_produto = %s WHERE id_estoque = %s"
        self.cursor.execute(query, mantimento.format_for_database(id_estoque=id_estoque))
        
        if self.cursor.rowcount > 0:
            return jsonify({"message": "Produto atualizado com sucesso!"}), 200
        else:
            return jsonify({"message": "Produto não encontrado."}), 404
        

    @app.route('/estoque/<int:id_estoque>', methods=['DELETE'])
    def delete_produto(self, id_estoque):
        # Delete o produto do estoque do banco de dados
        query = "DELETE FROM estoque WHERE id_estoque = %s"
        self.cursor.execute(query, id_estoque)
        if self.cursor.rowcount > 0:
            return jsonify({"message": "Produto deletado do estoque com sucesso!"}), 200
        else:
            return jsonify({"message": "Produto não encontrado."}), 404
from flask import Flask, request, jsonify
from utils.cursor.cursor import Cursor
from utils.obj.abrigo import *
from utils.obj.mantimento import *

cursor = Cursor()
app = Flask(__name__)

class Routes():

    @app.route('/abrigo', methods=['POST'])
    def create_abrigo():
        data = request.get_json()
        try:
            abrigo = Abrigo(endereco=data['endereco'], nome_responsavel=data['nome_responsavel'], cpf_responsavel=data['cpf_responsavel'],
                            telefone_responsavel=data['telefone_responsavel'], email=data['email'], ocupacao_maxima=data['ocupacao_maxima'], 
                            ocupacao_animais=data['ocupacao_animais'], feminino=data['feminino'])
            # Insira o novo abrigo no banco de dados
            cursor.insert_abrigo(values=abrigo.format_for_database())
            return jsonify({"message": "Abrigo criado com sucesso!"}), 201
        except:
            return jsonify({"message": "Erro ao criar abrigo"}), 500
    

    @app.route('/abrigo/<int:id_abrigo>', methods=['GET'])
    def read_abrigo(id_abrigo):
        # Busque o abrigo pelo ID no banco de dados
        response = cursor.get_abrigo(id=id_abrigo)
        if response:
            return jsonify({
                "endereco": response[1],
                "nome_responsavel": response[2],
                "cpf_responsavel": response[3],
                "telefone_responsavel": response[4],
                "email": response[5],
                "ocupacao_maxima": response[6],
                "ocupacao_animais": response[7],
                "feminino": response[8]
            })
        else:
            return jsonify({"message": "Abrigo não encontrado."}), 404
        

    @app.route('/abrigo/<int:id_abrigo>', methods=['PUT'])
    def update_abrigo(id_abrigo):
        data = request.get_json()
        abrigo = Abrigo(endereco=data['endereco'], nome_responsavel=data['nome_responsavel'], cpf_responsavel=data['cpf_responsavel'],
                telefone_responsavel=data['telefone_responsavel'], email=data['email'], ocupacao_maxima=data['ocupacao_maxima'], 
                ocupacao_animais=data['ocupacao_animais'], feminino=data['feminino'])
        # Atualize o abrigo no banco de dados
        count = cursor.update_abrigo(abrigo.format_for_database(id_abrigo=id_abrigo))
        if count > 0:
            return jsonify({"message": "Abrigo atualizado com sucesso!"}), 200
        else:
            return jsonify({"message": "Abrigo não encontrado."}), 404
        

    @app.route('/abrigo/<int:id_abrigo>', methods=['DELETE'])
    def delete_abrigo(id_abrigo):
        # Delete o abrigo do banco de dados
        count = cursor.delete_abrigo(id=id_abrigo)
        if count > 0:
            return jsonify({"message": "Abrigo deletado com sucesso!"}), 200
        else:
            return jsonify({"message": "Abrigo não encontrado."}), 404
        

    @app.route('/estoque', methods=['POST'])
    def create_produto():
        data = request.get_json()
        try:
            mantimento = Mantimento(id_abrigo=data['id_abrigo'], id_produto=data['id_produto'], descricao_produto=data['descricao_produto'])
            # Insira o novo produto no estoque no banco de dados
            cursor.insert_mantimento(mantimento.format_for_database())
            return jsonify({"message": "Produto adicionado ao estoque com sucesso!"}), 201
        except:
            return jsonify({"message": "Falha ao adicionar produto ao estoque"}), 500
            

    @app.route('/estoque/<int:id_estoque>', methods=['GET'])
    def read_produto(id_estoque):
        # Busque o produto pelo ID no banco de dados
        response = cursor.get_mantimento(id=id_estoque)
        if response:
            return jsonify({
                "id_abrigo": response[1],
                "id_produto": response[2],
                "descricao_produto": response[3]
            })
        else:
            return jsonify({"message": "Produto não encontrado."}), 404


    @app.route('/estoque/<int:id_estoque>', methods=['PUT'])
    def update_produto(id_estoque):
        data = request.get_json()
        mantimento = Mantimento(id_abrigo=data['id_abrigo'], id_produto=data['id_produto'], descricao_produto=data['descricao_produto'])
        # Atualize o produto no estoque no banco de dados
        count = cursor.update_mantimento(values=mantimento.format_for_database(id_estoque=id_estoque))
        if count > 0:
            return jsonify({"message": "Produto atualizado com sucesso!"}), 200
        else:
            return jsonify({"message": "Produto não encontrado."}), 404
        

    @app.route('/estoque/<int:id_estoque>', methods=['DELETE'])
    def delete_produto(id_estoque):
        # Delete o produto do estoque do banco de dados
        count = cursor.delete_mantimento(id=id_estoque)
        if count > 0:
            return jsonify({"message": "Produto deletado do estoque com sucesso!"}), 200
        else:
            return jsonify({"message": "Produto não encontrado."}), 404
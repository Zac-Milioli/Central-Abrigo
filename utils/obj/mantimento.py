class Mantimento:
    def __init__(self, id_abrigo: int = 0, id_produto: int = 0, descricao_produto: str = ''):
        self.id_abrigo = id_abrigo
        self.id_produto = id_produto
        self.descricao_produto = descricao_produto

    def format_for_database(self, id_estoque=None):
        if id_estoque:
            return (self.id_abrigo, self.id_produto, self.descricao_produto, id_estoque)
        else:
            return (self.id_abrigo, self.id_produto, self.descricao_produto)
class Mantimento:
    def __init__(self, id_abrigo: int = 0, id_produto: int = 0, descricao_produto: str = ''):
        self._id_abrigo = id_abrigo
        self._id_produto = id_produto
        self._descricao_produto = descricao_produto

    # Getter para id_abrigo
    def get_id_abrigo(self):
        return self._id_abrigo

    # Setter para id_abrigo
    def set_id_abrigo(self, id_abrigo):
        self._id_abrigo = id_abrigo

    # Getter para id_produto
    def get_id_produto(self):
        return self._id_produto

    # Setter para id_produto
    def set_id_produto(self, id_produto):
        self._id_produto = id_produto

    # Getter para descricao_produto
    def get_descricao_produto(self):
        return self._descricao_produto

    # Setter para descricao_produto
    def set_descricao_produto(self, descricao_produto):
        self._descricao_produto = descricao_produto
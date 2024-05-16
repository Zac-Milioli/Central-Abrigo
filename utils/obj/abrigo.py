class Abrigo:
    def __init__(self, endereco: str = '', nome_responsavel: str = '', cpf_responsavel: str = '', telefone_responsavel: str = '', email: str = '', ocupacao_maxima: int = 0, ocupacao_animais: int = 0, feminino: bool = False):
        self.endereco = endereco
        self.nome_responsavel = nome_responsavel
        self.cpf_responsavel = cpf_responsavel
        self.telefone_responsavel = telefone_responsavel
        self.email = email
        self.ocupacao_maxima = ocupacao_maxima
        self.ocupacao_animais = ocupacao_animais
        self.feminino = feminino

    def format_for_database(self, id_abrigo=None):
        if id_abrigo:
            return (self.endereco, self.nome_responsavel, self.cpf_responsavel, self.telefone_responsavel, self.email, self.ocupacao_maxima, self.ocupacao_animais, self.feminino, id_abrigo)
        else:
            return (self.endereco, self.nome_responsavel, self.cpf_responsavel, self.telefone_responsavel, self.email, self.ocupacao_maxima, self.ocupacao_animais, self.feminino)

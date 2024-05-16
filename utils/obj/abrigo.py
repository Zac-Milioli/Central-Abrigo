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

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, endereco):
        self.endereco = endereco

    def get_nome_responsavel(self):
        return self.nome_responsavel

    def set_nome_responsavel(self, nome_responsavel):
        self.nome_responsavel = nome_responsavel

    def get_cpf_responsavel(self):
        return self.cpf_responsavel

    def set_cpf_responsavel(self, cpf_responsavel):
        self.cpf_responsavel = cpf_responsavel

    def get_telefone_responsavel(self):
        return self.telefone_responsavel

    def set_telefone_responsavel(self, telefone_responsavel):
        self.telefone_responsavel = telefone_responsavel

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_ocupacao_maxima(self):
        return self.ocupacao_maxima

    def set_ocupacao_maxima(self, ocupacao_maxima):
        self.ocupacao_maxima = ocupacao_maxima

    def get_ocupacao_animais(self):
        return self.ocupacao_animais

    def set_ocupacao_animais(self, ocupacao_animais):
        self.ocupacao_animais = ocupacao_animais

    def is_feminino(self):
        return self.feminino

    def set_feminino(self, feminino):
        self.feminino = feminino
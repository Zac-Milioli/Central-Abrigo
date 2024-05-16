CREATE TABLE IF NOT EXISTS abrigo (
    id_abrigo INTEGER PRIMARY KEY AUTOINCREMENT,
    endereco VARCHAR(255),
    nome_responsavel VARCHAR(255),
    cpf_responsavel VARCHAR(255),
    telefone_responsavel VARCHAR(255),
    email VARCHAR(50),
    ocupacao_maxima INTEGER,
    ocupacao_animais INTEGER,
    feminino BOOLEAN
);

CREATE TABLE IF NOT EXISTS estoque (
    id_estoque INTEGER PRIMARY KEY AUTOINCREMENT,
    id_abrigo INTEGER UNIQUE,
    id_produto REAL UNIQUE,
    descricao_produto VARCHAR(255),
    FOREIGN KEY (id_abrigo) REFERENCES abrigo(id_abrigo)
);
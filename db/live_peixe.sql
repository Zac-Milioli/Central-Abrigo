CREATE TABLE abrigo (
    id_abrigo INT AUTO_INCREMENT PRIMARY KEY,
    endereco VARCHAR(255),
    nome_responsavel VARCHAR(255),
    cpf_responsavel VARCHAR(255),
    telefone_responsavel VARCHAR(255),
    email VARCHAR(50),
    ocupacao_maxima INT,
    ocupacao_animais INT,
    feminino BOOL
);

CREATE TABLE estoque (
	id_estoque INT AUTO_INCREMENT PRIMARY KEY,
    id_abrigo INT UNIQUE,
    id_produto FLOAT UNIQUE,
    descricao_produto VARCHAR(255),
    FOREIGN KEY (id_abrigo) REFERENCES abrigo(id_abrigo)
);

select * from abrigo;
select * from estoque;
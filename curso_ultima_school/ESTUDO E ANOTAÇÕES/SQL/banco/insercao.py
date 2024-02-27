import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('sqlite5')
cursor = conn.cursor()

# iserir valores na coluna
sql = '''
CREATE TABLE Fornecedor (
    id INT PRIMARY KEY,
    nome VARCHAR(255),
    endereco VARCHAR(255),
    produto VARCHAR(255)
);


'''
cursor.execute(sql)
conn.commit()
conn.close()


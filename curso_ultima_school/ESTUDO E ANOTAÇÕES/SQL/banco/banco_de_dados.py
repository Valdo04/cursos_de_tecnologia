
import sqlite3

conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE bicicleta (id INT, nome VARCHAR(100),endereco VARCHAR(250));')
conexao.commit()
conexao.close()

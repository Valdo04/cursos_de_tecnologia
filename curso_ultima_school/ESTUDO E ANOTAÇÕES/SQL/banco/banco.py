
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('sqlite3')
cursor = conn.cursor()
# Criar a tabela com AUTOINCREMENT na coluna id (INTEGER PRIMARY KEY)
cursor.execute('CREATE TABLE categoria (id INTEGER PRIMARY KEY AUTOINCREMENT, descricao TEXT);')
# Commit para salvar as alterações
conn.commit()
# Fechar a conexão
conn.close()


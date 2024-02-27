import sqlite3

# Conectar ao banco de dados (ou criar um novo)
conexao = sqlite3.connect('sqlite5')

# Criar o cursor
cursor = conexao.cursor()

# Inserir novos fornecedores
cursor.executescript('''
    INSERT INTO Fornecedor (id, nome, endereco, produto) VALUES
    (3, 'Padaria do Pão', 'Rua da Padaria, 123', 'Pães'),
    (4, 'Marcenaria Martelo', 'Avenida da Marcenaria, 456', 'Móveis');
''')

# Atualizar endereço do fornecedor com id = 2
cursor.execute("UPDATE Fornecedor SET endereco = 'Rua dos Peixes, 26' WHERE id = 2")

# Selecionar todos os registros da tabela Fornecedor
cursor.execute("SELECT * FROM Fornecedor")
todos_fornecedores = cursor.fetchall()
print("Todos os fornecedores:")
for fornecedor in todos_fornecedores:
    print(f"{fornecedor[0]} - {fornecedor[1]} - {fornecedor[2]} - {fornecedor[3]}")

# Selecionar registros da tabela Fornecedor com produto igual a Carnes
cursor.execute("SELECT * FROM Fornecedor WHERE produto = 'Carnes'")
fornecedores_carnes = cursor.fetchall()
print("\nFornecedores de Carnes:")
for fornecedor in fornecedores_carnes:
    print(f"{fornecedor[0]} - {fornecedor[1]} - {fornecedor[2]} - {fornecedor[3]}")

# Remover fornecedor com id = 1
cursor.execute("DELETE FROM Fornecedor WHERE id = 1")

# Commit e fechar a conexão
conexao.commit()
conexao.close()

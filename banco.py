import sqlite3 as lite

# Criando a conexão
connection = lite.connect('dados.db')

# Criando a tabela de clientes
with connection:
    cursor_clients = connection.cursor()
    cursor_clients.execute('CREATE TABLE clientes(nome TEXT, cpf INTEGER PRIMARY KEY, email TEXT, telefone TEXT,'
                           ' endereço TEXT)')
    cursor_motorcyle = connection.cursor()
    cursor_motorcyle.execute('CREATE TABLE motocicletas(numero_de_identificaçao INTEGER PRIMARY KEY, preço FLOAT,'
                             ' modelo TEXT, estado_da_motocicleta TEXT)')


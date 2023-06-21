import sqlite3 as lite

# Fazendo o CRUD

# Criando a conexão
connection = lite.connect('dados.db')


# Criando informações de clientes
def create_clients_info(clients_info_list):
    with connection:
        cursor_create_clients = connection.cursor()
        query_create_clients = "INSERT INTO clientes (nome, CPF, email, telefone, endereço) VALUES (?, ?, ?, ?, ?)"
        cursor_create_clients.execute(query_create_clients, clients_info_list)


# Acessando informações de clientes
def show_clients_info():
    clients_list = []
    with connection:
        cursor_read_clients = connection.cursor()
        query_read_clients = "SELECT * FROM clientes"
        cursor_read_clients.execute(query_read_clients)
        info = cursor_read_clients.fetchall()

        for i in info:
            clients_list.append(i)
    return clients_list


# Atualizando informações de clientes
def update_clients_info(clients_update_list):
    with connection:
        cursor_update_clients = connection.cursor()
        query_update_clients = "UPDATE clientes SET nome=?, email=?, telefone=?, endereço=? WHERE cpf=?"
        cursor_update_clients.execute(query_update_clients, clients_update_list)


# Deletando clientes
def delete_clients_info(clients_delete_list):
    with connection:
        cursor_delete_clients = connection.cursor()
        query_delete_clients = "DELETE FROM clientes WHERE cpf=?"
        cursor_delete_clients.execute(query_delete_clients, clients_delete_list)


####################################################################################################

# Criando informações de motocicletas
def create_motorcycle_info(motorcycle_info_list):
    with connection:
        cursor_create_motorcycle = connection.cursor()
        query_create_motorcycle = "INSERT INTO motocicletas (numero_de_identificaçao, preço, modelo, estado_da" \
                                  "_motocicleta) VALUES (?, ?, ?, ?)"
        cursor_create_motorcycle.execute(query_create_motorcycle, motorcycle_info_list)


# Acessando informações de motocicletas
def show_motorcycle_info():
    motorcycle_list = []
    with connection:
        cursor_read_motorcycle = connection.cursor()
        query_read_motorcycle = "SELECT * FROM motocicletas"
        cursor_read_motorcycle.execute(query_read_motorcycle)
        info = cursor_read_motorcycle.fetchall()

        for i in info:
            motorcycle_list.append(i)
    return motorcycle_list


# Atualizando informações de motocicletas
def update_motorcycle_info(motorcycle_update_list):
    with connection:
        cursor_update_motorcycle = connection.cursor()
        query_update_motorcycle = "UPDATE motocicletas SET preço=?, modelo=?, estado_da_motocicleta=? WHERE numero_de" \
                                  "_identificaçao=?"
        cursor_update_motorcycle.execute(query_update_motorcycle, motorcycle_update_list)


# Deletando motocicletas
def delete_motorcycle_info(motorcycle_delete_list):
    with connection:
        cursor_delete_motorcycle = connection.cursor()
        query_delete_motorcycle = "DELETE FROM motocicletas WHERE numero_de_identificaçao=?"
        cursor_delete_motorcycle.execute(query_delete_motorcycle, motorcycle_delete_list)

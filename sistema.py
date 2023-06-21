from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from view import *

# cores
co1 = "#feffff"  # Branco
co2 = "#4fa882"  # Verde
co3 = "#38576b"  # Azul-escuro
co4 = "#403d3d"  # Cor da letra
co5 = "#038cfc"  # Azul
co6 = "#ef5350"  # Vermelho
co7 = "#e9edf5"  # Azul muito claro

root = Tk()
root.geometry('1280x720')
root.title('Sistema para concessionária')
root.configure(background=co7)
root.resizable(width=False, height=False)

# Criando as abas clientes, motocicletas e vendas
notebook = ttk.Notebook(root, width=1280, height=720)

clients_frame = Frame(notebook, background=co7)
motorcycle_frame = Frame(notebook, background=co7)
sales_frame = Frame(notebook, background=co7)

notebook.add(clients_frame, text='Clientes')
notebook.add(motorcycle_frame, text='Motocicletas')
notebook.add(sales_frame, text='Vendas')

notebook.enable_traversal()
notebook.pack(padx=0, pady=0)

# Dividindo a tela da aba de clientes

clients_title_frame = Frame(clients_frame, width=410, height=50, bg=co3, relief='flat')
clients_title_frame.place(x=0, y=0)

clients_interface_frame = Frame(clients_frame, width=410, height=650, bg='light gray', relief='flat')
clients_interface_frame.place(x=0, y=51)

clients_table_frame = Frame(clients_frame, width=870, height=700, bg=co7, relief='flat')
clients_table_frame.place(x=411, y=0)

# Criando o título da aba de clientes

clients_title = Label(clients_title_frame, text='CADASTRO DE CLIENTES', anchor=CENTER, font=('ivy', 19, 'bold'),
                      bg=co3, fg=co1, relief='flat')
clients_title.place(x=48, y=7)

global tree_clients


# Função para criar clientes

def create_client():
    name = entry_clients_name.get()
    CPF = entry_clients_cpf.get()
    email = entry_clients_email.get()
    phone_number = entry_clients_phone_number.get()
    address = entry_clients_address.get()

    clients_infos = [name, CPF, email, phone_number, address]

    if name == '' or CPF == '' or email == '' or phone_number == '' or address == '':
        messagebox.showerror('Erro', 'Todos os campos devem ser preenchidos!')
    else:
        create_clients_info(clients_infos)
        messagebox.showinfo('Sucesso', 'Cliente cadastrado.')

        entry_clients_name.delete(0, 'end')
        entry_clients_cpf.delete(0, 'end')
        entry_clients_email.delete(0, 'end')
        entry_clients_phone_number.delete(0, 'end')
        entry_clients_address.delete(0, 'end')

    for widget in clients_table_frame.winfo_children():
        widget.destroy()

    show_clients()


# Função para atualizar clientes

def update_client():
    try:
        treev_info = tree_clients.focus()
        treev_dictionary = tree_clients.item(treev_info)
        tree_list = treev_dictionary['values']

        cpf = tree_list[0]

        entry_clients_name.delete(0, 'end')
        entry_clients_cpf.delete(0, 'end')
        entry_clients_email.delete(0, 'end')
        entry_clients_phone_number.delete(0, 'end')
        entry_clients_address.delete(0, 'end')

        entry_clients_name.insert(0, tree_list[1])
        entry_clients_cpf.insert(0, tree_list[0])
        entry_clients_email.insert(0, tree_list[2])
        entry_clients_phone_number.insert(0, tree_list[3])
        entry_clients_address.insert(0, tree_list[4])

        # Função criar

        def update_tree_clients():
            name = entry_clients_name.get()
            email = entry_clients_email.get()
            phone_number = entry_clients_phone_number.get()
            address = entry_clients_address.get()

            clients_infos = [name, email, phone_number, address, cpf]

            if name == '' or email == '' or phone_number == '' or address == '':
                messagebox.showerror('Erro', 'Todos os campos devem ser preenchidos!')
            else:
                update_clients_info(clients_infos)
                messagebox.showinfo('Sucesso', 'Dados atualizados.')

                entry_clients_name.delete(0, 'end')
                entry_clients_cpf.delete(0, 'end')
                entry_clients_email.delete(0, 'end')
                entry_clients_phone_number.delete(0, 'end')
                entry_clients_address.delete(0, 'end')

            for widget in clients_table_frame.winfo_children():
                widget.destroy()

            clients_update_confirm.place_forget()
            show_clients()

        # Botão confirmar (aba clientes)
        clients_update_confirm = Button(clients_interface_frame, command=update_tree_clients, text='CONFIRMAR',
                                        width=20, anchor=CENTER, font=('ivy', 12, 'bold'), bg=co5, fg=co1,
                                        relief='raised', overrelief='ridge')
        clients_update_confirm.place(x=100, y=470)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione algum cliente da tabela!')


# Função para deletar clientes

def delete_client():
    try:
        treev_info = tree_clients.focus()
        treev_dictionary = tree_clients.item(treev_info)
        tree_list = treev_dictionary['values']

        cpf = [tree_list[0]]

        delete_clients_info(cpf)
        messagebox.showinfo('Sucesso', 'O cliente foi removido da tabela.')

        for widget in clients_table_frame.winfo_children():
            widget.destroy()

        show_clients()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione algum cliente da tabela!')


# Configurando a interface da aba de clientes

# Nome
label_clients_name = Label(clients_interface_frame, text='Nome', anchor=NW, font=('ivy', 12, 'bold'),
                           bg='light gray', fg=co4, relief='flat')
label_clients_name.place(x=10, y=10)
entry_clients_name = Entry(clients_interface_frame, width=40, font=('ivy', 12), justify='left', relief='solid')
entry_clients_name.place(x=13, y=40)

# CPF
label_clients_cpf = Label(clients_interface_frame, text='CPF', anchor=NW, font=('ivy', 12, 'bold'),
                          bg='light gray', fg=co4, relief='flat')
label_clients_cpf.place(x=10, y=80)
entry_clients_cpf = Entry(clients_interface_frame, width=40, font=('ivy', 12), justify='left', relief='solid')
entry_clients_cpf.place(x=13, y=110)

# Email
label_clients_email = Label(clients_interface_frame, text='Email', anchor=NW, font=('ivy', 12, 'bold'),
                            bg='light gray', fg=co4, relief='flat')
label_clients_email.place(x=10, y=150)
entry_clients_email = Entry(clients_interface_frame, width=40, font=('ivy', 12), justify='left', relief='solid')
entry_clients_email.place(x=13, y=180)

# Telefone
label_clients_phone_number = Label(clients_interface_frame, text='Telefone', anchor=NW,
                                   font=('ivy', 12, 'bold'), bg='light gray', fg=co4, relief='flat')
label_clients_phone_number.place(x=10, y=220)
entry_clients_phone_number = Entry(clients_interface_frame, width=40, font=('ivy', 12), justify='left',
                                   relief='solid')
entry_clients_phone_number.place(x=13, y=250)

# Endereço
label_clients_address = Label(clients_interface_frame, text='Endereço', anchor=NW, font=('ivy', 12, 'bold'),
                              bg='light gray', fg=co4, relief='flat')
label_clients_address.place(x=10, y=290)
entry_clients_address = Entry(clients_interface_frame, width=40, font=('ivy', 12), justify='left',
                              relief='solid')
entry_clients_address.place(x=13, y=320)

# Botão criar (aba clientes)
clients_create = Button(clients_interface_frame, command=create_client, text='CRIAR', width=20, anchor=CENTER,
                        font=('ivy', 12, 'bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
clients_create.place(x=100, y=390)

# Botão atualizar (aba clientes)
clients_update = Button(clients_interface_frame, command=update_client, text='ATUALIZAR', width=20, anchor=CENTER,
                        font=('ivy', 12, 'bold'), bg=co5, fg=co1, relief='raised', overrelief='ridge')
clients_update.place(x=100, y=470)

# Botão deletar (aba clientes)
clients_delete = Button(clients_interface_frame, command=delete_client, text='DELETAR', width=20, anchor=CENTER,
                        font=('ivy', 12, 'bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
clients_delete.place(x=100, y=550)


# Criando a tabela da aba clientes

# Função para fazer a tabela de clientes
def show_clients():
    global tree_clients

    clients_list = show_clients_info()

    clients_list_header = ['CPF', 'Nome', 'Email', 'Telefone', 'Endereço']

    tree_clients = ttk.Treeview(clients_table_frame, selectmode='extended', columns=clients_list_header,
                                show='headings',
                                height=32)

    # Barra de rolagem vertical
    vsb_clients = ttk.Scrollbar(clients_table_frame, orient='vertical', command=tree_clients.yview)

    # Barra de rolagem horizontal
    hsb_clients = ttk.Scrollbar(clients_table_frame, orient='horizontal', command=tree_clients.xview)

    # Criando a tabela
    tree_clients.configure(yscrollcommand=vsb_clients.set, xscrollcommand=hsb_clients.set)

    tree_clients.grid(column=0, row=0, sticky='nsew')
    vsb_clients.grid(column=1, row=0, sticky='ns')
    hsb_clients.grid(column=0, row=1, sticky='ew')
    clients_table_frame.grid_rowconfigure(0, weight=12)

    hd_clients = ['nw', 'center', 'nw', 'center', 'nw']
    # Definindo o tamanho dos campos da tabela
    h_clients = [200, 100, 200, 100, 246]
    n = 0

    for col in clients_list_header:
        tree_clients.heading(col, text=col.title(), anchor=CENTER)
        tree_clients.column(col, width=h_clients[n], anchor=hd_clients[n])
        n += 1

    for item in clients_list:
        tree_clients.insert('', 'end', values=item)


show_clients()

# Dividindo a tela da aba de motocicletas

motorcycle_title_frame = Frame(motorcycle_frame, width=410, height=50, bg=co3, relief='flat')
motorcycle_title_frame.place(x=0, y=0)

motorcycle_interface_frame = Frame(motorcycle_frame, width=410, height=650, bg='light gray', relief='flat')
motorcycle_interface_frame.place(x=0, y=51)

motorcycle_table_frame = Frame(motorcycle_frame, width=870, height=700, bg=co7, relief='flat')
motorcycle_table_frame.place(x=411, y=0)

# Criando o título da aba de motocicletas

motorcycle_title = Label(motorcycle_title_frame, text='CADASTRO DE MOTOCICLETAS', anchor=CENTER,
                         font=('ivy', 19, 'bold'), bg=co3, fg=co1, relief='flat')
motorcycle_title.place(x=8, y=7)

global tree_motorcycle


# Função para criar motocicletas

def create_motorcycle():
    id = entry_motorcycle_id.get()
    price = entry_motorcycle_price.get()
    model = entry_motorcycle_model.get()
    condition = entry_motorcycle_condition.get()

    motorcycle_infos = [id, price, model, condition]

    if id == '' or price == '' or model == '' or condition == '':
        messagebox.showerror('Erro', 'Todos os campos devem ser preenchidos!')
    else:
        create_motorcycle_info(motorcycle_infos)
        messagebox.showinfo('Sucesso', 'Motocicleta cadastrada.')

        entry_motorcycle_id.delete(0, 'end')
        entry_motorcycle_price.delete(0, 'end')
        entry_motorcycle_model.delete(0, 'end')
        entry_motorcycle_condition.delete(0, 'end')

    for widget in motorcycle_table_frame.winfo_children():
        widget.destroy()

    show_motorcycle()


# Função para atualizar motocicletas

def update_motorcycle():
    try:
        treev_info = tree_motorcycle.focus()
        treev_dictionary = tree_motorcycle.item(treev_info)
        tree_list = treev_dictionary['values']

        id = tree_list[0]

        entry_motorcycle_id.delete(0, 'end')
        entry_motorcycle_price.delete(0, 'end')
        entry_motorcycle_model.delete(0, 'end')
        entry_motorcycle_condition.delete(0, 'end')

        entry_motorcycle_id.insert(0, tree_list[0])
        entry_motorcycle_price.insert(0, tree_list[1])
        entry_motorcycle_model.insert(0, tree_list[2])
        entry_motorcycle_condition.insert(0, tree_list[3])

        # Função criar

        def update_tree_motorcycle():
            price = entry_motorcycle_price.get()
            model = entry_motorcycle_model.get()
            condition = entry_motorcycle_condition.get()

            motorcycle_infos = [price, model, condition, id]

            if price == '' or model == '':
                messagebox.showerror('Erro', 'Todos os campos devem ser preenchidos!')
            else:
                update_motorcycle_info(motorcycle_infos)
                messagebox.showinfo('Sucesso', 'Dados atualizados.')

                entry_motorcycle_id.delete(0, 'end')
                entry_motorcycle_price.delete(0, 'end')
                entry_motorcycle_model.delete(0, 'end')
                entry_motorcycle_condition.delete(0, 'end')

            for widget in motorcycle_table_frame.winfo_children():
                widget.destroy()

            motorcycle_update_confirm.place_forget()
            show_motorcycle()

        # Botão confirmar (aba motocicletas)
        motorcycle_update_confirm = Button(motorcycle_interface_frame, command=update_tree_motorcycle, text='CONFIRMAR',
                                           width=20, anchor=CENTER, font=('ivy', 12, 'bold'), bg=co5, fg=co1,
                                           relief='raised', overrelief='ridge')
        motorcycle_update_confirm.place(x=100, y=470)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione alguma motocicleta da tabela!')


# Função para deletar motocicletas

def delete_motorcycle():
    try:
        treev_info = tree_motorcycle.focus()
        treev_dictionary = tree_motorcycle.item(treev_info)
        tree_list = treev_dictionary['values']

        id = [tree_list[0]]

        delete_motorcycle_info(id)
        messagebox.showinfo('Sucesso', 'A motocicleta foi removido da tabela.')

        for widget in motorcycle_table_frame.winfo_children():
            widget.destroy()

        show_motorcycle()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione alguma motocicleta da tabela!')


# Configurando a interface da aba de motocicletas

# Número de identificação
label_motorcycle_id = Label(motorcycle_interface_frame, text='Número de identificação', anchor=NW,
                            font=('ivy', 12, 'bold'), bg='light gray', fg=co4, relief='flat')
label_motorcycle_id.place(x=10, y=10)
entry_motorcycle_id = Entry(motorcycle_interface_frame, width=40, font=('ivy', 12), justify='left',
                            relief='solid')
entry_motorcycle_id.place(x=13, y=40)

# Preço
label_motorcycle_price = Label(motorcycle_interface_frame, text='Preço', anchor=NW, font=('ivy', 12, 'bold'),
                               bg='light gray', fg=co4, relief='flat')
label_motorcycle_price.place(x=10, y=80)
entry_motorcycle_price = Entry(motorcycle_interface_frame, width=40, font=('ivy', 12), justify='left',
                               relief='solid')
entry_motorcycle_price.place(x=13, y=110)

# Modelo
label_motorcycle_model = Label(motorcycle_interface_frame, text='Modelo', anchor=NW, font=('ivy', 12, 'bold'),
                               bg='light gray', fg=co4, relief='flat')
label_motorcycle_model.place(x=10, y=150)
entry_motorcycle_model = Entry(motorcycle_interface_frame, width=40, font=('ivy', 12), justify='left',
                               relief='solid')
entry_motorcycle_model.place(x=13, y=180)

# Estado
label_motorcycle_condition = Label(motorcycle_interface_frame, text='Estado da motocicleta', anchor=NW,
                                   font=('ivy', 12, 'bold'), bg='light gray', fg=co4, relief='flat')
label_motorcycle_condition.place(x=10, y=220)
entry_motorcycle_condition = ttk.Combobox(motorcycle_interface_frame, width=38, font=('ivy', 12))
entry_motorcycle_condition['values'] = ['Nova', 'Seminova', 'Usada']
entry_motorcycle_condition.current(0)
entry_motorcycle_condition.place(x=13, y=250)

# Botão criar (aba motocicletas)
motorcycle_create = Button(motorcycle_interface_frame, command=create_motorcycle, text='CRIAR', width=20, anchor=CENTER,
                           font=('ivy', 12, 'bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
motorcycle_create.place(x=100, y=390)

# Botão atualizar (aba motocicletas)
motorcycle_update = Button(motorcycle_interface_frame, command=update_motorcycle, text='ATUALIZAR', width=20, anchor=CENTER,
                           font=('ivy', 12, 'bold'), bg=co5, fg=co1, relief='raised', overrelief='ridge')
motorcycle_update.place(x=100, y=470)

# Botão deletar (aba motocicletas)
motorcycle_delete = Button(motorcycle_interface_frame, command=delete_motorcycle, text='DELETAR', width=20, anchor=CENTER,
                           font=('ivy', 12, 'bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
motorcycle_delete.place(x=100, y=550)


# Criando a tabela da aba motocicletas


# Função para fazer a tabela de motocicletas
def show_motorcycle():
    global tree_motorcycle

    motorcycle_list = show_motorcycle_info()

    motorcycle_list_header = ['Número de identificação', 'Preço', 'Modelo', 'Estado Da Motocicleta']

    tree_motorcycle = ttk.Treeview(motorcycle_table_frame, selectmode='extended', columns=motorcycle_list_header,
                                   show='headings', height=32)

    # Barra de rolagem vertical
    vsb_motorcycle = ttk.Scrollbar(motorcycle_table_frame, orient='vertical', command=tree_motorcycle.yview)

    # Barra de rolagem horizontal
    hsb_motorcycle = ttk.Scrollbar(motorcycle_table_frame, orient='horizontal', command=tree_motorcycle.xview)

    # Criando a tabela
    tree_motorcycle.configure(yscrollcommand=vsb_motorcycle.set, xscrollcommand=hsb_motorcycle.set)

    tree_motorcycle.grid(column=0, row=0, sticky='nsew')
    vsb_motorcycle.grid(column=1, row=0, sticky='ns')
    hsb_motorcycle.grid(column=0, row=1, sticky='ew')
    motorcycle_table_frame.grid_rowconfigure(0, weight=12)

    hd_motorcycle = ['center', 'center', 'nw', 'nw']
    # Definindo o tamanho dos campos da tabela
    h_motorcycle = [211, 211, 212, 212]
    n = 0

    for col in motorcycle_list_header:
        tree_motorcycle.heading(col, text=col.title(), anchor=CENTER)
        tree_motorcycle.column(col, width=h_motorcycle[n], anchor=hd_motorcycle[n])
        n += 1

    for item in motorcycle_list:
        tree_motorcycle.insert('', 'end', values=item)


show_motorcycle()

# Dividindo a tela da aba de vendas

sales_title_frame = Frame(sales_frame, width=410, height=50, bg=co3, relief='flat')
sales_title_frame.place(x=0, y=0)

sales_interface_frame = Frame(sales_frame, width=410, height=650, bg='light gray', relief='flat')
sales_interface_frame.place(x=0, y=51)

sales_table_frame = Frame(sales_frame, width=870, height=700, bg=co7, relief='flat')
sales_table_frame.place(x=411, y=0)

# Criando o título da aba de vendas

sales_title = Label(sales_title_frame, text='GERENCIAMENTO DE VENDAS', anchor=CENTER, font=('ivy', 19, 'bold'),
                    bg=co3, fg=co1, relief='flat')
sales_title.place(x=14, y=7)

# Configurando a interface da aba de vendas

# Número de identificação da motocicleta
label_sales_motocycleid = Label(sales_interface_frame, text='Número de identificação da motocicleta', anchor=NW,
                                font=('ivy', 12, 'bold'), bg='light gray', fg=co4, relief='flat')
label_sales_motocycleid.place(x=10, y=10)
entry_sales_motocycleid = Entry(sales_interface_frame, width=40, font=('ivy', 12), justify='left',
                                relief='solid')
entry_sales_motocycleid.place(x=13, y=40)

# CPF do cliente
label_sales_clientscpf = Label(sales_interface_frame, text='CPF', anchor=NW, font=('ivy', 12, 'bold'),
                               bg='light gray', fg=co4, relief='flat')
label_sales_clientscpf.place(x=10, y=80)
label_sales_clientscpf = Entry(sales_interface_frame, width=40, font=('ivy', 12), justify='left',
                               relief='solid')
label_sales_clientscpf.place(x=13, y=110)

# Valor da venda
label_sales_price = Label(sales_interface_frame, text='Preço', anchor=NW, font=('ivy', 12, 'bold'),
                          bg='light gray', fg=co4, relief='flat')
label_sales_price.place(x=10, y=150)
entry_sales_price = Entry(sales_interface_frame, width=40, font=('ivy', 12), justify='left', relief='solid')
entry_sales_price.place(x=13, y=180)

# Forma de pagamento
label_sales_payment_method = Label(sales_interface_frame, text='Forma de pagamento', anchor=NW,
                                   font=('ivy', 12, 'bold'), bg='light gray', fg=co4, relief='flat')
label_sales_payment_method.place(x=10, y=220)
entry_sales_payment_method = ttk.Combobox(sales_interface_frame, width=16, font=('ivy', 12))
entry_sales_payment_method['values'] = ['Dinheiro', 'Crédito', 'Débito', 'Cheque']
entry_sales_payment_method.current(0)
entry_sales_payment_method.place(x=13, y=250)

# Data da venda
label_sales_date = Label(sales_interface_frame, text='Data da venda', anchor=NW, font=('ivy', 12, 'bold'),
                         bg='light gray', fg=co4, relief='flat')
label_sales_date.place(x=250, y=220)
entry_sales_date = DateEntry(sales_interface_frame, width=14, background='darkblue', foreground='white',
                             borderwidth=2, locale='pt_BR')
entry_sales_date.place(x=253, y=250)

# Botão criar (aba vendas)
sales_create = Button(sales_interface_frame, text='VENDER', width=20, anchor=CENTER,
                      font=('ivy', 12, 'bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
sales_create.place(x=100, y=390)

# Botão atualizar (aba vendas)
sales_search = Button(sales_interface_frame, text='PESQUISAR', width=20, anchor=CENTER,
                      font=('ivy', 12, 'bold'), bg=co5, fg=co1, relief='raised', overrelief='ridge')
sales_search.place(x=100, y=470)

# Botão deletar (aba vendas)
sales_delete = Button(sales_interface_frame, text='DELETAR', width=20, anchor=CENTER,
                      font=('ivy', 12, 'bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
sales_delete.place(x=100, y=550)

# Criando a tabela da aba vendas

sales_list = [['1', 88537558773, 83847362837593863, '20/09/2022', 'R$ 839283,00', 'Cheque'],
              ['2', 42537552772, 33852362840553861, '16/12/2015', 'R$ 1439133,00', 'Dinheiro'],
              ['3', 38547552770, 43846436234059386, '04/06/2018', 'R$ 155223,00', 'Débito'],
              ['4', 77537558764, 20347346283056337, '27/04/2020', 'R$ 239285,00', 'Crédito'],
              ]

sales_list_header = ['Id', 'CPF', 'Número de identificação', 'Data', 'Preço', 'Forma de pagamento']

tree_sales = ttk.Treeview(sales_table_frame, selectmode='extended', columns=sales_list_header, show='headings',
                          height=32)

# Barra de rolagem vertical
vsb_sales = ttk.Scrollbar(sales_table_frame, orient='vertical', command=tree_sales.yview)

# Barra de rolagem horizontal
hsb_sales = ttk.Scrollbar(sales_table_frame, orient='horizontal', command=tree_sales.xview)

# Criando a tabela
tree_sales.configure(yscrollcommand=vsb_sales.set, xscrollcommand=hsb_sales.set)

tree_sales.grid(column=0, row=0, sticky='nsew')
vsb_sales.grid(column=1, row=0, sticky='ns')
hsb_sales.grid(column=0, row=1, sticky='ew')
sales_table_frame.grid_rowconfigure(0, weight=12)

hd_sales = ['center', 'center', 'center', 'center', 'nw', 'center']
# Definindo o tamanho dos campos da tabela
h_sales = [141, 141, 141, 141, 141, 141]
n = 0

for col in sales_list_header:
    tree_sales.heading(col, text=col.title(), anchor=CENTER)
    tree_sales.column(col, width=h_sales[n], anchor=hd_sales[n])
    n += 1

for item in sales_list:
    tree_sales.insert('', 'end', values=item)

root.mainloop()

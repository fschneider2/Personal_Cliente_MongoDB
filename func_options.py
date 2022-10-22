import pymongo
import pprint
import os
from time import sleep
from basic_func import menus, salutation, user_name_and_salutation, inicial
import func_app

conexao = pymongo.MongoClient("mongodb://localhost:27017/")

#=======================================================================================#
# função da opção 0 do menu principal:

# Função para desligar o app, é chamada em todos os sub_menus e no menu principal. 

def app_off():
    os.system('clear')
    print(f'\nObrigado por utilizar nosso aplicativo {salutation()}')
    sleep(0.5)
    return True

#=======================================================================================#
# Funções para execução das funcionalidades da opção 1 do menu principal:

# Funções para criar Bancos de dados

#Faz a chamada inicial, trazendo o menu, pegando a opção do usuario e retornando.
def criar_db_inicial():

    os.system('clear')

    string = (f"Para criar um banco de dados no MongoDB, "
    f"é necessário inserir ao menos uma coleção e um documento, selecione como você deseja prosseguir: \n{menus('sub_menu_1')}")

    options_menu = ('0', '1', '2')

    option_selec = inicial(options_menu, string)

    return option_selec

# esta função retorna um menu, que será invocado após o usuario incluir o banco.
def sub_menu_1_1():

    options_menu = ('0', '1', '2')
    
    string = f"\n Selecione uma das seguintes opções :\n{menus('sub_menu_1_1')}"

    option_selec = inicial(options_menu, string)
    
    if option_selec == 0:
        app_off()

    if option_selec == 1:
        option = criar_db_inicial()
        sub_menu_1(option)

    if option_selec == 2:
        func_app.app()

# esta função recebe a criar_db_inicial, e executa as opções de criação do banco,
# retorna um sub_menu, cujas opções são inserir um novo banco, sair ou voltar ao menu inicial.
def sub_menu_1(option_selec):

    if option_selec == 0:
        app_off()

    if option_selec == 1:

        os.system('clear')

        name_db = input("Digite nome do banco a ser criado:>>> ")

        db = conexao[name_db]

        collection_autocreate = db['teste']

        collection_autocreate.insert_one(
            {
                "arquivo": "teste"
            }
        )

        os.system('clear')
    
        print(f"Banco {name_db} criado com sucesso!")

        sub_menu_1_1()

    if option_selec == 2:

        os.system('clear')

        name_db = input("Digite nome do banco a ser criado:>>> ")
        
        db = conexao[name_db]

        name_collection = input("Digite nome da coleção a ser criada:>>> ")

        collection_create = db[name_collection]

        name_chave = input("Digite nome da chave:>>> ")

        name_valor = input("Digite nome do valor:>>> ")

        collection_create.insert_one(
            {
                name_chave: name_valor
            }
        )

        os.system('clear')

        print(f"Banco {name_db}, coleção {name_collection} e documento criados com sucesso!")
        
        sub_menu_1_1()

# Função de invocação, invoca e organiza as funções de criação de banco 
# para depois ser invocada pela função app() do arquivo func_app.
def criar_db():

    option_selec = criar_db_inicial()

    sub_menu_1(option_selec)

#=======================================================================================#
# Funções de ação para funcionalidade 2 do menu principal:
def criar_colecao_inicial():

    os.system('clear')

    options_menu = ('0', '1', '2')

    string = (f"Para criar uma Coleção, devera informar o nome do banco ou retorne ao "
    f"menu principal para criar um, \nselecione como você deseja prosseguir: \n{menus('sub_menu_2')}")

    option_selec = inicial(options_menu, string)

    return option_selec

def sub_menu_2(option_selec):

    if option_selec == 0:
        app_off()

    if option_selec == 1:

        os.system('clear')

        print("Ao criar uma coleção, irei inserir automaticamente um documento com _id = 0, chave = arquivo, valor = teste.")

        list_db = conexao.list_database_names()

        print(f"\nBancos disponiveis: \n{list_db}")

        name_db = input("\nDigite nome do banco para qual deseja criar a coleção:>>> ")

        while name_db not in list_db:
            os.system('clear')
            print(f"Banco {name_db} não existe.")
            print(f"\nBancos disponiveis: \n{list_db}")
            name_db = input("\nDigite nome do banco para qual deseja criar a coleção:>>> ")

        db = conexao[name_db]
        
        name_collection = input("\nDigite nome da coleção a ser criada:>>> ")

        collection_create = db[name_collection]

        collection_create.insert_one(
            {
                "_id": 0,
                "arquivo": "teste"
            }
        )

        print(f"Coleção {name_collection} criada com sucesso!")
        sleep(1.2)
        option = criar_colecao_inicial()
        sub_menu_2(option)

    if option_selec == 2:
        func_app.app()

def criar_colecao():
    option_select = criar_colecao_inicial()

    sub_menu_2(option_select)

#=======================================================================================#
# Funções de ação para funcionalidade 7 do menu principal:

def print_bancos():
    list_db = conexao.list_database_names()   

    print('Bancos Disponiveis: \n')
    print('='*20)

    for banco in list_db:
        print(f"  {banco}")

    print('='*20)    

def menu_consulta_inicial():

    options_menu = ('0', '1', '2')
    
    string = f"\nPara prosseguir Informe uma das seguintes opções do menu:{menus('sub_menu_7')}"
    
    option_selec = inicial(options_menu, string)

    return option_selec

def sub_menu_7(option_selec):

    if option_selec == 0:
        app_off()

    if option_selec == 1:

        os.system('clear')

        print_bancos()

        list_db = conexao.list_database_names()  

        name_db = input("\nDigite nome do banco para qual deseja consultar a(s) coleção(ões):>>> ")

        while name_db not in list_db:

            os.system('clear')
            print(f"Banco {name_db} não existe.")
            print(f"\nBancos disponiveis: \n{list_db}")
            name_db = input("\nDigite nome do banco para qual deseja consultar a(s) coleção(ões):>>> ")

        banco = conexao[name_db]

        list_collections = banco.list_collection_names()

        sleep(2)
        os.system('clear')

        print(f"\nColeções do banco {name_db}: \n{list_collections}")

        option = menu_consulta_inicial()
        sub_menu_7(option)

    if option_selec == 2:
        os.system('clear')
        func_app.app()

def listar_bancos_colecoes():

    print_bancos()

    option_selec = menu_consulta_inicial()

    sub_menu_7(option_selec)
    


    

    
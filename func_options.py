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

# Funções para criar Bancos de dados, questão 5 letra A.
# todas as funções abaixo são relacionadas a funcionalidade criar bancos de dados.

#Faz a chamada inicial, trazendo o menu, pegando a opção do usuario e retornando.
def criar_db_inicial():

    os.system('clear')
    print(f"Para criar um banco de dados no MongoDB, é necessário inserir ao menos uma coleção e um documento, "
          f"selecione como você deseja prosseguir: \n{menus('sub_menu_1')}")

    options_menu = ('0', '1', '2')

    option_selec = input("Digite:>>> ")
    os.system('clear')

    while option_selec not in options_menu:
        os.system('clear')
        print(f'Opção {option_selec} invalida')
        print(f'\nPara prosseguir Informe uma das seguintes opções do menu:\n{menus("sub_menu_1")}')
        option_selec = input("Digite:>>> ")

    option_selec = int(option_selec)
    return option_selec

# esta função retorna um menu, que será invocado após o usuario incluir o banco.
def sub_menu_1_1():

    print(f"\n Selecione uma das seguintes opções :\n{menus('sub_menu_1_1')}")

    options_menu = ('0', '1', '2')

    option_selec = input("Digite:>>> ")

    os.system('clear')

    while option_selec not in options_menu:

        print(f'Opção {option_selec} invalida')
        print(f'\nPara prosseguir Informe uma das seguintes opções do menu:\n{menus("sub_menu_1_1")}')
        option_selec = input("Digite:>>> ")

    option_selec = int(option_selec)
    
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


    

    
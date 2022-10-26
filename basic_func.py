import pymongo
from datetime import datetime
from time import sleep
import os

conexao = pymongo.MongoClient("mongodb://localhost:27017/")

# Função com o menu de opções e submenus, será utilizado para criação do laço de repetição principal do aplicativo, 
# o menu principal e sub menu, cada sub menu esta nomeado de acordo com as opções do menu, e trazem uma funcionalidade 
# extra as opções ou a possibilidade de permanecer na funcionalidade após o fim da ação solicitada.
def menus(name):
    if name == "menu":
        return ("\n(1) - Criar banco de dados, coleções e inserir documentos. " 
                "\n(2) - Buscar documentos. " 
                "\n(3) - Deletar documentos ou coleção. " 
                "\n(4) - Listar Bancos de dados e coleções. "
                "\n(0) - Sair.\n")

    if name == "sub_menu_1":
        return ("\n(1) - Continuar."
                "\n(2) - Retornar ao menu inicial.\n ")
               

    if name == "sub_menu_2":
        return ("\n(1) - Todos os documentos. "
                "\n(2) - Informe a quantidade de documentos. "
                "\n(3) - Retornar ao menu principal.\n ")
              

    if name == "sub_menu_3":
        return ("\n(1) - Deletar documentos."
                "\n(2) - Deletar Coleção. "
                "\n(3) - Retornar ao menu principal.\n ")
              

    if name == "sub_menu_4":
        return ("\n(1) - Listar coleções. "
                "\n(2) - Retornar ao menu principal.\n ")
                

# Função de saudação, para dar Bom dia, boa tarde ou boa noite ao usuário, com base na hora atual do datetime.
def salutation():

    hour_now = datetime.now()
    hour = hour_now.hour
    hour = int(hour)

    if hour <= 11.59:
        return('Bom dia')
    if hour >= 12 and hour <= 18:
        return('Boa tarde')
    if hour > 18:
        return('Boa noite')

# Função inicial básica, para perguntar o nome do cliente e trazer uma saudação inicial.
def user_name_and_salutation():

    os.system('clear')
    print(f'Informe como gostaria de ser chamado: ')
    user_name = input("\nDigite:>>> ")
    os.system('clear')
    print(f"{salutation()} {user_name}! \n\nVou lhe auxiliar nas funções básicas de um SGBD MongoDB.")
    
# Função inicial, traz o menu principal e retorna a opção escolhida pelo cliente.
# Utilizada em varios trechos do código, ela recebe uma string e um menu, faz o print da string, traz as opções, 
# faz um filtro, evitando que o usuario insira uma informação invalida e retorna a opção escolhida
def inicial(options_menu, string):
    options_menu = options_menu
    print(string)
    option_select = input("Digite:>>> ")
    os.system('clear')
        
    while option_select not in options_menu:
        os.system('clear')
        print(f'Opção {option_select} invalida')
        print(string)
        option_select = input("Digite:>>> ")

    return option_select

# Função para padronizar o sleep, é utilizado principalmente em locais onde 
# tem uma mensagem que antecede a limpeza da tela, dando tempo para o usuario ler.
def regressive_sleep():
    print(f'Voltando ')
    for i in range(2,0,-1):
        sleep(1)
    os.system('clear')

#Função para mostrar os bancos disponiveis, utilizado em quase todas as funcionalidades.
def print_bancos():
    list_db = conexao.list_database_names()
    print('Bancos Disponiveis: \n')
    print('='*20)
    for banco in list_db:
        print(f"  {banco}")
    print('='*20)

def validade_decision(string):

    print(string)
    decision = input('\nDigite S/s(sim) ou N/n(não):>>>  ')

    list_decision = ('S', 's', 'N', 'n')

    while decision not in list_decision:
        print(string)
        print('\nDigite S ou s para sim e N ou n para não:')
        decision = input('Digite:>>> ')

    return decision

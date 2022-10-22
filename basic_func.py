from datetime import datetime
import os

# Função com o menu de opções e submenus, será utilizado para criação do laço de repetição principal do aplicativo, 
# o menu principal e sub menu, cada sub menu esta nomeado de acordo com as opções do menu, e trazem uma funcionalidade 
# extra as opções ou a possibilidade de permanecer na funcionalidade após o fim da ação solicitada.
def menus(name):
    if name == "menu":
        return ("\n1 - Criar banco de dados, " 
            "\n2 - Criar coleção, " 
            "\n3 - Inserir documentos, " 
            "\n4 - Buscar documentos, " 
            "\n5 - Deletar documentos, " 
            "\n6 - Remover coleção, "
            "\n7 - Listar Bancos de dados e coleções, "
            "\n0 - Sair.\n")

    if name == "sub_menu_1":
        return ("\n1 - Irei criar o banco de dados e automaticamente insira uma coleção e um documento com o nome teste, "
                "\n2 - Irei Criar banco de dados e nomearei a coleção e a chave e valor do documentos, "
                "\n0 - Sair.\n")

    if name == "sub_menu_1_1":
        return ("\n1 - Criar banco de dados, "
                "\n2 - Retornar ao menu principal, "
                "\n0 - Sair.\n") 

    if name == "sub_menu_2":
        return ("\n1 - Criar coleção, "
                "\n2 - Retornar ao menu principal, "
                "\n0 - Sair.\n")

    if name == "sub_menu_3":
        return ("\n1 - Inserir documento, "
                "\n2 - Retornar ao menu principal, "
                "\n0 - Sair.\n")

    if name == "sub_menu_4_1":
        return ("\n1 - 1 documento, "
                "\n2 - 5 documentos, "
                "\n3 - Todos documentos, "
                "\n4 - Informe a quantidade, "
                "\n5 - Retornar ao menu principal, "
                "\n0 - Sair.\n")

    if name == "sub_menu_4_2":
        return ("\n1 - Buscar novos documentos, "
                "\n2 - Retornar ao menu principal, "
                "\n0 - Sair.\n")

    if name == "sub_menu_5_1":
        return ("\n1 - 1 registro, "
                "\n2 - Todos registros, "
                "\n3 - Retornar ao menu principal, "
                "\n0 - Sair.\n")

    if name == "sub_menu_5_2":
        return ("\n1 - Deletar documentos, "
                "\n2 - Retornar a"
                "\n0 - Sair.\n")

    if name == "sub_menu_6":
        return ("\n1 - Deletar Coleção, "
                "\n2 - Retornar ao menu principal, "
                "\n0 - Sair.\n")

    if name == "sub_menu_7":
        return ("\n1 - Listar coleções, "
                "\n2 - Retornar ao menu principal, "
                "\n0 - Sair.\n")


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
def inicial(options_menu, string):

    options_menu = options_menu

    print(string)
    option_select = input("Digite:>>> ")

    os.system('clear')
        
    while option_select not in options_menu:
        os.system('clear')
        print(f'Opção {option_select} invalida')
        print(f'\nPara prosseguir Informe uma das seguintes opções do menu:\n{menus(menu_name)}')
        option_select = input("Digite:>>> ")

    option_select = int(option_select)

    return option_select


import pymongo
from pprint import pprint
import os
from time import sleep
from basic_func import menus, salutation, user_name_and_salutation, inicial, regressive_sleep, print_bancos, validade_decision
import func_app

conexao = pymongo.MongoClient("mongodb://localhost:27017/")
#=======================================================================================#
# função da opção 0 do menu principal:
# Função para desligar o app, é chamada em todos os sub_menus e no menu principal.

def app_off():
    os.system('clear')
    print(f'\nObrigado por utilizar nosso aplicativo. {salutation()}!\n')
    print('\nAplicativo desenvolvido por Fernando Schneider.\n')
    for time in range(5,0,-1):
        print(f'Saindo em {time}')
        sleep(1)
    os.system('clear')
    return True 

#=======================================================================================#
# Funções para execução das funcionalidades da opção 1 do menu principal, Criar bancos de dados, coleções e documentos:

# Função do menu que sera chamada em outras funções desta funcionalidade.
def menu_create_db():
    os.system('clear')
    options_menu = ('0', '1', '2')

    string = ('Você pode criar um banco de dados, uma coleção ou inserir documentos.\n'
              '\nPara criar um banco, é so inserir o nome do banco a ser criado e após digite exit. '
              '\nIrei criar um banco e adicionarei uma coleção e documento com o nome teste.\n'

              '\nPara criar uma coleção, crie ou digite o nome de um banco existente e após digite o nome da coleção a ser criada.'
              '\npor fim digite exit.\n'

              '\nPara inserir um documento, crie ou selecione banco e coleção, após digite a(s) chave(s) e valor(es).'
              '\npor fim, digite exit no campo chave para encerrar e salvar o documento no banco\n'
              '\nPara inserir um documento utilizarei a função: collection_create.insert_one({"chave": "valor"})\n'
              '\nSelecione para continuar:'
              f'{menus("sub_menu_1")}\n')

    option_selec = inicial(options_menu, string)
    return option_selec

# Função para criar bancos de dados
def create_db():

    option_selec = menu_create_db()

    if option_selec == '0':
        os.system('clear')
        app_off()

    if option_selec == "1":
        os.system('clear')
        list_db = conexao.list_database_names()
        print_bancos()
        print('Digite o nome de um dos bancos listados ou o nome do banco que deseja criar.')
        name_db = input('\nDigite:>>> ')

        if name_db not in list_db:
            string = (f'\nBanco >--- {name_db} não existe, deseja criar?\n')
            decision = validade_decision(string)

            if decision == 'N' or decision == 'n':
                print(f'Banco >--- {name_db} não foi criado!')
                regressive_sleep()
                os.system('clear')
                create_db_collection_doc()

    return name_db

    if option_selec == "2":
        func_app.app()

# Função para criar coleçõe:
def create_collection(name_db):

    db = conexao[name_db]

    name_db = name_db
    list_db = conexao.list_database_names()
    list_collections = db.list_collection_names()

    os.system('clear')
    print(f'\nColeções disponiveis no banco {name_db}:  \n{list_collections}\n')
    print('\nDigite a coleção, o nome da coleção que deseja criar ou exit para concluir e voltar ao menu inical')
    collection = input('Digite:>>> ')

    if collection == "exit":

        collection_autocreate = db['teste']

        collection_autocreate.insert_one(
            {
                "arquivo": "teste"
            }
        )
        if name_db not in list_db:
            print(f"Banco >--- {name_db} criado com sucesso!")

        regressive_sleep()
        os.system('clear')
        func_app.app()

    if collection not in list_collections:

        string = (f'\nColeção >--- {collection} não existe, deseja criar?')

        decision = validade_decision(string)

        if decision == "N" or decision == 'n':
            print('Voltando ao inicio')
            regressive_sleep()
            os.system('clear')
            create_db_collection_doc()

        collection_selec = db[collection]
        collection_selec.insert_one(
            {
                "arquivo": "teste"
            }
        )
        list_collections = db.list_collection_names()

        os.system('clear')
        print(f'\nColeções disponiveis no banco >--- {name_db} \n{list_collections}\n')

    print('\n(1) - Criar uma nova coleção \n|exit| - concluir e voltar ao inicio \n >--Qualquer tecla para inserir um documento--<\n')
    decision = input('Digite:>>> ')

    if decision == '1':
        regressive_sleep()
        os.system('clear')
        create_collection(name_db)

    if decision == "exit":
        regressive_sleep()
        os.system('clear')
        create_db_collection_doc()

    collection_selec = db[collection]

    os.system('clear')

    print(f'Você esta trabalhando no banco >--- {name_db} | coleção >--- {collection}\n')
    inserir_documento_db(collection_selec)

    string = ('\nDeseja inserir um novo documento?')

    decision = validade_decision(string)

    if decision == 'S' or decision == 's':
        os.system('clear')
        inserir_documento_db(collection_selec)

    os.system('clear')
    print('Voltando para menu inicial')
    regressive_sleep()
    func_app.app()

# Função para criar e inserir documentos.
def inserir_documento_db(colecao):

    colecao = colecao
    dicionario = {}
    fim = False

    print('\nInforme abaixo a(s) chave(s) e o(s) valor(es) que deseja inserir no documento.\nPara encerrar digite exit no campo chave.\n')

    while fim == False:
        valor_chave = input('Digite a chave:>>> ')

        if valor_chave == "exit":
            fim = True
        else:
            valor = input('Digite o valor:>>> ')
            dicionario[valor_chave] = valor

    if len(dicionario) > 0:
        colecao.insert_one(dicionario)
        print('Documento inserido com sucesso!')
    else:
        print('Documento vazio, não iserido')
        regressive_sleep()
        os.system('clear')
        # inserir_documento_db(colecao)

# Função que agrega e organiza as funções da opção 1 do menu, posteriormente sera importada no arquivo func_app

def create_db_collection_doc():
    name = create_db()
    create_collection(name)
#=======================================================================================#
# Funções de ação para funcionalidade 2 do menu principal, busca por documentos:

# Função de menu, que será chamada em outros locais desta funcionalidade
def home_menu_find():

    os.system('clear')
    options_menu = ('0', '1', '2', '3')

    string = (f'\nVocê pode visualizar todos os documentos, informar a quantidade ou ainda retornar. '
              f'\ninforme uma das opções para continuar \n{menus("sub_menu_2")}\n')

    option_selec = inicial(options_menu, string)
    return option_selec

# Função para listar os documentos, com base no limite informado pelo usuário.
def search_docs(limit):

    limit = limit

    os.system('clear')

    print_bancos()
    list_db = conexao.list_database_names()
    print('\nInforme o banco ou digite exit para retornar.\n')

    name_db = input('Digite:>>> ')
    os.system('clear')

    if name_db == 'exit':
        find_doc_collection()

    while name_db not in list_db:
        os.system('clear')
        print(f"Banco >--- {name_db} não existe.")
        print(f"\nBancos disponiveis: \n{list_db}")
        name_db = input("\ninforme um dos bancos da lista:>>> ")

    db = conexao[name_db]
    list_collections = db.list_collection_names()

    print(f"Coleções disponiveis >--- {list_collections}")
    print('\nInforme o nome da coleção')

    collection = input('Digite:>>> ')

    while collection not in list_collections:

        os.system('clear')
        print(f"Coleção {collection} não existe.")
        print(f"\nColeções disponiveis >--- {list_collection}")
        collection = input('\nInforme o nome da coleção:>>> ')

    collection_selec = db[collection]

    os.system('clear')
    print(f'Você esta trabalhando no banco >--- {name_db} | coleção >--- {collection}.\n')

    options_menu = ('1', '2')

    string = ('Deseja ver todos os documentos dessa coleção ou aplicar um filtro "chave":"valor"?\n'
    '\n(1) - Todos documentos da coleção\n(2) - Informar chave e valor\n')

    option_selec = inicial(options_menu, string)

    if option_selec == "1":
        query = collection_selec.find({}).limit(limit)

        os.system('clear')
        print(f'Documentos da coleção >--- {collection}')
        for doc in query:
            pprint(doc)
            print('\n')
        input('>--- Pressione qualquer tecla para voltar <---')
        find_doc_collection()

    if option_selec == "2":
        os.system('clear')
        print(f'Você esta trabalhando no banco >--- {name_db} | coleção >--- {collection}.\n')
        print("\nInforme a chave e o valor\n")
        key = input("Digite a chave:>>> ")
        value = input("\nDigite o valor:>>> ")
        
        query = collection_selec.find(
            {
                key:{"$eq": value}
            }
        ).limit(limit)

        count_docs_in_query = 0
        for doc in query:
            pprint(doc)
            print('\n')
            count_docs_in_query += 1

        if count_docs_in_query == 0:
            print(f'\n {key}:{value} não retornou nenhum documento.')
            regressive_sleep()
            find_doc_collection()

        input('>--- Pressione qualquer tecla para voltar <---')
        find_doc_collection()

# Função agregadora de funcionalidades, que posteriormente será chamada no arquivo func_app. A função 2, por ser menor, foi criada dentro desta,
# Algo que não fiz em outras funções principais.
def find_doc_collection():
    option_selec = home_menu_find()

    if option_selec == '0':
        os.system('clear')
        app_off()

    if option_selec == '1':
        limit = 0
        search_docs(limit)

    if option_selec == '2':

        limit = input('\nDigite o número correspondente ao limite de documentos que deseja visualizar\nDigite:>>> ')
        test_limit_is_number = str.isnumeric(limit)

        while test_limit_is_number == False:
            print(f'Informação >--- {limit} não é valida, insira somente número')
            limit = input('\nDigite o número correspondente ao limite de documentos que deseja visualizar\nDigite:>>> ')
            test_limit_is_number = str.isnumeric(limit)

        limit = int(limit)

        limit = int(limit)
        search_docs(limit)
        

    if option_selec == '3':
        func_app.app()
#=======================================================================================#
# Funções de ação para funcionalidade 3 do menu principal Drop documentos e coleções:

#função de menu da funcionalidade, será chamada em outras funções da funcionalidade 3.
def home_menu_drops():
    os.system('clear')
    options_menu = ('0', '1', '2', '3')

    string = (f'\nInforme a opção desejada.\n{menus("sub_menu_3")}')

    option_selec = inicial(options_menu, string)
    return option_selec

# Função criada para drop de documentos.
def drop_doc():

    os.system('clear')
    print('Para deletar arquivos, você deverá inserir chave e valor. \nUtilizarei a função collection_selec.delete_many({chave:{$eq:valor}}) '
          '\n\n!!!Após confirmar, todos os arquivos localizados serão excluidos!!!\n')

    print_bancos()
    list_db = conexao.list_database_names()
    print('\nInforme o banco ou digite exit para retornar.\n')

    name_db = input('Digite:>>> ')
    os.system('clear')

    if name_db == 'exit':
        drop_doc_collection()

    while name_db not in list_db:
        os.system('clear')
        print(f"Banco >--- {name_db} não existe.")
        print(f"\nBancos disponiveis: \n{list_db}")
        name_db = input("\ninforme um dos bancos da lista:>>> ")

    db = conexao[name_db]

    list_collections = db.list_collection_names()

    print(f"\nColeções disponiveis: \n{list_collections}")
    print('\nInforme o nome da coleção')
    collection = input('Digite:>>> ')

    while collection not in list_collections:
        os.system('clear')
        print(f"Coleção >--- {collection} não existe.")
        print(f"\nColeções disponiveis: \n{list_collection}")
        collection = input('\nInforme o nome da coleção:>>> ')

    collection_selec = db[collection]

    os.system('clear')
    print(f'Você esta trabalhando no banco >--- {name_db} | coleção >--- {collection}.\n')

    print('\nInforme a chave e valor para consulta e posterior exclusão dos dados')

    key = input('\nDigite a chave:>>> ')
    value = input('\nDigite o valor:>>> ')

    query = collection_selec.find(
        {
            key: {"$eq": value}
        }
    )
    os.system('clear')

    print('\nDocumentos encontrados:\n')

    count_docs_in_query = 0
    for doc in query:
        pprint(doc)
        count_docs_in_query += 1

    if count_docs_in_query == 0:
        print(f'\n {key}:{value} não retornou nenhum documento.')
        regressive_sleep()
        drop_doc()

    string = ('\nTem certeza que deseja excluir? \nDigite N/n para retornar ao inicio SEM excluir ou S/s para continuar.\n')

    decision = validade_decision(string)

    if decision == 'N' or decision == 'n':
        os.system('clear')
        drop_doc_collection()

    collection_selec.delete_many(
        {
            key: {"$eq": value}
        }
    )
    os.system('clear')
    print('Arquivos deletados')
    regressive_sleep()
    os.system('clear')
    drop_doc_collection()

# Função para apagar coleções:
def drop_collection():

    os.system('clear')
    print('Ao apagar uma coleção, você irá apagar todos os documentos contidos nela. \nSe for a unica coleção do banco, irá apagar o banco!\n')
    print_bancos()
    print('\nInforme o nome do banco para prosseguir ou digite exit para voltar \n')
    name_db = input('Digite:>>> ')

    if name_db == 'exit':
        drop_doc_collection()

    list_db = conexao.list_database_names()

    while name_db not in list_db:
        print(f'\nBanco >--- {name_db} não existe')
        print('\nInforme o nome do banco para prosseguir\n')
        name_db = input('Digite:>>> ')

    db = conexao[name_db]

    list_collections = db.list_collection_names()
    os.system('clear')
    print(f'Coleções disponiveis no banco >--- {name_db}: {list_collections}')

    print('\nInforme o nome da coleção')
    collection = input('Digite:>>> ')

    while collection not in list_collections:
        os.system('clear')
        print(f"\nColeção >--- {collection} não existe.")
        print(f"\nColeções disponiveis: \n{collection}")
        collection = input('\nInforme o nome da coleção:>>> ')

    collection_selec = db[collection]

    os.system('clear')

    query = collection_selec.find({})
    count_docs_in_query = 0

    for count in query:
        count_docs_in_query += 1

    string = (f'Você esta trabalhando no banco >--- {name_db} | coleção >--- {collection}.\n'
    f'Você tem certeza que deseja excluir a coleção >--- {collection}, ela possui {count_docs_in_query} documentos.\n')

    decision = validade_decision(string)

    if decision == 'N' or decision == 'n':
        os.system('clear')
        drop_doc_collection()

    collection_selec.drop()

    os.system('clear')
    print('Coleção deletada')
    regressive_sleep()
    os.system('clear')
    drop_doc_collection()

# Função de junção, uni e organiza as funções da funcionalidade drop, posteriormente sera chamada no arquivo func_app.
def drop_doc_collection():

    option_selec = home_menu_drops()

    if option_selec == '0':
        os.system('clear')
        app_off()

    if option_selec == '1':
        drop_doc()

    if option_selec == '2':
        os.system('clear')
        drop_collection()

    if option_selec == '3':
        func_app.app()

#=======================================================================================#
# Funções de ação para funcionalidade 4 do menu principal, busca de bancos e coleções:

# Menu inical da funcionalidade, será invocado em outros momentos.
def home_menu_consult():
    options_menu = ('0', '1', '2')
    string = f"\nPara prosseguir Informe uma das seguintes opções do menu:{menus('sub_menu_4')}"
    option_selec = inicial(options_menu, string)
    return option_selec

# Sub menu de consultas, recebe a opção informada no meu e aplica as buscas
def sub_menu_consult(option_selec):
    if option_selec == '0':
        os.system('clear')
        app_off()

    if option_selec == '1':
        os.system('clear')
        print_bancos()
        list_db = conexao.list_database_names()
        
        print("\nDigite nome do banco para qual deseja consultar a(s) coleção(ões):>>> ")
        
        name_db = input('Digite:>>> ')

        while name_db not in list_db:
            os.system('clear')
            print(f"Banco >--- {name_db} não existe.")
            print(f"\nBancos disponiveis: \n{list_db}\n\nDigite nome do banco para qual deseja consultar a(s) coleção(ões)")
            name_db = input("Digite>>> ")

        banco = conexao[name_db]
        list_collections = banco.list_collection_names()
        os.system('clear')
        print(f"\nColeções do banco >--- {name_db}: \n{list_collections}")

        option = home_menu_consult()
        sub_menu_consult(option)

    if option_selec == '2':
        os.system('clear')
        func_app.app()

# Monta e organiza as funções, posteriormente será chamada no arquivo func_app.
def list_db_collections():
    print_bancos()
    option_selec = home_menu_consult()
    sub_menu_consult(option_selec)

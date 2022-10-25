import pymongo
import pprint
import os
from time import sleep
from basic_func import menus, salutation, user_name_and_salutation, inicial
import func_app
import func_options

conexao = pymongo.MongoClient("mongodb://localhost:27017/")


os.system('clear')

print('Você pode criar um banco de dados, uma coleção ou inserir documentos.\n')
print('\nPara criar um banco, é so inserir o nome do banco a ser criado e após digite exit. '
'\nIrei criar um banco e adicionarei uma coleção e documento com o nome teste.\n')

print('\nPara criar uma coleção, crie ou digite o nome de um banco existente e após digite o nome da coleção a ser criada.'
'\npor fim digite exit.\n')

print('\nPara inserir um documento, crie ou selecione banco e coleção, após digite a(s) chave(s) e valor(es).'
'\npor fim, digite exit no campo chave para encerrar e salvar o documento no banco\n'
'\nPara inserir um documento utilizarei a função: collection_create.insert_one({"chave": "valor"})\n')

input('\nAperte qualquer tecla para continuar:>>> \n')

os.system('clear')

func_options.print_bancos()



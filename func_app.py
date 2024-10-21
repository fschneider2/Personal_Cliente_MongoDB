import func_options
import basic_func 
import gc
import os
from time import sleep


# função da opção 0 do menu principal:
# Função para desligar o app, é chamada em todos os sub_menus e no menu principal.

def app_off():
   gc.collect()
   os.system('clear')
   print(f'\nObrigado por utilizar nosso aplicativo. {basic_func.salutation()}!\n')
   print('\nAplicativo desenvolvido por Fernando Schneider.\n')
   sleep(3)
   os.system('clear')
   return True 

# Função que recebe as funcões do arquivo func_options e do basic_func
def app():
   gc.collect()
   app_on_off = False

   while app_on_off == False:

      options_menu = ('0','1','2','3','4')

      string = f'\nPara prosseguir Informe uma das seguintes opções do menu:\n{basic_func.menus("menu")}'
        
      opcao_menu_principal = basic_func.inicial(options_menu, string)

      if opcao_menu_principal == '0':
         gc.collect()
         app_on_off = app_off()

      elif opcao_menu_principal == '1':
         gc.collect()
         app_on_off = func_options.create_db_collection_doc()
        
      elif opcao_menu_principal == '2':
         gc.collect()
         app_on_off = func_options.find_doc_collection()

      elif opcao_menu_principal == '3':
         gc.collect()
         app_on_off = func_options.drop_doc_collection()

      else:
         gc.collect()
         app_on_off = func_options.list_db_collections()



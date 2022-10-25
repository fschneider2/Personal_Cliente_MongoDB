from func_options import app_off, create_db_collection_doc, list_db_collections, menus, drop_doc_collection, find_doc_collection
from basic_func import inicial

def app():
    
    app_on_off = False
    while app_on_off == False:

        options_menu = ('0','1','2','3','4')

        string = f'\nPara prosseguir Informe uma das seguintes opções do menu:\n{menus("menu")}'
        
        opcao_menu_principal = inicial(options_menu, string)

        if opcao_menu_principal == '0':
            os.system('clear')
            app_on_off = app_off()

        if opcao_menu_principal == '1':
            app_on_off = create_db_collection_doc()
        
        if opcao_menu_principal == '2':
            app_on_off = find_doc_collection()

        if opcao_menu_principal == '3':
            app_on_off = drop_doc_collection()

        if opcao_menu_principal == '4':
            app_on_off = list_db_collections()



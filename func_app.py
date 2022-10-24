from func_options import app_off, criar_db, criar_colecao, listar_bancos_colecoes, menus, inserir_documento
from basic_func import inicial

def app():
    
    app_on_off = False
    while app_on_off == False:

        options_menu = ('0','1','2','3','4','5','6','7','8')

        string = f'\nPara prosseguir Informe uma das seguintes opções do menu:\n{menus("menu")}'
        
        opcao_menu_principal = inicial(options_menu, string)

        if opcao_menu_principal == 0:
            app_on_off = app_off()

        if opcao_menu_principal == 1:
            app_on_off = criar_db()

        if opcao_menu_principal == 2:
            app_on_off = criar_colecao()

        if opcao_menu_principal == 3:
            app_on_off = inserir_documento()

        if opcao_menu_principal == 7:
            app_on_off = listar_bancos_colecoes()



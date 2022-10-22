from func_options import app_off, criar_db
from basic_func import inicial

def app():
    app_on_off = False
    while app_on_off == False:
        
        opcao_menu_principal = inicial()

        if opcao_menu_principal == 0:
            app_on_off = app_off()

        if opcao_menu_principal == 1:
            app_on_off = criar_db()
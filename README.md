# Trabalho final do modulo Banco de dados 2 do cusro Data Science da escola Growdev.  
>--- https://www.growdev.com.br/

# Esta aplicação traz algumas funcionalidades básicas de um cliente MongoDb, como o mongoDb Compass, por exemplo.

# É um projeto de estudo, sem aplicação real, porém desenvolvido com muita dedicação, trabalhei bastante nos detalhes. Desenvolvido para avaliação e como portfolio.

# É uma aplicação criada com base em um menu e sub menus, funciona em loop, ou seja, so encerra quando o usuario solicitar, e todas as funcionalidades respondem no banco localhost.

### Requisitos para rodar esse aplicativo:

>-- Possuir MongoDb instalado e ativo em sua maquina.(https://www.mongodb.com/try/download/community)
>-- Ter a biblioteca pymongo instalada.
>-- baixar todos os arquivos deste repositorio. 
>-- Utilizei pymongo.MongoClient("mongodb://localhost:27017/") como padrão, caso sua conecção seja diferente, altere essa informação nos arquivos basic_func.py linha 5 e func_options.py linha 8.
<!-- Rode o arquivo app.py em seu VsCode ou terminal-->
<!-- em linux ubuntu jammy(22.04) eu acesso o terminal, vou ate a pasta onde os arquivos estão salvos, acesso o python utilizando >>>python3, após dou o comando >>>exec(open("app.py").read()) -->

>----------------------------------------------------------------<
# Informação sobre os arquivos presentes neste repositorio.
# Acesse os arquivos para mais informações.

>--- basic_func.py:
<!-- Arquivo com funções básicas e presente em todo o código, como menus, saudação e print's comuns a varias funções. -->

>--- func_options.py
<!-- Neste arquivo consta todas as funções referentes as funcionalidades, esta dividido entre as 5 prinicpais funcionalidades da aplicação.
0 - desligar o app,
1 - Criar
2 - Consultar docs
3 - Deletar 
4 - Listar Bancos e coleções -->

>--- func_app.py
<!-- Nele consta a junção das funções do func_options.py, ele quem define o loop e o aplica a função desligar. -->

>--- App.py
<!-- É o arquivo que junta, que recebe a função do arquivo func_app.py e do basic func.py, este é o arquivo que você deve rodar, este é o aplicativo, os o restante é a construção e arquivos de sistema.  -->

<!-- !!!Todas as atividades que fizer dentro da aplicação serão aplicadas no banco localhost!!! -->









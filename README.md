
# Trabalho final do modulo Banco de dados 2 do curso Data Science da escola Growdev.  
- https://www.growdev.com.br/

Versão - 1.1 - 27/10/2022

Esta aplicação traz funcionalidades básicas de um cliente MongoDB.

Este é um projeto de estudo, sem aplicação real, porém desenvolvido com muita dedicação,onde trabalhei bastante nos detalhes. Foi desenvolvido para avaliação do modulo e como portfolio.

A aplicação foi criada com base em um menu e sub menus, funciona em loop, ou seja, so encerra quando o usuario solicitar, e todas as funcionalidades são aplicadas no localhost.


## Autores

- [Fernando Schneider](www.linkedin.com/in/fernando-schneiderdev)


## Stack utilizada

Back-end: Python, MongoDB, PyMongo, Terminal

## Funcionalidades

O programa deve ser implementado em Python
Deve ser utilizado o banco MongoDB como banco NoSQL. Não serão aceitos outros bancos de dados.
Pode utilizar quantos arquivos julgar necessário.
Procure organizar o código da melhor forma possível.
O programa deverá fornecer ao usuário as seguintes opções.

- a) Criar um ou mais banco de dados, com o nome fornecido pelo usuário.

- b) Criar uma ou mais coleções, com o nome fornecido pelo usuário.

- c) Inserir documentos.

    Deverá ser pedido ao usuário, qual a coleção onde deve ser inserido.
    Pedir quais os pares de chave-valor a serem inseridos em cada documento.

- d) Buscar documentos.

    O usuário deve escolher se busca por todos os documentos, ou se quer aplicar algum filtro (critério de seleção), e nesse caso ele deve fornecer a chave e o valor correspondente do filtro. Obs: apenas são permitidos testes de igualdade e apenas um filtro para busca.
    Forneça a opção de limitar a busca a uma quantidade informada de registros.

- e) Deletar documentos.

    O Usuário deve fornecer qual as chaves utilizadas na condição da remoção e qual o valor correspondente para encontrar o(s) registros a serem deletados. Obs: apenas será considerado o teste de igualdade para encontrar registros e um único filtro para encontrar os registros a serem deletados.
- f) Remover coleções.

- g) Listar bancos de dados.

- h) Listar coleções de um banco de dados.

## Configurações para o uso

>-- Possuir MongoDb instalado e ativo em sua maquina.(https://www.mongodb.com/try/download/community)

>-- Ter a biblioteca pymongo instalada.

>-- Baixar todos os arquivos deste repositorio. 

>-- Como configuração de acesso pelo pymongo utilizei "pymongo.MongoClient("mongodb://localhost:27017/")" , caso sua conecção seja diferente, altere essa informação nos arquivos basic_func.py linha 5 e func_options.py linha 8.

-- Rode o arquivo app.py em seu VsCode, editor ou terminal

-- Em linux ubuntu jammy(22.04) por exemplo, eu acesso o terminal, vou ate a pasta onde os arquivos estão salvos, acesso o python utilizando o comando >>>python3, após utilizo o comando >>>exec(open("app.py").read())

## Aprendizados

O que você aprendeu construindo esse projeto? Quais desafios você enfrentou e como você superou-os?

Com essa aplicação aprendi sobre varias funções python, back end e interação do banco de dados direto na aplicação:

    -gc.collect(), pymongo, pprint() e suas funcionalidades;

    -importancia de uma boa organização do codigo 

    -A importancia de utilizar o del, para limpar variaveis;

    -A importancia e funcionalidade do Try, except e correção de erros;

    -Aprimorei meus conhecimentos em Python;

    -Aprofundei meus conhecimentos em MongoDB;

    -Uma boa experiencia com um projeto, que mesmo com poucas funcionalidades,
    fiz tudo sozinho, buscando corrigir erros, incluindo loops, refatorando,
    fazendo todos os teste...;



## Documentação

- Fiz um viideo de apresentação as funções e arquivos:

 - https://www.youtube.com/watch?v=xlbg9PPMC7A

--> Após a gravação do video foi alterado:

    Incluindo função gc.collect() em todo código, juntamente com o del 'nome da variavel', para que, após o uso das variaveis e uso das funcionalidades,        o sitema limpe a memoria e apague as variaveis, evitando uso indevido ou erros ao terminar a aplicação. Após o usuario criar um banco, ao digitar        exit para retornar, ou, após o usuario ir até a opção de excluir coleções e retornar sem confirmar a exclusão, ao sair da aplicação, ele executava        ações indevidas, isso foi corrigido com o uso do del e gc.collect();
    
    alterado a pasta de localização da função app_off(), agora esta em func_app.py;
    
    Alterado funções da funcionalidade 1, código esta mais limpo e facil de compreender.
    
    Adicionado contador de documentos na consulta as coleções, opção 4 do menu principal. 
    
    Versão 1.0 apresentava so o nome das coleções.
    
    Versão 1.1 apresenta o nome das coleções e a quantidade de documentos presentes em cada coleção.

### Informações básicas sobre os arquivos da aplicação:

- basic_func.py:

Arquivo com funções básicas e presente em todo o código, como menus, saudação e print's comuns a varias funções.

- func_options.py

Neste arquivo consta todas as funções referentes as funcionalidades, esta dividido entre as 5 prinicpais funcionalidades da aplicação.

0 - desligar o app,

1 - Criar

2 - Consultar docs

3 - Deletar 

4 - Listar Bancos e coleções 

- func_app.py

Nele consta a junção das funções do func_options.py, ele quem define o loop e o aplica a função desligar.

- App.py

É o arquivo que monta, que recebe a função do arquivo func_app.py e do basic func.py, este é o arquivo que você deve rodar, este é o aplicativo, os o restante é a construção e arquivos de sistema.

<--!!!Todas as atividades que fizer dentro da aplicação serão aplicadas no banco localhost!!!-->


## Contribuindo

Contribuições são sempre bem-vindas!

Você pode me contatar em fernandosc@feevale.br ou fernandosc.dev@gmail.com

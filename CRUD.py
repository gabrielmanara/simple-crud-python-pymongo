import os
from apoiador import apoiador
from connection import connection
#!/usr/bin/python

#INSTÂNCIAS DE CLASSE#####################################################################################
objConn = connection()

objApoiador = apoiador(objConn.db, objConn.client, objConn.collection)


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

# FUNCOES
def menuInsert():
    print('____________________________________')
    objApoiador.apoiador_id = input('| ID: ')
    print('____________________________________')
    objApoiador.apoiador_imagem = input('| Imagem:  ')
    print('____________________________________')
    objApoiador.apoiador_name = input('| Name:   ')
    print('____________________________________')


opcao = 0
while (opcao < 5):
    print('+-----------------------------------------------------------+')
    print('|              Apoiador DEVNAESTRADA                    |')

    print('\n')
    print('__________________________________')
    print('| 1 - Incluir Apoiador           |')
    print('__________________________________')
    print('| 2 - Alterar Apoiador           |')
    print('__________________________________')
    print('| 3 - Listar Apoiador            |')
    print('__________________________________')
    print('| 4 - Excluir Apoiador           |')
    print('__________________________________')
    print('| 5 - Sair                       |')
    print('__________________________________')
    opcao = int(input('\nEscolha a opcao desejada '))

    if(opcao == 1):
        menuInsert()
        objApoiador.insert()
        if objApoiador.HasError:
            print(objApoiador.MsgError)
        else:
            print('Dados inseridos com sucesso.')
            limpar()
    if(opcao == 2):
        print('______________Alterar Apoiador____________\n')
        objApoiador.listarApoiador(0)

        pCodigo = int(input('\nDigite o código do Apoiador: '))
        objApoiador.listarApoiador(pCodigo)
        menuInsert()
        objApoiador.update(pCodigo)

    if(opcao == 3):
        objApoiador.listarApoiador(0)

    if (opcao == 4):
        print('______________Deletar Apoiador____________\n')
        objApoiador.listarApoiador(0)

        pCodigo = int(input('\nDigite o código do Apoiador: '))
        objApoiador.delete(pCodigo)



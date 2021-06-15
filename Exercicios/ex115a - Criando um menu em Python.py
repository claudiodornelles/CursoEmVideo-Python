"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""
from time import sleep


def titulo(prompt=None, color='null'):
    tam = 40
    print(f'{cores_texto[color]}-' * tam, f'{cores_texto["null"]}')
    if prompt != None:
        print(f'{cores_texto[color]}{prompt.center(tam)}')
        print('-' * tam, f'{cores_texto["null"]}')


def menu():
    titulo('MENU PRINCIPAL', 'amarelo')
    print(f'{cores_texto["amarelo"]}1{cores_texto["null"]} - {cores_texto["azul"]}Ver pessoas cadastradas{cores_texto["null"]}')
    print(f'{cores_texto["amarelo"]}2{cores_texto["null"]} - {cores_texto["azul"]}Cadastrar nova pessoa{cores_texto["null"]}')
    print(f'{cores_texto["amarelo"]}3{cores_texto["null"]} - {cores_texto["azul"]}Sair do sistema{cores_texto["null"]}')
    titulo(color='amarelo')


def opcao():
    while True:
        try:
            op = int(input(f'{cores_texto["null"]}Sua opção: {cores_texto["null"]}'))
        except:
            print(f'{cores_texto["vermelho"]}ERRO! Digite uma opção válida.{cores_texto["null"]}')
            titulo()
        else:
            if 0 < op < 4:
                break
            else:
                print(f'{cores_texto["vermelho"]}ERRO! Digite uma opção válida.{cores_texto["null"]}')
                titulo()
    return op


def leiaIdade(prompt='Idade: '):
    while True:
        try:
            idade = int(input(prompt))
        except:
            print(f'{cores_texto["vermelho"]}ERRO! Digite uma idade válida.{cores_texto["null"]}')
        else:
            if idade > 0:
                break
            else:
                print(f'{cores_texto["vermelho"]}ERRO! Digite uma idade válida.{cores_texto["null"]}')
    return idade


cores_texto = {'null': '\033[m',
               'branco': '\033[30m',
               'vermelho': '\033[31m',
               'verde': '\033[32m',
               'amarelo': '\033[33m',
               'azul': '\033[34m',
               'magenta': '\033[35m',
               'ciano': '\033[36m',
               'cinza': '\033[37m'}


while True:
    menu()
    op = opcao()
    sleep(0.35)
    if op == 1:
        try:
            open('cadastro.txt', 'r+')
        except:
            open('cadastro.txt', 'w+')
        else:
            titulo('PESSOAS CADASTRADAS', color='amarelo')
            sleep(0.35)
            i = 1
            with open('cadastro.txt', 'r') as file:
                for line in file:
                    print(f'{line}', end='')
                    i += 1
                print()
                sleep(1)
    elif op == 2:
        try:
            open('cadastro.txt', 'r+')
        except:
            open('cadastro.txt', 'w+')
            print('Criei o arquivo.')
        else:
            titulo('NOVO CADASTRO', 'verde')
            nome = str(input('Nome: ')).strip().title()
            idade = leiaIdade()
            with open('cadastro.txt', 'a') as file:
                file.write(f'\n{nome.ljust(30)}{idade} anos')
            print(f'Novo registro de {cores_texto["amarelo"]}{nome}{cores_texto["null"]} adicionado.')
            sleep(1)
    if op == 3:
        titulo('Saindo do sistema... Até logo!', 'vermelho')
        sleep(1)
        break

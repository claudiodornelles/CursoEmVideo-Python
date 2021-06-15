from ex115_files import cores, leia
from time import sleep


def titulo(prompt=None, color='null'):
    tam = 40
    print(f'{cores.texto[color]}-' * tam, f'{cores.texto["null"]}')
    if prompt != None:
        print(f'{cores.texto[color]}{prompt.center(tam)}')
        print('-' * tam, f'{cores.texto["null"]}')


def menu(options: list() = 'None'):
    titulo('MENU PRINCIPAL', 'amarelo')
    i = 1
    for option in options:
        print(f'{cores.texto["amarelo"]}{i}{cores.texto["null"]} - {cores.texto["azul"]}{option}{cores.texto["null"]}')
        i += 1
    titulo(color = 'amarelo')


def escolha(options: list() = 'None'):
    while True:
        try:
            op = int(input(f'{cores.texto["null"]}Sua opção: {cores.texto["null"]}'))
        except:
            print(f'{cores.texto["vermelho"]}ERRO! Digite uma opção válida.{cores.texto["null"]}')
            titulo()
        else:
            if op in range(1, len(options) + 1):
                break
            else:
                print(f'{cores.texto["vermelho"]}ERRO! Digite uma opção válida.{cores.texto["null"]}')
                titulo()
                sleep(1)
    return op - 1


def exibirDados(file_name):
    try:
        open(file_name, 'rt')
    except:
        open(file_name, 'w+')
    else:
        titulo('PESSOAS CADASTRADAS', color='amarelo')
        sleep(1)
        file = open(file_name, 'rt')
        for line in file:
            dado = line.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>10}')
        sleep(2)


def novoCadastro(file_name):
    try:
        open(file_name, 'r')
    except:
        open(file_name, 'w+')
    else:
        titulo('NOVO CADASTRO', 'verde')
        sleep(1)
        nome = str(input('Nome: ')).strip().title()
        sleep(0.5)
        idade = leia.idade()
        with open(file_name, 'a') as file:
            file.write(f'{nome};{idade} anos\n')
        print(f'Novo registro de {cores.texto["amarelo"]}{nome}{cores.texto["null"]} adicionado.')
        sleep(1)

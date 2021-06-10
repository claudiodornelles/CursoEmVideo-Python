"""
Faça um mini-sistema que utilize o InteractiveHelp do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
OBS: Use cores.
"""
from time import sleep

def ajuda(com):
    sleep(0.35)
    titulo(f'Acessando o manual de "{comando}"', 3)
    print(c[5], end='', flush=True)
    help(com)
    print(c[0], flush=True)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor],'~' * tam, c[0])
    print(c[cor],f'  {msg}  ', c[0])
    print(c[cor],'~' * tam, c[0])


c = ('\033[m',  # 0 sem cores
     '\033[0;30;41m',  # 1 vermelho
     '\033[0;30;42m',  # 2 verde
     '\033[0;30;45m',  # 3 magenta
     '\033[0;30;46m',  # 4 ciano
     '\033[7;40m')  # 5 branco

while True:
    titulo('SISTEMA DE AJUDA - PyHelp', 2)
    print('\033[32m', end='')
    comando = str(input('- Função ou Biblioteca -> ')).strip()
    print(c[0])

    if comando.upper() not in 'FIM':
        ajuda(comando)
    else:
        break
titulo('Até logo!', 1)

"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indica o número a calcular e o segundo chamado SHOW, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial
"""
from time import sleep

def fatorial(n: int, show=False):
    """
    -> Calcula o Fatorial de um número.

    :param n: O número a ser calculado.
    :param show: (Opcional) Mostra na tela o processo de cálculo.
    :return: O valor do Fatorial de um número 'n'.
    """
    f = 1
    for i in range(n, 0, -1):
        if show:
            if i > 1:
                print(f'{i} x ', end='', flush=True)
            else:
                print(f'{i} = ', end='', flush=True)
        f *= i
        sleep(0.3)
    return f
    

while True:
    try:
        num = int(input('Digite um número para saber o seu fatorial: '))
    
    except:
        print('Número inválido, tente novamente.')
        continue

    if num >= 0:
        break
    else:
        print('Não existe fatorial de número negativo, tente novamente.')

while True:
    resp = str(input('Deseja mostrar o processo de cálculo? [S/N] ')).upper().strip()[0]

    if resp in 'SN':
        break
    else:
        print('Não entendi. Por favor, tente novamente.')

if resp == 'S':
    show = True
else:
    show = False

print('-='*30)
print(fatorial(num, show))

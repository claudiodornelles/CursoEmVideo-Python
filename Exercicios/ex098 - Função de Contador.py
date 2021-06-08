'''
Faça um programa que tenha uma função chamada contador() que receba três parâmetros: início, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1.
b) De 10 até 0, de 2 em 2.
c) Uma contagem personalizada.
'''

from time import sleep

def contador(init, end, step):
    if step < 0:
            step = - step
    if step == 0:
        step = 1

    print('-='*30)
    print(f'Contagem de {init} até {end} de {step} em {step}:')
    sleep(1)
    if init < end:
        while init <= end:
            print(f'{init} ', end='', flush=True)
            sleep(0.5)
            init += step
            
    elif init > end:
        while end <= init:
            print(f'{init} ', end='', flush=True)
            sleep(0.5)
            init -= step
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
while True:
    try:
        inicio = int(input('Início: '))

    except:
        print('Não entendi, por favor digite um número inteiro.')
        continue
    
    break
while True:
    try:
        fim = int(input('Fim: '))

    except:
        print('Não entendi, por favor digite um número inteiro.')
        continue
    
    break
while True:
    try:
        passo = int(input('Passo: '))

    except:
        print('Não entendi, por favor digite um número inteiro.')
        continue
    
    break

contador(inicio, fim, passo)

"""
Faça um programa que tenha uma função chamada maior() que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep

def maior(* numeros: float):
    """
    -> Cálcula o maior número informado em uma sequência de números digitados.

    :param numeros: Não aceita listas
    """


    print('-='*30)
    print('Analisando os valores passados...')
    if len(numeros) != 0:
        maior = numeros[0]
        for numero in numeros:
            if numero > maior:
                maior = numero
            print(f'{numero} ', end='', flush=True)
            sleep(.5)
        print()
    else:
        maior = 0
    print(f'Foram informados {len(numeros)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

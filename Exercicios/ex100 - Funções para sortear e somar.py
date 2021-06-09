"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e colocá-los dentro da lista. A segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
"""

from random import randint
from time import sleep


def sorteia(lista: list):
    """
    -> Sorteia 5 valores, guarda em uma lista e mostra os valores na tela.
    
    :param lista: Variável que irá estocar os valores sorteados.
    """


    print(f'Sorteando 5 valores: ', end='')
    for i in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[i], end=' ', flush=True)
        sleep(0.3)
    print('Pronto!')

def somaPar(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    print(f'Somando os valores pares de {lista}, temos {soma}.')


numeros = []
sorteia(numeros)
somaPar(numeros)

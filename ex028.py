"""
Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
from time import sleep
escolha = 'S'
while escolha == 'S':
    num = randint(0, 5)
    print('-=-' * 22)
    print('Vou pensar em um número entre 0 e 5 e você pode tentar adivinhar')
    print('-=-' * 22)
    tentativa = int(input('Em qual número pensei? '))
    print("PROCESSANDO...")
    sleep(1)
    if tentativa == num:
        print(f'Vocé é um gênio! Eu realmente pensei no número {num}!')
    else:
        print(f'Infelizmente você errou... O número que pensei foi o {num}.')
    escolha = input('Quer tentar novamente? (S/N)').upper()
    if not escolha or escolha != 'S':
        print('Tudo bem, jogamos novamente mais tarde!')
        break

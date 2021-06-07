"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep

numeros = []
jogos = []

print('-'*35)
print(f'{"JOGO DA MEGA SENA":^35}')
print('-'*35)

n_jogos = int(input('Quantos jogos você deseja criar? '))

if n_jogos == 1:
    print(f'-=-=-=-=- SORTEANDO 1 JOGO -=-=-=-=-')
else:
    print(f' -=-=-=-=- SORTEANDO {n_jogos} JOGOS -=-=-=-=-')

for i in range(0,n_jogos):
    for j in range(0,6):
        while True:
            numero = randint(1,60)
            if numero not in numeros:
                numeros.append(numero)
                break
    jogos.append(numeros[:])
    sleep(0.5)
    print(f'Jogo {i + 1}: {sorted(jogos[i])}')
    numeros.clear()
print(f'-=-=-=-=-=-=< BOA SORTE! >=-=-=-=-=-=-')
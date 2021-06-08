"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep

jogadores = {'Jogador 1':randint(1,6),
             'Jogador 2':randint(1,6),
             'Jogador 3':randint(1,6),
             'Jogador 4':randint(1,6)}

print('== Valores sorteados ==')
sleep(0.75)
for chave, valor in jogadores.items():
    print(f'  O {chave} tirou {valor}')
    sleep(0.75)

print()
print(' == Ranking dos jogadores == ')

jogadores_cp = jogadores.copy()
ranking = []
temp = []
rep = 0

for i in jogadores:
    for chave, valor in jogadores_cp.items():

        if rep == 0:
            maior_valor = valor
            maior_jogador = chave
        elif valor > maior_valor:
            maior_valor = valor
            maior_jogador = chave
        rep += 1

    rep = 0
    temp.append(maior_jogador)
    temp.append(maior_valor)
    ranking.append(temp[:])
    temp.clear()
    del jogadores_cp[maior_jogador]

for pos, jogador in enumerate(ranking):
    sleep(0.75)
    print(f'  {pos + 1}º lugar: {jogador[0]} com {jogador[1]}')
print()

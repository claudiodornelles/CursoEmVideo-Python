"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e a quantidade de partidas que ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluíndo o total de gols feitos durante o campeonato.
"""

jogador = {}
partidas = []
gols = total_gols = 0

jogador['Nome'] = str(input('Nome do Jogador: ')).strip().title()
tot_partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for p in range(0, tot_partidas):
    gols = int(input(f'Quantos gols {jogador["Nome"]} fez na partida {p + 1}? '))
    partidas.append(gols)
    total_gols += gols

jogador['Gols'] = partidas[:]
jogador['Total'] = total_gols

print('-='*30)
print(jogador)
print('-='*30)
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}.')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {tot_partidas} partidas.')
for np, ng in enumerate(partidas):
    if ng == 0:
        print(f'=> Na partida {np + 1}, não fez nenhum gol.')
    elif ng == 1:
        print(f'=> Na partida {np + 1}, fez {ng} gol.')
    else:
        print(f'=> Na partida {np + 1}, fez {ng} gols.')
print(f'Foi um total de {total_gols} gols.')
print()

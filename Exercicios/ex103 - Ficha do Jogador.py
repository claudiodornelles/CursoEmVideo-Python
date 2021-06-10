"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""

def ficha(nome="<desconhecido>", gols=0):
    
    if gols == 0:
        print(f'O jogador {nome} não fez gols no campeonato.')
    elif gols == 1:
        print(f'O jogador {nome} fez {gols} gol no campeonato.')
    elif gols > 1:
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-='*30)
n = str(input('Nome do Jogador: ')).strip().title()
g = str(input('Número de Gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gols = g)
else:
    ficha(n, g)

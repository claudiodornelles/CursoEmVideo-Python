"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela com a formatação correta.
"""

matriz = [[],[],[]]

for i in range(0,3):
    for j in range(0,3):
        n = int(input(f'Digite um valor para [{i}, {j}]: '))
        matriz[i].append(n)

print('-='*30)

for i in range(0, 3):
    for j in range(0,3):
        if j != 2:
            print(f'[{matriz[i][j]:^6}]', end='')
        else:
            print(f'[{matriz[i][j]:^6}]')
print()
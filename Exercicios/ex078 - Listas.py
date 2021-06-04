"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

n = []
pos_maior = []
pos_menor = []
i = j = maior = menor = 0

for i in range(0,5):
    n.append(int(input(f"Digite um valor para a posição {i}: ")))
    if i == 0:
        maior = n[i]
        menor = n[i]
    else:
        if n[i] > maior:
            maior = n[i]
        if n[i] < menor:
            menor = n[i]

for i, j in enumerate(n):
    if j == maior:
        pos_maior.append(i)
    elif j == menor:
        pos_menor.append(i)

print("-="*25)
print(f'Você digitou os valores {n}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')

for pos in pos_maior:
    print(f'{pos}... ', end='')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')

for pos in pos_menor:
    print(f'{pos}... ', end='')

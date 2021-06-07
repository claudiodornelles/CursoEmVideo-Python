"""
Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
1 - Quantas pessoas foram cadastradas.
2 - Uma listagem com as pessoas mais pesadas.
3 - Uma listagem com as pessoas mais leves.
"""

pessoas = []
lista_aux = []
maior_peso = menor_peso = 0

while True:
    lista_aux.append(str(input('Nome: ')))
    lista_aux.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior_peso = lista_aux[1]
        menor_peso = lista_aux[1]
    else:
        if lista_aux[1] > maior_peso:
            maior_peso = lista_aux[1]
        if lista_aux[1] < menor_peso:
            menor_peso = lista_aux[1]

    pessoas.append(lista_aux[:])
    lista_aux.clear()

    while True:
        resposta = str(input('Deseja continuar? [S/N] '))
        if resposta in 'SsNn':
            break
    
    if resposta in 'Nn':
        break

print('-='*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

print(f'O maior peso foi de {maior_peso}kg. Peso de ', end='')

for i in range(0, len(pessoas)):
    if pessoas[i][1] == maior_peso:
        print(f'{pessoas[i][0]}, ', end='')

print('\b\b.')

print(f'O menor peso foi de {menor_peso}kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor_peso:
        print(f'{pessoa[0]}, ', end='')
print('\b\b.')
print()

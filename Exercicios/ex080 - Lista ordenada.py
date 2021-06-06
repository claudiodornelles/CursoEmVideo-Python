"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem utilizar o comando sort()).
No final, mostre a lista ordenada na tela.
"""
lista = []

for i in range(0,5):

    n = int(input('Digite um número: '))

    if i > 0:
        for i, j in enumerate(lista):
            if n > j and n > lista[i + 1]:
                break


print(f'Você digitou os números: {lista}')

lista.insert
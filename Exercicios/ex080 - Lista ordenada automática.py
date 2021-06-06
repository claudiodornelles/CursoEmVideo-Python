"""

Criar uma lista de números ordenada automáticamente

"""
numeros = []

for i in range(0,5):
    numero = int(input('Digite um valor: '))
    if i == 0 or numero > numeros[-1]:
        numeros.append(numero)
        print('Adicionado ao final da lista...')
    else:
        for posicao, valor in enumerate(numeros):
            if numero < valor:
                numeros.insert(posicao, numero)
                print(f'Adicionado na posição {posicao} da lista...')
                break
print('-='*30)
print(f'Os valores digitaos em ordem foram {numeros}')

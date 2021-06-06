"""

Criar uma lista de números ordenada automáticamente

"""
numeros = []
adicionado = False

for i in range(0,5):
    numero = int(input('Digite um valor: '))
    adicionado = False
    if i == 0:
        numeros.append(numero)
        adicionado = True
        print('Adicionado ao final da lista...')
    else:
        for posicao, valor in enumerate(numeros):
            if numero < valor:
                numeros.insert(posicao, numero)
                adicionado = True
                print(f'Adicionado na posição {posicao} da lista...')
                break
        if not adicionado:
            numeros.append(numero)
            adicionado = True
            print('Adicionado ao final da lista...')
print('-='*30)
print(f'Os valores digitaos em ordem foram {numeros}')
#se o número for o maior, ele entra no final.
#se não, entra no meio
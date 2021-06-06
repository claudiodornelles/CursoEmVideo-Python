"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""

numeros = []
pares = []
impares = []

while True:
    try:
        numero = int(input('Digite um valor: '))

    except:
        print('Não entendi... ', end='')
        continue
    
    numeros.append(numero)

    while True:
        resp = str(input('Deseja continuar? [S/N] '))
        if resp in 'SsNn':
            break
        print('Não entendi... ', end='')
    
    if resp in 'Nn':
        break

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

numeros.sort()
pares.sort()
impares.sort()

print('-='*30)

print(f'Os números digitados foram: {numeros}')
print(f'Os números PARES digitados foram: {pares}')
print(f'Os números ÍMPARES digitados foram: {impares}')

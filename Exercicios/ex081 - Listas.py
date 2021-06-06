"""
Crie um programa que vai ler vários números (deseja continuar?) e colocar em uma lista.
Depois disso, mostre:
1 - Quantos números foram digitados?
2 - A lista de valores ordenada de forma decrescente.
3 - Se o valor 5 foi digitado e está ou não na lista.
"""

numeros = []

while True:
    try:
        numero = int(input('Digite um número: '))
    except:
        continue

    numeros.append(numero)

    while True:
        resp = str(input('Deseja continuar? [S/N] '))

        if resp in 'SsNn':
            break

    if resp in 'Nn':
        break
    
print('-='*30)
print(f'Você digitou {len(numeros)} números.')
numeros.sort()
print(f'Os valores em ordem decrescente são {numeros[::-1]}')
if 5 in numeros:
    print('O número 5 faz parte da lista!')
else:
    print('O número 5 não foi encontrado na lista.')


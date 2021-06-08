"""
Faça um programa que tenha uma função chamada área() que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""

def área(x, y):
    a = x * y
    print(f'A área de um terreno {x:.2f}m x {y:.2f}m é igual a {a:.2f}m².')


print('-'*28)
print('--- Controle de Terrenos ---')
print('-'*28)

while True:
    try:
        largura = float(input('LARGURA (m): '))
        
    except:
        print('Não entendi... Por favor, tente novamente.')
        continue

    if largura > 0:
        break
    else:
        print('Não entendi... Por favor, tente novamente.')

while True:
    try:
        comprimento = float(input('COMPRIMENTO (m): '))
    except:
        print('Não entendi... Por favor, tente novamente.')
        continue

    if comprimento > 0:
        break
    else:
        print('Não entendi... Por favor, tente novamente.')

área(largura, comprimento)

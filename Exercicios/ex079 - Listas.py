"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

list_n = []

while True:
    try:
        n = int(input("Digite um valor: "))
    
    except:
        print('Não entendi...', end='')
        continue

    if n not in list_n:
        list_n.append(n)
        print(f'O número {n} foi adicionado com sucesso.')
    else:
        print(f'O número {n} já está na lista.')

    while True:
        resp = str(input("Deseja continuar? [S/N] "))
        if resp in 'SsNn':
            break
        print("Não entendi... ", end='')

    if resp in 'Nn':
        break

print('-='*25)
print(f'Você digitou os valores {sorted(list_n)}')

"""
Aprimorar o desafio anterior, mostrando no final: 
1 - A soma de todos os valores pares digitados.
2 - A soma dos valores da terceira coluna.
3 - O maior valor da segunda linha.
"""

matriz = [[],[],[]]
soma_pares = soma_terceira_coluna = maior_valor_segunda_linha = 0

for i in range(0,3):
    for j in range(0,3):
        while True:
            try:
                valor = int(input(f'Digite um valor para [{i}, {j}]: '))
            except:
                print('Não entendi... ', end='')
                continue
            
            if valor % 2 == 0:
                soma_pares += valor

            break
        matriz[i].append(valor)

print('-='*30)
for i in range(0,3):
    for j in range(0,3):
        if j != 2:
            print(f'[ {matriz[i][j]:^6} ]', end='')
        else:
            print(f'[ {matriz[i][j]:^6} ]')

print('-='*30)
print(f'A soma de todos os valores pares digitados é {soma_pares}.')

print(f'A soma dos valores da terceira coluna é ', end='')

for i in range(0,3):
    soma_terceira_coluna += matriz[i][2]

print(f'{soma_terceira_coluna}.')

print(f'O maior valor da segunda linha é ', end='')

for j in range(0,3):
    if matriz[1][j] > maior_valor_segunda_linha:
        maior_valor_segunda_linha = matriz[1][j]

print(f'{maior_valor_segunda_linha}.')

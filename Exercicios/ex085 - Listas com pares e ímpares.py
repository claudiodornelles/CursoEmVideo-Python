"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

valores = [[], []]

for i in range(0,7):
    while True:
        try:
            valor = int(input(f'Digite o {i + 1}º valor: '))
        
        except:
            print('Não entendi... ', end='')
            continue
        
        break
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(valores[0])}')
print(f'Os valores ímpares digitados foram: {sorted(valores[1])}')
print()

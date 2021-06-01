"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

1 - Quatas vezes apareceu o valor 9.
2 - Em que posição foi digitado o primeiro valor 3.
3 - Quais foram os números pares.

"""

pares = []
tupla = (int(input("Informe o primeiro valor: ")),int(input("Informe o segundo valor: ")),int(input("Informe o terceiro valor: ")), int(input("Informe o quarto valor: ")))

print(f'Você digitou os valores {tupla}')
if tupla.count(9) != 1:
    print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
else:
    print(f'O valor 9 apareceu {tupla.count(9)} vez.')

if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição.')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')

print(f'Os valores pares digitados foram ', end = '')

for elemento in tupla:
    if elemento % 2 == 0:
        print(f'{elemento}, ', end = '')

print('\b\b.')



"""
Crie um programa que leia um número Real qualquer pelo teclado
e mostre na tela a sua porção Inteira.

Ex:
Digite um número: 6.127
O número 6.127 tem a parte Inteira 6.
"""

import math

numero = float(input('Digite um número: '))
parte_inteira = math.floor(numero)
print(f'O número {numero} tem a parte Inteira {parte_inteira}')

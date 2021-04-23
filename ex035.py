"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
ou não formar um triângulo.
"""

r1 = float(input('Informe o comprimento da reta 1: '))
r2 = float(input('Informe o comprimento da reta 2: '))
r3 = float(input('Informe o comprimento da reta 3: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
	print(f'Parabéns, é possível sim formar um triângulo com três retas de comprimento {r1}, {r2} e {r3}!')
else:
	print(f'Não é possível formar um triângulo com três retas de comprimento {r1}, {r2} e {r3}.')

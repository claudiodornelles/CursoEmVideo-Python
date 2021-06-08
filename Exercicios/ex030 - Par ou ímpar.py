"""
Crie um programa que leia um número inteiro e mostre na tela se ele é
PAR ou ÍMPAR.
"""

n = int(input('Digite um número inteiro: '))

if n == 0:
	print(f'O número {n} não possui paridade.')
else:
	if n % 2 == 0:  # % significa o resto da divisão de n por 2
		print(f'O número {n} é par!')
	else:
		print(f'O número {n} é ímpar!')

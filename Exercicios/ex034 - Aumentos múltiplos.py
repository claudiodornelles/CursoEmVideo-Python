"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para salários inferiores ou iguais, o aumento será de 15%.
"""

sal = float(input('Informe o seu salário: '))

if sal > 1250:
	aumento = sal * 0.10
else:
	aumento = sal * 0.15
print(f'O seu aumento será de R${aumento}0.')

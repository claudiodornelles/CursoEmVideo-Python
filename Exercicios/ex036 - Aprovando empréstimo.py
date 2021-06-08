"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcular o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo
será negado.
"""

salario = float(input('Qual é o seu salário?'))
divida = float(input('Qual o valor que você quer financiar?'))
prazo = int(input('Em quantos meses você gostaria de pagar?'))
prestacao = divida / prazo

if prestacao > (salario * 0.30):
	print('Infelizmente a sua renda não é suficiente para liberarmos este financiamento.')
else:
	print('Parabéns, o seu limite de crédito foi liberado!')
	print(f'O seu financiamento de R${divida:.2f} será efetuado em {prazo} parcelas de R${prestacao:.2f}.')

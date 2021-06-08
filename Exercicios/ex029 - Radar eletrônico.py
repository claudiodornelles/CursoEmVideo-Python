"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima da velocidade.
"""

v = float(input('Qual é a velocidade do carro (km/h)? '))

if v > 80000:
	multa = (v - 80) * 7
	print('Você ultrapassou o limite de velocidade de 80km/h.')
	print('Você foi multado em R${:.2f}.'.format(multa))
else:
	print('Muito bem! {:.1f}km/h está dentro do limite de velocidade. Siga com segurança!'.format(v))

"""
Desenvolva um programa que pergunte a distância de uma viagem em quilômetros.
Calcule o preço da passagem cobrando R$0,50 por km para viagens até 200km e R$0,45 para viagens mais longas.
"""
#  Recebendo dados do usuário
dist = float(input('Informe a distância da sua viagem em quilômetros (informe apenas números): '))
#  Processamento de dados
if dist > 200:
    preco = dist * 0.45
    print(f'O preço da passagem será R${preco:.2f}')
else:
    preco = dist * 0.50
    print(f'O preço da passagem será R${preco:.2f}')

"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import date

cadastro = dict()

cadastro['Nome'] = str(input('Nome: ')).strip().title()
cadastro['Idade'] = date.today().year - int(input('Ano de Nascimento: '))
cadastro['CTPS'] = int(input('Nº da Carteira de Trabalho (0 caso não possua): '))

if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = float(input('Salário: R$'))
    cadastro['Aposentadoria'] = 35 - (date.today().year - cadastro['Contratação']) + cadastro['Idade']
print('-='*30)

for chave, valor in cadastro.items():
    print(f'{chave} tem o valor {valor}')

print()

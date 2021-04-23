"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não
com o nome "SANTO".
"""

#  Recebendo os dados do usuário
cidade = input('Digite o nome de uma cidade: ').lower()
#  Processamento dos dados]
cidade_lista = cidade.split()
print('santo' in cidade_lista[0])

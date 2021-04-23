"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente. Independentemente do tamanho do nome.
"""
#  Recebendo dados do usuário
nome_completo = input('Digite seu nome completo: ').title().strip()
#  Processamento de dados
nome_lista = nome_completo.split()
i = len(nome_lista) - 1
#  Devolvendo dados ao usuário
print(f'O primeiro nome é {nome_lista[0]} e o último nome é {nome_lista[i]}.')

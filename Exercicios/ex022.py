"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
1 - O nome com todas as letras maiúsculas
2 - O nome com todas as letras minúsculas
3 - Quantas letras ao todo (sem considerar espaços)
4 - Quantas letras tem o primeiro nome
"""
#  Recebendo dados
nome = str(input('Qual é o seu nome completo? '))

#  Processamento
print(f'1 - {nome.upper()}')
print(f'2 - {nome.lower()}')
nome_lista = nome.split()
nome_lista_junta = nome_lista[0] + nome_lista[1] + nome_lista[2] + nome_lista[3]
print(f'3 - O seu nome tem {len(nome_lista_junta)} letras, sem considerar os espaços.')
print(f'4 - O seu primeiro nome tem {len(nome_lista[0])} letras.')

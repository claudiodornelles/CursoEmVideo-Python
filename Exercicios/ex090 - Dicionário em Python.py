"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""

aluno = {}

aluno['nome'] = str(input('Nome: ')).title().strip()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

print(f'Nome é igual a {aluno["nome"]}.')
print(f'Média é igual a {aluno["media"]:.1f}.')
print('Situação é igual a ', end='')

if aluno['media'] >= 7:
    print('Aprovado.')
else:
    print('Reprovado.')

print()
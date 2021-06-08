"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""

aluno = {}

aluno['Nome'] = str(input('Nome: ')).title().strip()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Média'] < 5:
    aluno['Situação'] = 'REPROVADO'
elif aluno['Média'] < 7:
    aluno['Situação'] = 'EM RECUPERAÇÃO'
else:
    aluno['Situação'] = 'APROVADO'
print('-='*30)
for k, v in aluno.items():
    print(f'   - {k} é igual a {v}.')
print()
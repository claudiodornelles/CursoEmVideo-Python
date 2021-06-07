"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
1 - Quantas pessoas foram cadastradas.
2 - A média de idade do grupo.
3 - Uma lista com todas as mulheres.
4 - Uma lista com todas as pessoas com idade acima da média.
"""

temp = {}
pessoas = []
mulheres = []
soma_idades = media = 0

while True:
    temp['nome'] = str(input('Nome: ')).strip().title()
    temp['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
    temp['idade'] = int(input('Idade: '))
    pessoas.append(temp.copy())
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-='*30)
print(f'- O grupo tem {len(pessoas)} pessoas.')

for pessoa in pessoas:
    soma_idades += pessoa['idade']

media = soma_idades / len(pessoas)

print(f'- A média de idade é de {media:.0f} anos.')

print(f'- As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        mulheres.append(p['nome'])
        mulheres.sort()
for m in range(0, len(mulheres)):
    if m < len(mulheres) - 1:
        print(f'{mulheres[m]}, ', end='')
    else:
        print(f'\b\b e {mulheres[m]}.')

print('- Lista das pessoas com idade acima da média:')
print()
for pessoa in pessoas:
    if pessoa['idade'] > media:
        print(f'--> Nome = {pessoa["nome"]}; Sexo = {pessoa["sexo"]}; Idade = {pessoa["idade"]}.')
print('\n<< ENCERRADO >>\n')

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
    while True:
        temp['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if temp['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    temp['idade'] = int(input('Idade: '))
    pessoas.append(temp.copy())
    temp.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro! Por favor, digite apenas S ou N.')
    if resp in 'N':
        break

print('-='*30)
print(f'- O grupo tem {len(pessoas)} pessoas.')

for pessoa in pessoas:
    soma_idades += pessoa['idade']

media = soma_idades / len(pessoas)

print(f'- A média de idade é de {media:.0f} anos.')

for p in pessoas:
    if p['sexo'] == 'F':
        mulheres.append(p['nome'])
        mulheres.sort()
if len(mulheres) > 0:
    print(f'- As mulheres cadastradas foram: ', end='')
    for m in range(0, len(mulheres)):
        if m < len(mulheres) - 1:
            print(f'{mulheres[m]}, ', end='')
        else:
            print(f'\b\b e {mulheres[m]}.')
else:
    print('- Não foram cadastradas mulheres na lista.')

print('- Lista das pessoas com idade acima da média:')
for pessoa in pessoas:
    if pessoa['idade'] > media:
        print(f'  --> Nome = {pessoa["nome"]}; Sexo = {pessoa["sexo"]}; Idade = {pessoa["idade"]}.')
print('\n<< ENCERRADO >>\n')

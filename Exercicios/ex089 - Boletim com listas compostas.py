"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada aluno e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
notas = []
aluno = []
alunos = []
soma = n_notas = 0

while True:
    nome = str(input('Nome: '))
    aluno.append(nome)

    n1 = float(input('Nota 1: '))
    notas.append(n1)

    n2 = float(input('Nota 2: '))
    notas.append(n2)

    aluno.append(notas[:])
    alunos.append(aluno[:])
    notas.clear()
    aluno.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] '))
        if resp in 'SsNn':
            break
        print('Não entendi... ', end='')
    if resp in 'Nn':
        break

print('\n-'*30)
print(f'Nº\tNome\t\tMédia')
print('-'*30)

for n, aluno in enumerate(alunos):
    for nota in aluno[1]:
        soma += nota
        n_notas += 1
    media = soma / n_notas
    print(f'{n}\t{aluno[0]}\t\t{media:.1f}')
    soma = 0
    n_notas = 0
print('-'*30)

while True:
    try:
        resp = int(input('\nDeseja mostrar a nota de qual aluno? (999 interrompe) '))
    
    except:
        print('Não entendi... ', end='')
        continue

    if resp == 999:
        print('Finalizando...\n<<< VOLTE SEMPRE >>>\n')
        break
    elif resp in range(0,len(alunos)):
            print(f'As notas de {alunos[resp][0]} foram {alunos[resp][1]}')
            print('-'*30)
    else:
        print('Aluno não cadastrado... ', end='')
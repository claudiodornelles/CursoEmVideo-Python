"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido.
"""
#  Importando bibliotecas necessárias
from random import choice
#  Recebendo dados do usuário
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
#  Processamento
alunos = [n1, n2, n3, n4]
escolhido = choice(alunos)
#  Devolvendo resultado
print(f'O aluno sorteado para apagar o quadro foi -> {escolhido}')

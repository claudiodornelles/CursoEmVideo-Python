"""
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
#  Importando bibliotecas necessárias
from random import shuffle
#  Recebendo dados do usuário
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
#  Processamento
alunos = [n1, n2, n3, n4]
shuffle(alunos)
#  Devolvendo resultado
print(f'A ordem de apresentação dos trabalhos será: {alunos}')
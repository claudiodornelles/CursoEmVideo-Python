"""
Faça um programa que leia uma frase pelo teclado e apresente:
-> Quantas vezes aparece a letra "A";
-> Em que posição ela aparece a primeira vez;
-> Em que posição ela aparece a última vez.
"""

#  Recebendo dados do usuário
frase = input('Digite uma frase qualquer: ').lower().strip()

#  Processamento dos dados
n_vezes = frase.count('a')
pos_ini = frase.find('a')
pos_fin = frase.rfind('a')
print(f'Na frase apresentada, a letra A aparece {n_vezes} vezes.')
print(f'Na frase apresentada, a letra A aparece pela primeira vez na posição {pos_ini}.')
print(f'Na frase apresentada, a letra A aparece pela última vez na posição {pos_fin}.')

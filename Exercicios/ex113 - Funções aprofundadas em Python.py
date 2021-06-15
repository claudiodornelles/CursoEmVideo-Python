"""
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
from ex113_files import leia

i = leia.leiaInt('Digite um número Inteiro: ')
f = leia.leiaFloat('Digite um número Real: ')

if type(i) == type(f) == bool:
    print('\033[31mO usuário não informou nenhum número.\033[m')
elif type(i) == bool:
    print(f'O valor Inteiro não foi informado e o valor Real digitado foi {f}')
elif type(f) == bool:
    print(f'O valor Inteiro digitado foi {i} e o valor Real não foi informado.')
else:
    print(f'O valor Inteiro digitado foi {i} e o valor Real foi {f}')
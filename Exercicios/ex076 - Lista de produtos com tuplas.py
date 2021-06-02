"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.

No final mostre uma listagem de preços organizando os dados em forma tabular.
"""

produtos = ('Lápis', 1.75,
             'Borracha', 2,
             'Caderno', 15.90,
             'Estojo', 25,
             'Transferidor', 4.20,
             'Compasso', 9.99,
             'Mochila', 120.32,
             'Canetas', 22.30,
             'Livro', 34.90)

print('')
print('-'*40)
# print('LISTAGEM DE PREÇOS'.center(40, ' '))
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
i = 1
while i <= (produtos.__len__()):
    
    # print(f'{produtos[i - 1]}'.ljust(30, '.'), end='')
    print(f'{produtos[i - 1]:.<30}R$', end='')
    # print(f'{produtos[i]:.2f}'.rjust(8, " "))
    print(f'{produtos[i]:>8.2f}')
    i += 2
print('-'*40)
print('')

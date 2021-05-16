"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""

n = int(input("Digite um número inteiro: "))

print('''Escolha uma das bases para conversão:
[ 1 ] - Converter para Binário
[ 2 ] - Converter para Octal
[ 3 ] - Converter para Hexadecimal''')

opcao = int(input("Informe sua opção: "))

if opcao == 1:
    print(f'{n} convertido para Binário é igual a {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} convertido para Octal é igual a {oct(n)[2:]}')
elif opcao	== 3:
    print(f'{n} convertido para Hexadecimal é igual a {hex(n)[2:]}')
else:
    print('Opção inválida. Tente novamente.')
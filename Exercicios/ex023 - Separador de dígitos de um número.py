"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
dígitos separados.

Ex:
Digite um número: 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1
"""

#  Recebendo os dados do usuário
num = str(input('Digite um número entre 0 e 9999: '))
#  Processando o dado
unidade = num[3]
dezena = num[2]
centena = num[1]
milhar = num[0]
#  Devolvendo os dados ao usuário
print(f"""Unidade: {unidade}
Dezena: {dezena}
Centena: {centena}
Milhar: {milhar}
""")
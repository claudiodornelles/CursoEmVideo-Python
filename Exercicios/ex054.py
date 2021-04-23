"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date

n = 7  # Número de dados para informar
maior = 0
menor = 0

for i in range(1,n + 1):
    ano_informado = int(input(f"Em que ano a {i}ª pessoa nasceu? "))
    idade = date.today().year - ano_informado
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print(f"Ao todo tivemos {maior} pessoas maiores de idade e {menor} pessoas menores de idade.")

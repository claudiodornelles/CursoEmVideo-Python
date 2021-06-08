"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando
os espaços.
"""

frase = str(input("Digite a frase que você quer saber se é um palíndromo: ")).strip().upper()
frase_lista = frase.split()
"""
frase_mod = ""
for i in range(0, len(frase_lista)):
    frase_mod += frase_lista[i]
"""
frase_mod = ''.join(frase_lista)

if frase_mod == frase_mod[::-1]:
    print(f"A frase que você digitou é um palíndromo!")
    print(f"A mesma frase lida de tras pra frente possui o mesmo sentido.")
    print(f"{frase} = {frase}")
else:
    print(f"A frase que você digitou não é um palíndromo!")

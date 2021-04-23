"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progessão.
"""

a1 = int(input("Informe o primeiro termo da PA: "))
r = int(input("Informe a razão da PA: "))
termos = int(input("Informe o número de termos da PA: "))
pa = []

for i in range(1, termos + 1):
    an = a1 + (i - 1) * r
    pa.append(an)
print(f"A PA informada é: {pa}")

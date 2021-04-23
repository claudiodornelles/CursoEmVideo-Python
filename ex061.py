"""
Refaça o DESAFIO 051 lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

a1 = int(input("Informe o primeiro termo da PA: "))
pa = [a1]
r = int(input("Informe a razão da PA: "))
termos = int(input("Informe o número de termos da PA: "))
c = 1
print(f"A progressão aritimétcia informada foi: ", end = "")

while c <= termos:
    a1 += r
    pa.append(a1)
    c += 1
print(pa)

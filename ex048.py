"""
Faça um programa que calcule a soma entre todos os números
ímpares que são múltiplos de três e que se encontram no intervalo
de 1 até 500.
"""
i = 1
j = 500
a = 3
soma = 0
cont = 0
for c in range(i, (j + 1)):
    if c % 2 != 0 and c % a == 0:
        soma += c
        cont += 1
print(f"Entre {i} e {j} existem {cont} números ímpares que são múltiplos de {a} e a soma deles é {soma}")

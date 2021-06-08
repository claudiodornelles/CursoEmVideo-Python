"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

while True:
    n = input("Informe um número para saber se ele é primo, ou digite [0] para sair: ")
    try:
        n = int(n)
    except:
        print("Número inválido, por favor digite um número inteiro para saber se ele é primo.")
        continue

    divisores = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisores.append(i)
        if len(divisores) > 2:
            print(f"O número {n} não é um número primo.")
            break
        elif i == n and len(divisores) == 2:
            print(f"O número {n} é um número primo.")
            print(divisores)
            break
        else:
            print(f"O número {n} não é um número primo.")
            break
    if n == 0:
        print("Você optou por sair do programa.")
        exit()

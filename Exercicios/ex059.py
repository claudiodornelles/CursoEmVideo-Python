"""
Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

op = 0
while op != 5:
    if op != 4:
        n1 = float(input("Digite um primeiro número: "))
        n2 = float(input("Digite um segundo número: "))
    else:
        n1 = float(input("Digite novamente um primeiro número: "))
        n2 = float(input("Digite novamente um segundo número: "))
    maior = n1

    if n2 > n1:
        maior = n2

    print("""OPERAÇÕES DISPONÍVEIS:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa""") 

    op_valid = False

    while not op_valid:
        op = int(input("Por favor, informe a operação desejada: "))
        if op in range(1,6):
            op_valid = True
    if op == 1:
        print(f"{n1} + {n2} = {n1 + n2}")
    elif op == 2:
        print(f"{n1} * {n2} = {n1 * n2}")
    elif op == 3:
        print(f"O maior número entre {n1} e {n2} é {maior}.")

print("Até breve.")

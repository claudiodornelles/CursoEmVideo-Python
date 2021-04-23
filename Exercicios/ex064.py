"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final mostre quantos números foram digitados e qual foi a soma entre eles.
"""

soma = num = 0
c = 1

while True:
    num = input(f"Digite o {c}º número inteiro: ")
    try:
        num = int(num)
    except:
        print("Não entendi, repita por favor.")
        continue
    if num != 999:
        soma += num
        c += 1
    else:
        c -= 1
        break
print(f"Você digitou {c} números e a soma deles foi {soma}.")

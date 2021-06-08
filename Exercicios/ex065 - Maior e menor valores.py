"""
Crie um programa que leia vários números inteiros.
No final da execução, mostre a média entre todos os números e quais foram o maior e o menor valor informado.
O programa deve perguntar ao usuário se ele quer continuar a digitar valores.
"""

soma = num = maior = menor = 0
c = 1

while True:
    num = input(f"Digite o {c}º número inteiro: ")
    try:
        num = int(num)
    except:
        print("Não entendi, vamos tentar novamente.")
        continue
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    soma += num
    while True:
        cont = input("Deseja continuar? [S/N]")
        try:
            cont = str(cont)
        except:
            print("Não entendi, vamos tentar novamente.")
            continue
        if cont in 'Ss':
            continuar = True
            break
        elif cont in 'Nn':
            continuar = False
            break
        else:
            print("Não entendi, vamos tentar novamente.")
            continue
    if continuar:
        c += 1
    else:
        break

media = soma/c

print(f"A média entre os {c} números digitados foi {media}.")
print(f"O menor valor informado foi {menor} e o maior {maior}.")
    
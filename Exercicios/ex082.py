"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""

numeros = []

while True:
    try:
        numero = int(input('Digite um valor: '))

    except:
        continue
    
    numeros.append(numero)

    while True:
        resp = str(input('Deseja continuar? '))
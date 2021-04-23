"""
Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex:
5! = 5x4x3x2x1 = 120
"""

num = int(input("Digite um número para saber o seu fatorial: "))
contador = num
num_fat = num
print(f"{num}! = ", end = '')
while contador > 1:
    num_fat *= (contador - 1)
    print(f"{contador} x ", end = '')
    contador -= 1
print(f"1 = {num_fat}")

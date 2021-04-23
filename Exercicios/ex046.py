"""
Faça um programa que mostre na tela um contagem regressiva para o
estouro de fogos de artifício, indo de 10 até 0, com pausa de 1 segundo
entre eles.
"""

from time import sleep

for i in range(10, 0, -1):
    print(f"{i}")
    sleep(1)

"""
Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo, calcule e mostre o
comprimento da hipotenusa.

"""

import math

ca = float(input('Qual é o comprimento do cateto adjacente? '))
co = float(input('Qual é o comprimento do cateto oposto? '))
h = math.hypot(ca, co)
print(f'O comprimento da hipotenusa do triângulo de lados {ca} e {co} é igual a {h}.')

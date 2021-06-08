"""
Faça um programa que leia um ângulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse ângulo.

"""
#  Importando bibliotecas necessárias
import math
#  Recebendo dados
angulo = float(input('Digite o valor do ângulo: '))
#  Processando
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
#  Devolvendo resultado
print(f'O ângulo {angulo} tem Seno igual a {seno}, Cosseno igual a {cosseno} e Tangente igual a {tangente}.')

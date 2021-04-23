"""
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""

rep = 5
peso = []
for i in range(1, rep + 1):
    peso_info = float(input(f"Qual é o peso da {i}ª pessoa? "))
    peso.append(peso_info)
peso.sort()
maior = peso[len(peso) - 1]
menor = peso[0]
print(f"O maior peso lido foi {maior:.2f} kg e o menor foi {menor:.2f} kg.")

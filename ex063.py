"""
Escreva um programa que leia um número n inteiro qualquer e
mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
"""

i = 0
j = 1
an = 0
seq = [1]
print("Vou lhe mostrar uma sequência de Fibonacci!")
termos = int(input("Quantos termos você gostaria de ver? "))
if termos != 1:
    seq.append(1)
    while i <= (termos - 3):
        an = seq[i] + seq[j]
        seq.append(an)
        i += 1
        j = i + 1
    print(f"Os {termos} primeiros termos da sequência de Fibonacci são: {seq}")
else:
    print(f"O primeiro termo da sequência de Fibonacci é {seq}")

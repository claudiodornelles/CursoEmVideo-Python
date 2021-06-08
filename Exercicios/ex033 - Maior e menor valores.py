"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
#  Recebendo dados do usuário
n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
n3 = float(input('Informe o terceiro número: '))

#  Processamento de dados
#  Verificando se é Float ou Integer
if n1 == int(n1):
	n1 = int(n1)
if n2 == int(n2):
	n2 = int(n2)
if n3 == int(n3):
	n3 = int(n3)
#  Guardando número em lista e ordenando
lista = [n1, n2, n3]
lista.sort()
last = int(len(lista)) - 1
menor = lista[0]
maior = lista[last]

#  Devolvendo dados ao usuário
print(f'O maior número é o {maior} e o menor é o {menor}.')

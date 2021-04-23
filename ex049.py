"""
Refaça o DESAFIO 009 mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço FOR.
"""

n = int(input("Digite um número inteiro para ver a sua tabuada: "))
for i in range(1, 11):
    print(f"{n} x {i:2} = {n * i:2}")

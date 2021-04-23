"""
Refaça o desafio 035 dos triângulos e acrescente o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: Todos os lados iguais.
- Isósceles: Dois lados iguais.
- Escaleno: Todos os lados diferentes.
"""

r1 = float(input("Informe o comprimento da reta 1: "))
r2 = float(input("Informe o comprimento da reta 2: "))
r3 = float(input("Informe o comprimento da reta 3: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f"Parabéns, com três retas de comprimento {r1}, {r2} e {r3} é possível formar um triângulo ", end='')
    if r1 == r2 == r3:
        print("Equilátero, pois possui os três lados iguais.")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Isóceles, pois possui dois lado iguais.")
    else:
        print("Escaleno, pois todos os lados são diferentes entre si.")
else:
    print(f'Não é possível formar um triângulo com três retas de comprimento {r1}, {r2} e {r3}.')

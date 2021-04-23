"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acorod com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""

alt = float(input("Informe a sua altura em centímetros: "))/100
pes = float(input("Informe o seu peso em quilogramas: "))
IMC = pes / (alt * alt)

print(f"O seu IMC é igual à {IMC:.2f}.")
if IMC > 40:
    print("Você está com obesidade mórbida.")
elif IMC >= 30:
    print("Você está com obesidade.")
elif IMC >= 25:
    print("Você está com sobrepeso.")
elif IMC >= 18.5:
    print("Você está com o seu peso ideal.")
else:
    print("Você está abaixo do seu peso.")

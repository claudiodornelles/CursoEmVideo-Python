"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
'M' ou 'F'. Caso esteja errado peça a digitação novamente até ter um valor correto.
"""
sexo = 'n'

while sexo not in 'MmFf':
    sexo = str(input("Informe o sexo da pessoa [M ou F]: "))
print(f"O sexo informado foi '{sexo}'")

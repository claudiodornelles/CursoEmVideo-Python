"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

color = {'null': '\033[m',
         'txt_red': '\033[31m',
         'txt_blue': '\033[34m'}

n1 = int(input(f"Digite o {color['txt_blue']}primeiro{color['null']} número:"))
n2 = int(input(f"Digite o {color['txt_blue']}segundo{color['null']} número: "))

if n1 == n2:
    print(f"{color['txt_red']}Não existe{color['null']} valor maior, os dois são {color['txt_blue']}iguais{color['null']}.")
elif n1 > n2:
    print(f"O {color['txt_red']}primeiro{color['null']} valor é {color['txt_blue']}maior{color['null']}.")
else:
    print(f"O {color['txt_red']}segundo{color['null']} valor é {color['txt_blue']}maior{color['null']}.")

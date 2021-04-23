"""
Crie um programa que leia duas notas de um aluno e calcule sua média
mostrando uma mensagem no final de acordo com a média atingida.

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou supeior: APROVADO
"""
color = {'null': '\033[m',
         'txt_red': '\033[31m',
         'txt_green': '\033[32m',
         'txt_yellow': '\033[33m',
         'txt_blue': '\033[34m'}

n1 = float(input(f"Informe a {color['txt_blue']}primeira{color['null']} nota do aluno: "))
n2 = float(input(f"Informe a {color['txt_blue']}segunda{color['null']} nota do aluno: "))
m = (n1 + n2) / 2
if m < 5:
    print(f"{color['txt_red']}REPROVADO!{color['null']} A média do aluno foi {color['txt_red']}menor do que 5{color['null']}.")
elif m < 7:
    print(f"{color['txt_yellow']}RECUPERAÇÃO!{color['null']} A média do aluno foi {color['txt_yellow']}menor do que 7{color['null']}.")
else:
    print(f"{color['txt_green']}APROVADO!{color['null']} A média do aluno foi {color['txt_green']}maior do que 7{color['null']}.")

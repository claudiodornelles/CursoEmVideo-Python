"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
"""
from datetime import date

color = {'null': '\033[m',
         'txt_red': '\033[31m',
         'txt_green': '\033[32m',
         'txt_yellow': '\033[33m',
         'txt_blue': '\033[34m'}

yb = int(input(f"Qual é o {color['txt_blue']}ano{color['null']} de nascimento do atleta? "))
idade = date.today().year - yb
if idade <= 9:
    print(f"O atleta {color['txt_green']}pode competir{color['null']} na categoria: {color['txt_blue']}MIRIM{color['null']}")
elif idade <= 14:
    print(f"O atleta {color['txt_green']}pode competir{color['null']} na categoria: {color['txt_blue']}INFANTIL{color['null']}")
elif idade <= 19:
    print(f"O atleta {color['txt_green']}pode competir{color['null']} na categoria: {color['txt_blue']}JUNIOR{color['null']}")
elif idade <= 20:
    print(f"O atleta {color['txt_green']}pode competir{color['null']} na categoria: {color['txt_blue']}SÊNIOR{color['null']}")
else:
    print(f"O atleta {color['txt_green']}pode competir{color['null']} na categoria: {color['txt_blue']}MASTER{color['null']}")

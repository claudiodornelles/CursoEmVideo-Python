"""
Faça um programa que leia a idade de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda deve se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

"""
from datetime import date

color = {'null': '\033[m',
         'txt_blue': '\033[34m',
         'txt_red': '\033[31m'}

yb = int(input("Qual o seu ano de nascimento? "))

idade = date.today().year - yb

if idade == 18:
    print(f"{color['txt_blue']}Está na hora{color['null']} de você se alistar ao serviço militar!")
    print("O alistamento deve ocorrer no ano em que você completa 18 anos de idade.")
elif idade < 18:
    tempo = 18 - idade
    print(f"{color['txt_red']}Você ainda não tem{color['null']} idade para se alistar ao serviço militar.")
    print("O alistamento deve ocorrer no ano em que você completa 18 anos de idade.")
    print(f"Você poderá se alistar em {color['txt_blue']}{tempo} ano(s){color['null']}.")
else:
    tempo = idade - 18
    print(f"{color['txt_red']}Já passou o momento do seu alistamento.{color['null']}")
    print("O alistamento deve ocorrer no ano em que você completa 18 anos de idade.")
    print(f"Caso você não tenha se alistado, {color['txt_red']}você deveria ter o feito {tempo} ano(s) atrás{color['null']}.")

"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se a pessoa tem voto NEGADO, OPCIONAL, ou OBRIGATÓRIO nas eleições.
"""

from datetime import date

ano_atual = date.today().year

def voto(ano_nascimento: int):
    """
    voto(ano_nascimento)

    Calcula a idade do indivíduo e retorna se é possível realizar o voto na próxima eleição.
    """
    idade = ano_atual - ano_nascimento

    if idade < 16:
        return f'Com {idade} anos não é possível votar.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos o voto é opcional.'
    else:
        return f'Com {idade} anos o voto é obrigatório.'


print('-='*30)
while True:
    try:
        ano = int(input('Em que ano você nasceu? '))
    
    except:
        print('Ano de nascimento inválido. Tente novamente.')
        continue

    if ano > 0 and ano <= ano_atual:
        break
    else:
        print('Ano de nascimento inválido. Tente novamente')

print(voto(ano))

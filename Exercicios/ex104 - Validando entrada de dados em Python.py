"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
"""

cor = {'none': '\033[m',
       'vermelho': '\033[31m'}

def leiaInt(prompt=None):
    """
    Lê um número inteiro digitado pelo usuário.\n
    Retorna o número digitado.
    """

    while True:
        try:
            n = int(input(prompt))
        
        except:
            print(f'{cor["vermelho"]}Erro! Digite um número inteiro válido.{cor["none"]}')
            continue

        break
    return n


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')

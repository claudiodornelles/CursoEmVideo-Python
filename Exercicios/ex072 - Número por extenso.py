"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

numero = 21

while True:

    while True:
        numero = str(input("Digite um número entre 0 e 20: "))
        if numero in '01234567891011121314151617181920':
            break
        print(f'Não entendi. ', end='')

    print(f'Você digitou o número {numeros[int(numero)]}.')

    while True:
        resposta = str(input('Deseja continuar [S/N]? '))
        if resposta in 'SsNn':
            break
        print('Não entendi. ', end='')

    if resposta in 'Nn':
        break
print('\nPrograma encerrado.\n')
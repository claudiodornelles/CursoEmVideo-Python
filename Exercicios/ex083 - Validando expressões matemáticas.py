"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

expressao = str(input('Digite uma expressão: '))
teste = []

for letra in expressao:
    if letra == '(':
        teste.append(letra)
    elif letra == ')':
        if '(' in teste:
            teste.remove('(')
        else:
            teste.append('(')

if len(teste) > 0:
    print(f'A expressão "{expressao}" contém erro na abertura e fechamento de parênteses.')
else:
    print(f'A expressão "{expressao}" foi digitada corretamente!')

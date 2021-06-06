"""
Crie um programa que tenha uma tupla com várias palavras.
O programa deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')

for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra in 'AaEeIiOoUu':
            print(f'{letra.lower()}, ', end='')
    print('\b\b.')

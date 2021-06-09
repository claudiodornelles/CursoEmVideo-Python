"""
Faça um programa que tenha a função chamada escreva() que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~
"""

def escreva(txt: str):
    """
    -> Mostra na tela uma mensagem formatada como abaixo:
    \~~~~~~~~~~~~~
      Olá, Mundo! 
    \~~~~~~~~~~~~~
    
    :param txt: Mensagem
    :return: Sem retorno.
    """


    tam = len(txt) + 4
    print('~'*tam)
    print(f'  {txt}  ')
    print('~'*tam)


escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')

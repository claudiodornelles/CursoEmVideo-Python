"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só  que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint

inicio = 0
fim = 10
escolha = randint(inicio, fim)
tentativa = escolha + 1
rep = 0

print(f"Vou pensar em um número entre {inicio} e {fim}.\nVocê consegue adivinhar esse número?!")

while tentativa != escolha:
    tentativa = int(input("Em qual número eu pensei? "))
    rep += 1
    print(f"Você errou! Tente novamente!")
if rep > 1:
    print(f"Parabéns, você acertou o número que pensei em {rep} tentativas.")
else:
    print(f"Parabéns, você acertou de primeira!!!")

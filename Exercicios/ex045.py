"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
from random import randint
from time import sleep

i = 0
opcoes = ["PEDRA", "PAPEL", "TESOURA"]
print(f"{' Vamos jogar? ':=^40}")

while True:
    print("Escolha uma opção:\n"
    "[ 0 ] - PEDRA\n"
    "[ 1 ] - PAPEL\n"
    "[ 2 ] - TESOURA")
    i = input("Qual é a sua jogada? ")
    try:
        i = int(i)
    except:
        print("Não entendi a sua jogada, vamos tentar novamente?")
        continue
    if 0 <= i <= 2:
        escolha_jogador = opcoes[i]
        escolha_pc = opcoes[randint(0, 2)]
        print("JO")
        sleep(0.5)
        print("KEN")
        sleep(0.5)
        print("PO!")
        jogador = False
        if escolha_jogador == "PEDRA" and escolha_pc == "TESOURA":
            jogador = True
        elif escolha_jogador == "PAPEL" and escolha_pc == "PEDRA":
            jogador = True
        elif escolha_jogador == "TESOURA" and escolha_pc == "PAPEL":
            jogador = True
        else:
            jogador = False
        if jogador:
            print("Parabéns! Você venceu!")
        elif escolha_jogador == escolha_pc:
            print(f"Deu empate!")
        else:
            print("Infelizmente você perdeu... :(")
        print(f"Você jogou {escolha_jogador} e o computador jogou {escolha_pc}.")
    else:
        print("Não entendi a sua jogada...")
    escolha = input("Deseja tentar novamente [S/N] ? ")
    if escolha in 'Nn':
        print("Você optou por sair.")
        break

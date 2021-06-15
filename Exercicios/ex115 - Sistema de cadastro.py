"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""
from time import sleep
from ex115_files import interface


opcoes = ['Ver pessoas cadastradas',  # interface.exibirDados()
          'Cadastrar nova pessoa',  # interface.novoCadastro()
          'Sair do sistema']


while True:
    interface.menu(opcoes)
    op = interface.escolha(opcoes)
    sleep(0.35)

    if op == 0:
        interface.exibirDados('cadastro.txt')
    elif op == 1:
        interface.novoCadastro('cadastro.txt')
    elif op == 2:
        sleep(1)
        interface.titulo('Saindo do sistema... Até logo!', 'vermelho')
        sleep(0.5)
        break


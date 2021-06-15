from ex115_files import cores


def idade(prompt='Idade: '):
    while True:
        try:
            idade = int(input(prompt))
        except:
            print(f'{cores.texto["vermelho"]}ERRO! Digite uma idade válida.{cores.texto["null"]}')
        else:
            if idade > 0:
                break
            else:
                print(f'{cores.texto["vermelho"]}ERRO! Digite uma idade válida.{cores.texto["null"]}')
    return idade

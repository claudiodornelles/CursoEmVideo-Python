"""
Aprimore o EX093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
""" 

jogadores = []
jogador = {}
partidas = []
gols = total_gols = 0

while True:
    print('-'*30)
    jogador['Nome'] = str(input('Nome do Jogador: ')).strip().title()
    tot_partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

    for p in range(0, tot_partidas):
        gols = int(input(f'Quantos gols {jogador["Nome"]} fez na partida {p + 1}? '))
        partidas.append(gols)
        total_gols += gols

    jogador['Gols'] = partidas[:]
    jogador['Total'] = total_gols
    jogador['Partidas'] = tot_partidas
    jogadores.append(jogador.copy())
    jogador.clear()
    partidas.clear()
    total_gols = 0
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-='*30)
print(f'{"Cód.":^5}{"Nome":<15}{"Gols":<25}{"Total":^5}')
for i, j in enumerate(jogadores):
    print(f'{str(i):^5}{str(jogadores[i]["Nome"]):<15}{str(jogadores[i]["Gols"]):<25}{str(jogadores[i]["Total"]):^5}')
print('-='*30)

while True:
    resp = int(input('Deseja mostrar os dados de qual jogador? (Digite 999 para sair) '))

    if resp in range(0, len(jogadores)):
        print(f'\n--- Levantamento do Jogador "{jogadores[resp]["Nome"]}" ---\n')
        print(f'{jogadores[resp]["Nome"]} jogou {jogadores[resp]["Partidas"]} partidas.')
        for np, ng in enumerate(jogadores[resp]["Gols"]):
            if ng == 0:
                print(f'=> Na partida {np + 1}, {jogadores[resp]["Nome"]} não fez nenhum gol.')
            elif ng == 1:
                print(f'=> Na partida {np + 1}, {jogadores[resp]["Nome"]} fez {ng} gol.')
            else:
                print(f'=> Na partida {np + 1}, {jogadores[resp]["Nome"]} fez {ng} gols.')
        print(f'{jogadores[resp]["Nome"]} fez um total de {jogadores[resp]["Total"]} gols.')
        print()
    elif resp == 999:
        break
    else:
        print(f'Erro! Não existe jogador com o código {resp}! Tente novamente...')
print('\n<< Volte sempre >>\n')

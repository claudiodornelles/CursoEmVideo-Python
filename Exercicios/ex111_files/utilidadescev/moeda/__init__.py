def moeda(valor = 0):
    return (f'R${valor:.2f}')


def aumentar(valor = 0, taxa = 0, formatar = False):
    valor *= 1 + (taxa / 100)
    if formatar:
        return moeda(valor)
    else:
        return valor

def diminuir(valor = 0, taxa = 0, formatar = False):
    valor *= 1 - (taxa / 100)
    if formatar:
        return moeda(valor)
    else:
        return valor


def dobro(valor = 0, formatar = False):
    valor *=2
    if formatar:
        return moeda(valor)
    else:
        return valor 


def metade(valor = 0, formatar = False):
    valor /= 2
    if formatar:
        return moeda(valor)
    else:
        return valor


def resumo(valor = 0, taxa_aumentar = 0, taxa_diminuir = 0, formatar = False):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'   Preço analisado:\t{moeda(valor)}')
    print(f'   Dobro do preço: \t{dobro(valor, formatar)}')
    print(f'   Metade do preço:\t{metade(valor, formatar)}')
    print(f'   {taxa_aumentar}% de aumento: \t{aumentar(valor, taxa_aumentar, formatar)}')
    print(f'   {taxa_diminuir}% de redução: \t{diminuir(valor, taxa_diminuir, formatar)}')
    print('-'*40)

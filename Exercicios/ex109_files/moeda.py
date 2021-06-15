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


def moeda(valor = 0):
    return (f'R${valor:.2f}'.replace('.', ','))


def aumentar(valor = 0, taxa = 0):
    valor *= 1 + (taxa / 100)
    return valor


def diminuir(valor = 0, taxa = 0):
    valor *= 1 - (taxa / 100)
    return valor


def dobro(valor = 0):
    return valor * 2


def metade(valor = 0):
    return valor / 2


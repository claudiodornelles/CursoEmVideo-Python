def aumentar(valor = 0, taxa = 0):
    valor *= 1 + (taxa / 100)
    return valor


def diminuir(valor = 0, taxa = 0):
    valor *= 1 - (taxa / 100)
    return valor


def dobro(valor = 0):
    valor *= 2
    return valor


def metade(valor = 0):
    valor /= 2
    return valor


def aumentar(valor, percentual):
    valor *= 1 + (percentual / 100)
    return valor


def diminuir(valor, percentual):
    valor *= 1 - (percentual / 100)
    return valor


def dobro(valor):
    valor *= 2
    return valor


def metade(valor):
    valor /= 2
    return valor


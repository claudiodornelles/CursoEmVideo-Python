def leiaDinheiro(prompt=None):
    validado = False
    while not validado:
        valor = str(input(prompt)).replace(',', '.').strip()
        if valor.isalpha() or valor == '' or float(valor) < 0:
            print('\033[31mErro! Digite um valor monetário válido!\033[m')
        else:
            validado = True
    return float(valor)
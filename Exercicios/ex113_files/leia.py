def leiaInt(prompt=None):
    while True:
        try:
            n = int(input(prompt))
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return False
        except:
            print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def leiaFloat(prompt=None):
    global leu_float
    while True:
        try:
            n = float(input(prompt).replace(',', '.'))
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return False
        except:
            print('\033[31mERRO: Por favor, digite um número real válido.\033[m')
            continue
        else:
            return n


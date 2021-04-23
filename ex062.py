"""
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""
temos = 1
a1 = int(input("Informe o primeiro termo da PA: "))
pa = [a1]
r = int(input("Informe a razão da PA: "))
termos = int(input("Informe o número de termos que você deseja apresentar: "))
c = 1
print(f"A progressão aritimétcia informada foi: ", end = "")

while c <= termos - 1:
    a1 += r
    pa.append(a1)
    c += 1
c1 = c
print(pa)

while termos != 0:
    termos = int(input("Se deseja mostrar mais termos dessa PA, informe o número de termos adicionais: [0 = sair] "))
    if termos != 0:
        print(f"A progressão aritimétcia informada foi: ", end = "")
        while c <= (c1 + termos - 1):
            a1 += r
            pa.append(a1)
            c += 1
        print(pa)
        c1 = c
print("Programa finalizado.")

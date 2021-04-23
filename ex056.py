"""
Desenvolva um programa que leia o nome, a idade e o sexo de 4 pessoas.
No final do programa mostre:
1 - A média de idade do grupo.
2 - Qual é o nome do homem mais velho
3 - Quantas mulheres têm menos de 20 anos.
"""

n_pessoas = 6
nomes = []
idades = []
sexos = []
soma = 0
h_mais_velho = 0
idade_h_mais_velho = 0
m_mais_velha = 0
idade_m_mais_velha = 0
m_menor_de_vinte = 0

for i in range(0, n_pessoas):
    nome = str(input(f"Qual é o nome da {i + 1}ª pessoa? ")).strip().title()
    idade = int(input(f"{nome} tem quantos anos? "))
    sexo = str(input(f"{nome} é um homem (H) ou uma mulher (M)? ")).strip().upper()
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)
    soma += idade
    if sexos[i] == "H":
        if idades[i] > idade_h_mais_velho:
            idade_h_mais_velho = idades[i]
            h_mais_velho = i
    elif sexos[i] == "M":
        if idades[i] > idade_m_mais_velha:
            idade_m_mais_velha = idades[i]
            m_mais_velha = i
        if idades[i] < 20:
            m_menor_de_vinte += 1

media_idades = int(soma/n_pessoas)

print(f"1 - A média de idade do grupo é de {media_idades} anos.")
print(f"2 - O homem mais velho é o {nomes[h_mais_velho]} e ele tem {idades[h_mais_velho]} anos.")
print(f"2.1 - A mulher mais velha é a {nomes[m_mais_velha]} e ela tem {idades[m_mais_velha]} anos.")
if m_menor_de_vinte == 0:
    print(f"3 - No grupo informado não existem mulheres com idade menor do que 20 anos.")
elif m_menor_de_vinte == 1:
    print(f"3 - No grupo informado existe uma única mulher com idade menor do que 20 anos.")
else:
    print(f"3 - No grupo informado existem {m_menor_de_vinte} mulheres com idade menor do que 20 anos.")

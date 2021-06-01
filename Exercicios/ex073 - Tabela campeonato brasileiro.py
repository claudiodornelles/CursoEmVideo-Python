"""
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
1 - Apenas os 5 primeiros colocados.
2 - Os últimos 4 colocaods da tabela.
3 - Em que posição está o time da Chapecoense.
"""

tabela = ("Bragantino", "Bahia", "Ceará", "Fortaleza", "Athletico-PR", "Flamengo", "Atlético-GO", "Cuiabá", "Sport", "Juventude", "Internacional", "São Paulo", "Fluminense", "Grêmio", "Atlético-MG", "América-MG", "Palmeiras", "Corinthians", "Chapecoense", "Santos")

print('-=*=- '*10)
print(f'Lista de times do Brasileirão: {tabela}')
print('-=*=- '*10)
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print('-=*=- '*10)
print(f'Os 4 últimos colocados são: {tabela[-4:]}')
print('-=*=- '*10)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=*=- '*10)
print(f'O time da Chapecoense está na posição {tabela.index("Chapecoense")+1}')

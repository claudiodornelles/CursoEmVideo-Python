"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
from datetime import date

"""
Regra para ano bissexto:
- São bissextos todos os anos múltiplos de 400, p.ex: 1600, 2000, 2400, 2800...
- São bissextos todos os múltiplos de 4, exceto se for múltiplo de 100 mas não de 400, p.ex: 1996, 2000, 2004, 2008, 2012, 2016, 2020...
- Não são bissextos todos os demais anos.
"""

#  Recebendo dados do usuário
ano = int(input('Digite o ano para ser analisado ou digite 0 para analisar o ano atual: '))
#  Processamento de dados
if ano == 0:
	ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
	print(f'{ano} é um ano bissexto.')
else:
	print(f'{ano} não é um ano bissexto.')

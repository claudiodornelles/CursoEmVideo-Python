"""
Adicione ao módulo moeda.py criado nos exercícios anteriores, uma função chamada resumo() que mostre na tela informações geradas pelas funções que já temos no módulo criado até aqui.
"""

from ex110_files import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 50, 35, True)

"""
Crie um pacote chamado utilizadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos EX107, EX108, EX109 e EX110 para o primeiro pacote e mantenha tudo funcionando.
"""

from ex111_files.utilidadescev import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 35, 22, True)

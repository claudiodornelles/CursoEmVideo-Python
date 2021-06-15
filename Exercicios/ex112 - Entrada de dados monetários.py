"""
Dentro do pacotes utilidadesCeV que criamos no EX111 temos um módulo chamado DADO. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como função input(), mas com a validação de dados para aceitar somente valores que sejam monetários.
"""

from ex112_files.utilidadescev import dados
from ex112_files.utilidadescev import moeda

p = dados.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22, True)

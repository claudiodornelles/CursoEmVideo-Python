"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função.
"""


def notas(* valores, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param valores: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    notas = dict()
    notas['Total'] = len(valores)
    notas['Maior'] = max(valores)
    notas['Menor'] = min(valores)
    media = sum(valores)/len(valores)
    notas['Média'] = media

    if sit:
        if media < 5:
            notas['Situação'] = 'RUIM'
        elif media < 7:
            notas['Situação'] = 'RAZOÁVEL'
        else:
            notas['Situação'] = 'BOA'

    return notas


resp = notas(5.5, 4.5, 10, 2.5, 2, 1, sit=True)
print(resp)

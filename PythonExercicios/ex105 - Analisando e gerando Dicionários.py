# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# - quantidade de notas
# - a maior nota
# - a menor nota
# - a média da turma
# - a situação (opcional)

# adicione também as docstrings da função


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: uma ou mais notas dos alunos [aceita várias]
    :param sit: [opcional] mostra a situação (boa, razoável ou ruim) baseado na média
    :return: dicionário com [total, maior, menor, média e situação]
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5, 9.5, 7.5, sit=True)
print(resp)



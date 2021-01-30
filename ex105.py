def notas(*n, sit=False):
    """
    -> Analisa notas de alunos
    :param n: uma ou mais notas
    :param sit: situação do aluno, pode ou não ser mostrada
    :return: dicionário com várias infos do aluno
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'COMPLICADA'
    return r

#PRograma
resp = notas(5.5, 6.5, 7.4, 10, sit=True)
print(resp)
#help(notas)
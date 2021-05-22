def notas(*num, sit=False):
    '''
    -> função  para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita vários)
    :param sit: valor opcional, indica se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação do aluno.
    '''
    nota = {}
    nota['total'] = len(num)
    nota['maior'] = max(num)
    nota['menor'] = min(num)
    nota['media'] = sum(num)/len(num)
    if sit:
        if nota['media'] < 5:
            nota['situação'] = 'RUIM'
        elif nota['media'] < 7:
            nota['situação'] = 'RAZOÁVEL'
        else:
            nota['situação'] = 'BOA'
    return nota


resp = notas(7, 6, sit=True)
print(resp)
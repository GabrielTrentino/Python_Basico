def notas(*num):
    '''
    Função notas utiliza de uma lista de notas para processamento de dados
    :param num: Lista de notas dos alunos de uma sala
    :return: Total, maior nota, menor nota, média geral da sala e situacao de aproveitamento
    '''
    sala = dict()
    sala['total'] = len(num)
    sala['maior'] = max(num)
    sala['menor'] = min(num)
    sala['média'] = sum(num)/len(num)
    if sala['média'] > 8:
        sala['situacao'] = 'TOP'
    elif sala['média'] > 6:
        sala['situacao'] = 'OK'
    else:
        sala['situacao'] = 'RUIM'
    print(sala)

help(notas)
notas(1,2,3,4,5)
aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['nota'] = int(input('Digite a nota de {}: '.format(aluno['nome'])))
if aluno['nota'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['nota'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('O {} está com média {} e está {}'.format(aluno['nome'],aluno['nota'],aluno['situação']))
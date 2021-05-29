Dados = dict()
totaldegols = 0
gols = list()
Dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {Dados["nome"]} jogou? '))
for i in range(0,partidas):
    gol = int(input(f'Quantos gols na {i} partida? '))
    gols.append(gol)
    totaldegols += gol
Dados['gols'] = gols
Dados['total'] = totaldegols
print('-'*40)
print(Dados)
print('-'*40)

for k,v in Dados.items():
    print(f'O campo {k} tem valor {v}')
print('-'*40)

print(f'O Jogador {Dados["nome"]} jogou {partidas} partidas')
for i in gols:
    print('    => Na partida {}, fez {} gols'.format(i-1,gols[i-1]))
print('Totalizando: {}'.format(totaldegols))
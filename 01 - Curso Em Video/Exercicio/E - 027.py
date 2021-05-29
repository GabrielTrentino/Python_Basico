nome = str(input('Digite o nome: ')).strip()
separado = nome.split()
print('Primeiro nome: {}'.format(separado[0]))
print('Ultimo nome: {}'.format(separado[len(separado)-1]))
nome = str(input('Digite o nome: ')).strip()
loc = nome.lower().find('silva')
print(nome[loc:loc+5].lower() == 'silva')
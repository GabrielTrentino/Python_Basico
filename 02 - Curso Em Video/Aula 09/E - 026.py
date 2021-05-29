frase = str(input('Digite a frase: ')).strip().lower()
print('Sua frase possui {} letras A'.format(frase.count('a')))
print('A letra A aparece pela primeira vez no {} caracater'.format(frase.find('a')+1))
print('A letra A aparece pela ultima vez no {} caracter'.format(frase.rfind('a')+1-frase.count(' ')))
from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano de nascimento? '))
idade = atual - nasc
if idade > 20:
    print('Modalidade Master')
elif idade > 19:
    print('Modalidade Sênior')
elif idade > 14:
    print('Modalidade Junior')
elif idade > 9:
    print('Modalidade Infantil')
else:
    print('Modalidade Mirim')
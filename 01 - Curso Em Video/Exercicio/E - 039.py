from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano de nascimento? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade < 18:
    print('Você ainda vai se alistar em até {} anos'.format(18-idade))
elif idade > 18:
    print('Você ja passou do tempo de alistamento.')
    print('Você deve ter se alistado há {} anos'.format(idade-18))
else:
    print('Está na hora de se alistar')
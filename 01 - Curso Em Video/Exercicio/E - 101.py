from datetime import date
def vota(idade):
    print(f'Com {idade} você: ',end ='')
    if idade < 16:
        print('NÃO VOTA')
    elif idade < 18 or idade > 70:
        print('VOTO OPCIONAL')
    else:
        print('VOTA')


print('-'*30)
nasceu = int(input('Que ano você nasceu? '))
idade = date.today().year - nasceu
vota(idade)
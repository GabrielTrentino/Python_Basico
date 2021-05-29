cont = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze'
        'quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
num = int(input('Digite um numero entre 0 e 20: '))
while True:
    if 0 <= num <= 20:
        print('Você digitou {}'.format(cont[num]))
        break
    else:
        print('Tente novamente. ')
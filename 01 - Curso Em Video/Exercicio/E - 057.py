while True:
    sexo = str(input('É Masculino (M) ou Feminino (F)? ')).strip().upper()
    if sexo == 'M' or sexo == 'F':
        break
    else:
        print('Você digitou outra coisa do que foi pedido...')
print('Seu sexo é {}'.format(sexo))
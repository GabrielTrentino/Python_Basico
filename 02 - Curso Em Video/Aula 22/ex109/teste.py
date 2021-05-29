from ex109 import moeda

valor = float(input('Digite o valor: '))

print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor,True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(valor,10, True)}')
print(f'Diminuindo 25%, temos {moeda.diminuir(valor,25, True)}')
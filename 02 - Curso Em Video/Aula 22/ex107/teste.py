from ex107 import moeda

valor = float(input('Digite o valor: '))

print(f'A metade de R${valor:.2f} é R${moeda.metade(valor):.2f}')
print(f'O dobro de R${valor:.2f} é R${moeda.dobro(valor):.2f}')
print(f'Aumentando 10%, temos R${moeda.aumentar(valor,10)}')
print(f'Diminuindo 25%, temos R${moeda.diminuir(valor,25)}')
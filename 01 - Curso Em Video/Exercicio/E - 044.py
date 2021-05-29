print('=====MINHA LOJA=====')
valor = float(input('Qual o preço do produto? R$'))
print('FORMA DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/chegue')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opc = int(input('Qual a opção? '))
if opc == 1:
    print('Desconto de 10% ativado. O seu produto custava R${:.2f} e agora custa R${:.2f}'.format(valor,0.9*valor))
elif opc == 2:
    print('Desconto de 5% ativado. O seu produto custava R${:.2f} e agora custa R${:.2f}'.format(valor, 0.95 * valor))
elif opc == 3:
    print('Não há desconto, preço à pagar R${:.2f}'.format(valor))
elif opc == 4:
    print('Essa opção gera 20% de juros. Desse jeito você está pagando R${:.2f} no lugar de R${:.2f}'.format(1.2*valor,valor))
else:
    print('Escolhe serio, zé')

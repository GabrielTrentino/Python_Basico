valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salario? R$'))
anos = int(input('Quantos anos você irá pagar? '))
prestacao = valor/(anos*12)
print('O valor da prestação é de R${:.2f}'.format(prestacao))
if prestacao > 0.3*salario:
    print('E o emprestimo será negado')
else:
    print('E o emprestimo será aceito')
print('Pois a prestacao equivale a {:.2f}% do salário'.format(prestacao*100/salario))
salario = float(input('Digite o salário: '))
if salario > 1250:
    aumento = salario*0.10
else:
    aumento = salario*0.15
print('O salário de R${:.2f} recebe um aumento de R${:.2f}'.format(salario,aumento))
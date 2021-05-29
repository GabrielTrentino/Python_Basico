def factorial(num, op = False):
    '''
    -> Calcula o Fatorial de um Número
    :param num: O número a ser calculado
    :param op: Mostra ou não a conta
    :return: Retorna o fatorial de num
    '''
    fact = 1
    for num in range(num, 0, -1):
        if op:
            if num >1:
                print(num, end=' x ')
            else:
                print(num, end=' = ')
        fact *= num
    return fact
print(factorial(5, True))

print(factorial(5, False))
help(factorial)
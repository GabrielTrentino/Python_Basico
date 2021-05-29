def aumentar(valor=0, taxa=0, format=False):
    res = valor*(1 + taxa/100)
    return res if format is False else moeda(res)


def diminuir(valor=0, taxa=0, format=False):
    res = valor*(1-taxa/100)
    return res if format is False else moeda(res)


def dobro(valor=0, format=False):
    res = valor*2
    return res if format is False else moeda(res)


def metade(valor=0, format=False):
    res = valor/2
    return res if format is False else moeda(res)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>.2f}'.replace('.',',')

def resumo(valor=0,t1=0,t2=0):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço Analisado: \t{moeda(valor):>10}')
    print(f'Dobro do Preço: \t{dobro(valor,True):>10}')
    print(f'Metade do Preço: \t{metade(valor,True):>10}')
    print(f'{t1}% de aumento:  \t{aumentar(valor,t1,True):>10}')
    print(f'{t2}% de redução:  \t{diminuir(valor,t2,True):>10}')
    print('-'*30)

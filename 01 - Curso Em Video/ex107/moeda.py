def aumentar(valor,taxa):
    res = valor*(1 + taxa/100)
    return res

def diminuir(valor,taxa):
    res = valor*(1-taxa/100)
    return res

def dobro(valor):
    res = valor*2
    return res

def metade(valor):
    res = valor/2
    return res
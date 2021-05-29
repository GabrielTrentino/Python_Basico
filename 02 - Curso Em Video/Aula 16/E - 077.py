palavras = ('AVIÃO', 'CARRO' , 'FUTEBOL', 'SKATE','PYTHON','JAVA','CHUVA','ARVORE','NATUREZA')
for i in palavras:
    print("Na palavra {}, temos: ".format(i), end = '')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end = ' ')
    print('')
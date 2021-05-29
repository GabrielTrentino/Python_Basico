matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = soma3coluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o número para [{linha}, {coluna}]: '))
print('-='*15)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]',end ='')
        if matriz[linha][coluna] %2 ==0 :
            somapar += matriz[linha][coluna]
    soma3coluna += matriz[linha][2]
    print()
print('-='*15)
print(f'A soma dos Pares {somapar}')
print(f'A soma da 3 coluna: {soma3coluna}')
print(f'O maior valor da 2 linha: {max(matriz[1])}')
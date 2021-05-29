num = int(input('Você deseja ver a tabuada de qual valor? '))
while num > 0:
    cont = 0
    for cont in range (0,11,1):
        print(num, ' x ' , cont , ' = ', num*cont)
    num = int(input('Digite o proximo número: '))
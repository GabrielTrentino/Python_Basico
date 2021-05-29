import math

catopo = int(input("Digite o Cateto Oposto: "))
catadj = int(input("Digite o Cateto Adjacente: "))
hipote = int(math.sqrt(pow(catopo,2)+pow(catadj,2)))
print("A hipotenusa desse triangulo é: {}".format(hipote))


n1 = input("Primeiro Aluno: ")
n2 = input("Segudo Aluno: ")
n3 = input("Terceiro Aluno: ")
n4 = input("Quarto Aluno: ")
import random
lista = [n1,n2,n3,n4]
random.shuffle(lista)

print("O escolhido foi: ",lista)
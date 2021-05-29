import math

ang = float(input("Digite o Angulo: "))
ang = (ang*math.pi)/180
senang = round(math.sin(ang),3)
cosang = round(math.cos(ang),3)
tanang = round(math.tan(ang),3)
print("Os valores são: {} , {} , {}".format(senang,cosang,tanang))
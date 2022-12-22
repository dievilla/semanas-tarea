# CASO 3 

print("Bienvenido, por favor siga las intrucciones")
print("")
a1 = int(input("Ingrese la cantidad correspondiente a al articulo numero 1: "))
a2 = int(input("Ingrese la cantidad correspondiente a al articulo numero 2: "))
a3 = int(input("Ingrese la cantidad correspondiente a al articulo numero 3: "))
x1 = 10000
x2 = 10000
x3 = 10000
I1 = (a1 * 10000) * 0.053
I2 = (a2 * 10000) * 0.080
I3 = (a3 * 10000) * 0.16

Tp = a1*x1 + a2*x2 + a3*x3
ImT = I1+I2+I3
Tpi = Tp +  ImT

print("El total a pagar de impuesto correspondiente al articulo 1 es: ",I1)
print("El total a pagar de impuesto correspondiente al articulo 2 es: ",I2)
print("El total a pagar de impuesto correspondiente al articulo 3 es: ",I3)
print("El total a pagar sin impuesto es: ",Tp),
print("El total a pagar con impuestos es: ",Tpi)
print("El total a pagar de impuestos es: ",ImT)


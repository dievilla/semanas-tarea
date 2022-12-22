# CASO 25 CALCULAR LA DISTANCIA ENTRE DOS PUNTOS

from math import sqrt

print("Ingrese los valores del punto 1")
x1 = float(input())
y1 = float(input())

print("Ingrese los valores de punto 2")
x2 = float(input())
y2 = float(input())

distancia = sqrt((x2-x1)**2 +(y2-y1)**2)

print("La distancia entre los dos puntos es: ",distancia )

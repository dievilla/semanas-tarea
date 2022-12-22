# CASO 18 SUMAR MULTIPLOS DE 5 MENORES A 50

contador = 0
suma = 0

numero_maximo = int(input("Introduce el numero maximo: "))

while contador < numero_maximo:
    suma = suma + contador
    contador = contador + 5

print("La suma es: ", suma)




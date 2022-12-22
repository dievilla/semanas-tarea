# CASO 17 EN UN VIAJE, CUANTO SE DEBE COBRAR A CADA ALUMNO Y PAGAR A LA COMPAÑIA DE VIAJES 

num = int(input("Ingrese la cantidad de numeros a promediar: "))

a = 0
for i in range(num):
    b = int(input("Ingrese el numero: "))
    a += b

promedio = a/num
print("El promedio de los numeros es: ", promedio)




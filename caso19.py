# CASO 19 SUMA DE NUMEROS PARES

numero_inicial = int(input("Introduce el numero inicial: "))
numero_final = int(input("Introduce el numero final: "))
cantidad = 0

while numero_inicial < numero_final:
    if numero_inicial % 2 == 0:
        print(numero_inicial)
        cantidad += 1
    numero_inicial += 1

print("hay",cantidad,"numeros pares")
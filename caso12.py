# CASO 12 CUANTO SE DEBE PAGAR POR X CANTIDAD DE LAPICES

n = int(input("Ingrese la cantidad de lapices: "))

if n > 0:
    if n >= 1000:
        costo = n * .85
    else:
        costo = n * .90
print(f"El total a pagar {n} lapices es: ${costo}")


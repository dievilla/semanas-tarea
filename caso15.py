# CASO 15 DESCUENTO DE UN ARTICULO

precio = float(input("Ingrese el precio del articulo: "))
descuento = 0

if precio > 0:
    if precio <= 100:
        descuento = precio * .10
    else:
        if precio < 200:
            descuento = precio * .12
        else:
            descuento = precio * .15

        print (f"El total a pagar es: ${precio - descuento}")
        print(f"El descuento aplicado es: ${descuento}")
# CASO 14 CALCULAR EL TOTAL A PAGAR POR LA COMPRA DE CAMISAS

precio = float(input("Ingresa el precio de la camisa: "))
n = int(input("Ingresa el numero de camisas a compar: "))
total = precio * n
if n > 0:
    if n < 3:
        descuento = total * .10
    else:
         descuento = total * .20
    
    print(f"El total a pagar ya como descuento es: ${total - descuento}")
    print(f"El descuento aplicado es: ${descuento}")
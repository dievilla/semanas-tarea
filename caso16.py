# CASO 16 NUM COMPRENDIDOS ENTRE EL 1 Y 20

i = 1
while i <= 20:
    if i % 2 == 1:
        print(i)
    i = i + 1
    





# CASO 18 CALCULAR LA BECA DE UN ALUMNO SI OBTUVO UN INCREMENTO DEL 18% SOBRE SU BECA ANTERIOR

monto = float(input("Ingrese el monto de la beca anterior: "))
incremento = monto * .18
print(f"El monto actual de la beca es de ${monto+ incremento}")
print(f"El incremento de la beca es de ${incremento}")

# CASO 19 



# CASO 20 CALCULAR EL TOTAL A PAGAR POR LA COMPRA DE CAMISAS

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





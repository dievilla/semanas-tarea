# CASO 24 Un productor de leche lleva el registro de lo que produce en litros, 1 GALON:3.785 LITROS

litros = int(input("Ingresa el numero de litros: "))
precio = float(input("Ingresa el precio del galon de leche: "))

galon = litros / 3.785
total = precio * galon

print("El total a recibir por ",litros," litros de leche es: $",round(total,1))
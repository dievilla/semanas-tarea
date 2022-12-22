# CASO 31 LLENAR UN TANQUE QUE TIENE UNA CAPACIDAD DE 50 MERTOS CUBICOS: 50000 LITROS

capacidad_total = 50000

capacidad_manguera = int(input("Capacidad total de manguera: "))

tiempo_minutos = capacidad_total / capacidad_manguera

tiempo_horas = tiempo_minutos / 60

print("El total de horas que tarda en llenarse el tanque es de: " + str(tiempo_horas) + " horas.")




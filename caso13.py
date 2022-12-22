# CASO 13 CUANTO SE DEBE COBRAR POR EL USO DEL ESTACIONAMIENTO A SUS CLIENTES

horas = int(input("Ingrese las horas: "))
if horas > 0 and horas <= 2:
    total = horas * 5
elif horas <= 2+ 3:
    horas = horas - 2
    total = 10 + ( horas * 4)
elif horas <= 2 + 3 + 5:
    horas = horas - 5
    total = 10 + 12 + (horas * 3)
elif horas > 10:
    horas = horas - 19
    total = 10 + 12 + 15 + (horas * 2)

    print(f"El total a pagar es: ${total}")



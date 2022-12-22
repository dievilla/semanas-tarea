# CASO 10 VALIDACION DE CONTRASEÑA

n = int(input("Ingrese el numero de alumnos: "))
total = 0
if n > 0:
    if n < 30:
        total = 4000
    else:
        if n <= 49:
            total = n * 95
        else:
            if n <= 99:
                total = n * 70
            else:
                total =n * 65
    print(f"El total a pagar por la renta del autobus es: ${total}")
    print(f"El costo del boleto es: ${total/n}")



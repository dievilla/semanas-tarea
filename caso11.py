# CASO 11  SUELDO DE UN TRABAJADOR

horas = int(input("Ingrese las horas trabajadas: "))
pagosxhora =float(input("Ingrese el pago por hora: "))

if horas > 40:
    excedente = horas - 40
    sueldo = (40 * pagosxhora) +(excedente * 2)
else:
    sueldo = horas * pagosxhora

print(f"El sueldo semanal por {horas} horas es: ${sueldo}")


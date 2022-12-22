# CASO 33  Pago a un empleado con horas extra y retenciones

nombre = input("Ingrese el nombre del empleado: ")
salario = float(input("Ingrese el salario basico por hora: "))
h_ord = int(input("Ingrese la cantidad de horas ordinarias trabajadas: "))
e_diu = int(input("Ingrese la cantidad de horas extras diurnas trabajadas: "))
e_noc = int(input("Ingrese la cantidad de horas estras nocturnas trabajadas: "))
e_dom = int(input("Ingrese la cantidad de horas extras dominicales trabajadas: "))

salario_ordinario = h_ord * salario
salario_extra = (e_diu * salario)*1.25 + (e_noc *salario)*1.5 + (e_dom*salario)*1.75

retencion = salario_extra * 0.1

a_pagar = salario_ordinario + salario_extra - retencion 

print("/nPagar al empleado",nombre,"la cantidad de",a_pagar, 
"/nLa retencion fue de: ",retencion)
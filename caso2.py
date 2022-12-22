 #CASO 2 CALCULAR EL PROMEDIO DE 4 CALIFICACIONES

a = float(input("Ingresa la calificasion 1: "))
b = float(input("Ingresa la calificasion 2: "))
c = float(input("Ingresa la calificasion 3: "))
d = float(input("Ingresa la calificasion 4: "))

promedio = (a+b+c+d)/4

print("El promedio de las 4 calificaciones es: ",round(promedio,1))


nombre1 = input("Ingrese en nombre 1: ")
edad1 = int(input("Ingrese la edad: "))

nombre2 = input("Ingrese en nombre 2: ")
edad2 = int(input("Ingrese la edad: "))

nombre3 = input("Ingrese en nombre 3: ")
edad3 = int(input("Ingrese la edad: "))

if edad1 != edad2 and edad1 != edad3 and edad2 != edad3:
    if edad1 < edad2:
        if edad1 < edad3:
            print(f"{nombre1} tiene la menor edad {edad1}")
        else:
            print(f"{nombre3} tiene la menor edad {edad3}")
    else:
        if edad2 < edad3:
            print(f"{nombre2} tiene la menor edad {edad2}")
        else:
            print(f"{nombre3} tiene la menor edad {edad3}")
else:
    print("Las edades tienen que ser diferntes")










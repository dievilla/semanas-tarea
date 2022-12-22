# CASO 34 HAY 2 NUMEROS LA FUNCION DEBE ENCONTRAR CUAL ES EL MAS GRANDE Y RETONARLO

def maximo (num1, num2):
    if((type(num1)==int or type(num1) == float) and (type(num2) == int or type(num2)== float)):
        if(num1 > num2):
            print("No hay un maximo. Son iguales")
        elif(num1 > num2):
            return num1
        else:
            return num2
    else:
        print("Error! Los datos no son correctos")
        return False


num = maximo(3, 10)
if(type(num) != bool):
    print("El maximo es: " + str(num))
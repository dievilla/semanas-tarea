# CASO 35 MINI CALCULADORA PARA DOS NUMEROS

def calculadora():
    operacion = input("¿Que operacion quieres realizar? La opciones son:\n-suma\n-resta\n-potencia ")
    num1 = float(input("Numero 1: "))
    num2 = float(input("Numero 2: "))
    if(operacion == "suma"):
        print(num1+num2)
    if(operacion == "resta"):
        print(num1-num2)
    elif(operacion == "potencia"):
        print(num1**num2)
    else:
        print("La operacion es incorrecta, Las opciones son:\n-suma\n-resta\n-potencia")

calculadora()
calculadora()
calculadora()
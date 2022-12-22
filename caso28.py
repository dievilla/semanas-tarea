# CASO 28 TABLA DE MIULTIPLICAR

tabla = int(input("Introduce la tabla de multiplicar: "))
inicio = 1

while inicio <= 12:
    resultado = tabla * inicio
    
    print(tabla,"*",inicio,"=",resultado)
    
    inicio = inicio + 1

    
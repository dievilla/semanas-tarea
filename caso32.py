# CASO 32 CALCULAR LA SUMA DE 1 HASTA N

n = int(input("Ingrese N: "))

resultado = 0

for i in range(1, 11):
    resultado = resultado + i
    
print("La sumatoria de numeros desde 1 hasta " + str(n) + " es: " + str(resultado))
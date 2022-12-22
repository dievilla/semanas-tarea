# CASO 21 Armar una cuenta regresiva, de 10 a 0

import os
import time

print("Estas preparando para el despegue")
input("Presione la tecla ENTER ")

for numero in range(10,-1,-1):
    print(numero)
    time.sleep(1)
    os.system("cls")

print("Buen viaje!!!")




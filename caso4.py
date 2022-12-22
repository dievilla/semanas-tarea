# CASO 4 QUE PIDA 2 NUMEROS Y SE DEA CUENTA SI SON PAR O IMPAR

print("buenos dias profesor escaja cualquier libro que quiera comprar")

print("1. Algebra")
print("2. Fisica")
print("3. lenguaje")

precioalgebra = 50
preciofisica = 80
preciolenguaje = 45

print("¿Cuantos libros de algebra desea llevar?")
cant1 = int(input())
print("¿Cuantos libros de fisica desea llevar?")
cant2 = int(input())
print("¿Cuantos libros de lenguaje desea llevar?")
cant3 = int(input())

total1 = precioalgebra*cant1
total2 = preciofisica*cant2
total3 = preciolenguaje*cant3
total4 = total1+total2+total3

print("Su compra sale en total de: ", total4, "soles")



# Un sistema de reservas permite elegir entre 3 tipos de evento:
# 1. Cine ($20.000)
# 2. Teatro ($35.000)
# 3. Concierto ($50.000)
# Luego debe ingresar la cantidad de entradas deseadas. Si el total supera los $100.000, se
# aplica un 10% de descuento. Calcula el total a pagar.



print("1 - Cine")
print("2 - Teatro")
print("3 - Concierto")


opcion = int(input("Ingrese el tipo de evento: "))
entradas = int(input("Ingrese la cantidad de entradas: "))

if opcion == 1:
    valor_cine = 20000
    precio = entradas * valor_cine
    descuento = precio * 0.1
    total = precio - descuento
    print(f"El total es {total}")
elif opcion == 2:
    valor_teatro = 35000
    precio =  entradas * valor_teatro
    descuento = precio * 0.1
    total = precio - descuento
    print(f"El total es {total}")
elif opcion == 3:
    valor_concierto = 50000
    precio = entradas * valor_concierto
    descuento = precio * 0.1
    total = precio - descuento
    print(f"El total es {total}")


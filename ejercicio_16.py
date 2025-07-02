# Diseña un algoritmo que reciba un número del 1 al 7 y muestre el día correspondiente de la
# semana. Si se ingresa un número fuera de ese rango, mostrar un mensaje de error. Usa una
# estructura ‘según’ o ‘switch’.


print("1")
print("2")
print("3")
print("4")
print("5")
print("6")
print("7")

opcion = int(input("Ingrese numero: "))

if opcion == 1:
    print("Lunes")
elif opcion == 2:
    print("Martes")
elif opcion == 3:
    print("Miercoles")
elif opcion == 4:
    print("Jueves")
elif opcion == 5:
    print("Viernes")
elif opcion == 6:
    print("Sabado")
elif opcion == 7:
    print("Domingo")
else:
    print("Error")
﻿# Crea un programa que lea un número del 1 al 12 y muestre el nombre del mes
# correspondiente. Por ejemplo, 1 → 'Enero', 2 → 'Febrero', etc. Si se ingresa un número
# inválido, mostrar 'Mes no válido'. 


mes = int(input("Ingrese numero: "))

if mes == 1:
    print("Enero")
elif mes == 2:
    print("Febrero")
elif mes == 3:
    print("Marzo")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Mayo")
elif mes == 6:
    print("Junio")
elif mes == 7:
    print("Julio")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Septiembre")
elif mes == 10:
    print("Octubre")
elif mes == 11:
    print("Noviembre")
elif mes == 12:
    print("Diciembre")
else:
    print("Mes no valido")
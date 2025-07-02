# Desarrolla un algoritmo que muestre un menú con las siguientes opciones:
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Dividir
# El usuario elige una opción e ingresa dos números. El programa debe realizar la operación
# seleccionada y mostrar el resultado. Si la división es por cero, indicar 'No se puede dividir
# por cero'. 




print("1 - suma")
print("2 - resta")
print("3 - multiplicacion")
print("4 - division")



opcion = int(input("Selecion una opcion: "))

if opcion == 1:
    num_1 = int(input("Ingrese el primer numero: "))
    num_2 = int(input("Ingrese el segundo numero: "))
    suma = num_1 + num_2
    print(f"El resultado es {suma}")
elif opcion == 2:
    num_1 = int(input("Ingrese el primer numero: "))
    num_2 = int(input("Ingrese el segundo numero: "))
    resta = num_1 - num_2
    print(f"El resultado es {resta}")
elif opcion == 3:
    num_1 = int(input("Ingrese el primer numero: "))
    num_2 = int(input("Ingrese el segundo numero: "))
    multiplicacion = num_1 * num_2
    print(f"El resultado es {multiplicacion}")
elif opcion == 4:
    num_1 = float(input("Ingrese el primer numero: "))
    num_2 = float(input("Ingrese el segundo numero: "))
    if num_2 == 0:
        print("No se puede dividir por cero")
    else:
        division = num_1 / num_2
        print(f"El resultado es {division}")




    
    
    


    

    
        

    
























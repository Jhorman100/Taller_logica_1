# Un parqueadero cobra según el tipo de vehículo: - Carro → $5.000/hora - Moto → $2.000/hora - Bicicleta → $500/hora
# Diseña un algoritmo que reciba el tipo de vehículo y el número de horas y calcule el total a pagar.


print("1 - Carro")
print("2 - Moto")
print("3 - Bicicleta")


valor_carro = 5000
valor_moto = 2000
valor_bicicleta = 500



opcion = int(input("Selecion el vehiculo: "))

if opcion == 1:
    hora_carro = int(input("Ingrese las horas de parqueo: "))
    valor_total = valor_carro * hora_carro
    print(f"El valor del parqueadero de su carro es {valor_total}")
elif opcion == 2:
    hora_moto = int(input("Ingrese las horas de parqueo: "))
    valor_total = valor_moto * hora_moto
    print(f"El valor del parqueadero de su moto es {valor_total}")
elif opcion == 3:
    hora_bicicleta = int(input("Ingrese las horas de parqueo: "))
    valor_total = valor_bicicleta * hora_bicicleta
    print(f"El valor del parqueadero de su bicicleta {valor_total}")


    
        







# Dependiendo del tipo de actividad, se aplica una retención: - Dependiente → 10% - Independiente → 15% - Empresario → 20%
# Solicita el tipo y el ingreso mensual y calcula el valor del impuesto. Valida que los ingresos
# sean positivos.


print("1 - dependiente")
print("2 - independiente")
print("3 - empresario")

salario = 1500000

opcion = int(input("Selecione el de retencio: "))

if opcion == 1:
    impuesto = salario * 0.1
    retencion = salario - impuesto
    print(f"El valor de la retencion es {impuesto}")
    print(f"El total del sueldo es {retencion}")
elif opcion == 2:
    impuesto = salario * 0.15
    retencion = salario - impuesto
    print(f"El valor de la retencion es {impuesto}")
    print(f"El total del sueldo es {retencion}")
elif opcion == 3:
    impuesto = salario * 0.2
    retencion = salario - impuesto
    print(f"El valor de la retencion es {impuesto}")
    print(f"El total del sueldo es {retencion}")


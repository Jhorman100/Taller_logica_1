# En una tienda de tecnología se aplican descuentos por el valor total de la compra: - Sin descuento si es menor a $100.000 - 5% si está entre $100.000 y $200.000 - 10% si supera los $200.000
# Crea un algoritmo que reciba el valor de la compra y muestre qué porcentaje de descuento
# aplica. 


valor = int(input("El valor de la compra es: "))

if valor < 100000:
    print("No tiene descuento")
elif valor >= 100000 and valor <= 200000:
    print("Tiene el 5% de descuento")
else:
    print("Tiene el 10 % de descuento")
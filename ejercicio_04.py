# Una campaña de donación requiere filtrar a los posibles donantes. Para ser apto, la persona
# debe tener entre 18 y 65 años y pesar al menos 50 kg. Escribe un algoritmo que reciba la
# edad y el peso de una persona, y determine si está apta o no para donar sangre, mostrando
# un mensaje adecuado.


edad = int(input("Cual es su edad: "))
peso = int(input("Cual es su peso: "))

if edad > 18 and edad < 65 and peso == 50:
# pongo igual a 50kg porque en el problema no pone no dice un rango de peso, sino que especifia almenos 50kg
    print("Usted puede donar sangre")
else:
    print("Usted no es apto para donar sangre")


# Una institución educativa aprueba a un estudiante si cumple dos condiciones: una nota final
# igual o superior a 3.0 y una asistencia igual o superior al 80%. Escribe un algoritmo que
# reciba estos dos datos y determine si el estudiante aprueba o reprueba.


nota = float(input("Nota del estudiante: "))
asistencia = str(input("Asistencia del estudiante: "))

if nota >= 3.0 and asistencia >= (f"80%"):
    print("El estudiante aprueba")
else:
    print("El estudiante no aprueba")
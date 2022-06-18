# Bucle Indeterminado: While

print("Automotores la Carreta")

monto = int(input("Ingrese un monto a gastas: "))

while (monto < 500000):
    print("No poseemos vehiculos a ese valor")
    monto = int(input("Ingrese un monto a gastas: "))

print("El monto ingresaso es de ",monto)




while True:
    text = input("Ingrese exit:")
    if (text == "exit"):
        break # Usar Break para salir de un bulce

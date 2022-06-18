
claveJ1 = int(input(" Jugador 1 ingrese un numero clave: "))

while ( claveJ1<1 or claveJ1>10):
    claveJ1 = int(input("Clave Ingresada Incorrecta!!! Vuelva a intentar:"))

claveJ2 = int(input("Jugador 2 intente adivinar la clave en 3 intentos: "))

cant_Intentos = 1

while (claveJ1 != claveJ2):

    if (cant_Intentos == 3):
        print("Juego Terminado. Jugador 2 a Perdido")
        break

    print(" Clave Ingresada Incorrecta!!! Le quedan ", 3-cant_Intentos," intentos:")

    claveJ2 = int(input(" Vuelva a intentar: "))
    cant_Intentos += 1


if (claveJ1 == claveJ2):
    print("!!! CORRECTO !!! Jugador 2 a Ganado. Juego Terminado")


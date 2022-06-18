print ("Banco Patagónico")

nombre_Usuario = input("Ingrese su nombre: ")

intentos = 3

for i in range(intentos):
    correo_Usuario = input("Ingrese su correo electronico: ")

    cant_Arrobas = 0
    puntoDespuesArroba = True
    primerCaracterDistintoDeArrobaYPunto = False
    iteraciones=0
    for j in correo_Usuario:
        
        if (j == "@"):
            cant_Arrobas += 1
        if (j == "." and cant_Arrobas > 0):
            puntoDespuesArroba = True
        if (iteraciones == 0 and j!="@" and j!="."):
            primerCaracterDistintoDeArrobaYPunto = True

        iteraciones += 1
    
    if (cant_Arrobas == 1 and puntoDespuesArroba == True and primerCaracterDistintoDeArrobaYPunto == True):
        print("Segunda etapa del programa.")
        break
    else:
        print("Correo no valido.")

else:
    print("Su contraseña a sido bloqueada.")



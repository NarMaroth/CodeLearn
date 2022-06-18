print ("Banco Patagónico")

nombre_Usuario = input("Ingrese su nombre: ")

intentos = 3

for i in range(intentos):
    correo_Usuario = input("Ingrese su correo electronico: ")

    cant_Arrobas = 0
    for j in correo_Usuario:
        if (j == "@"):
            cant_Arrobas += 1
    
    if (cant_Arrobas == 1):
        print("Segunda etapa del programa.")
        break
    else:
        print("Correo no valido.")

else:
    print("Su contraseña a sido bloqueada.")



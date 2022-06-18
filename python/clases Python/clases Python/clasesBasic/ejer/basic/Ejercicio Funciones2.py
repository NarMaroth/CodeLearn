
def check_If_Afiliado():
    for i in numAfiliados:
        if i == numAfiliado_Usuario:
            return True
    else:
        return False

def cambio_Asignacion_Plan():
    plan_Deseado = input("1. Plan Roble.....$7000\n2. Plan Cedro.....$5500\n3. Plan Arrayán...$4500")
    
    if plan_Deseado == 1:
        print("Ahora tiene Plan Roble")
    elif plan_Deseado==2:
        print("Ahora tiene Plan Cedro")
    else:
        print("Ahora tiene Plan Arrayán")

def gestion_Turnos():
    especialidad_Usuario = input("Ingrese la especialidad que busca:")
    turnoEspecialidad_Usuario = int(input("Seleccione un turno \n1. Lunes 10-14Hs\n2. Lunes 10-16Hs\n3. Jueves 13-11Hs\n4. Viernes 14-12Hs"))

    if(turnoEspecialidad_Usuario == 1):
       print("Turno seleccionado: Lunes 10-14Hs")
    elif (turnoEspecialidad_Usuario == 2):
        print("Turno seleccionado: Lunes 10-16Hs")
    elif (turnoEspecialidad_Usuario == 3):
        print("Turno seleccionado: Jueves 13-11Hs")
    else:
        print("Turno seleccionado: Viernes 14-12Hs")

def llamado_Emergencias():
    direccion_Emergencia = input("Ingrese la dirección de la emergencia:")
    print ("Una ambulancia está en camino a",direccion_Emergencia)

def menu():
    while True:
        eleccion = input("seleccione la operación que desea realizar:\na) Cambio o asignación de plan.\nb) Gestión de turnos.\nc) Llamado a emergencias.\nd) Salir del sistema")
        
        if eleccion == "d":
            break
        elif eleccion == "a":
            cambio_Asignacion_Plan()
        elif eleccion == "b":
            gestion_Turnos()
        elif eleccion == "c":
            llamado_Emergencias()

        print("-------------------------")

def afiliarse():
    nombre_Usuario = input("Ingrese su nombre:")
    edad_Usuario = input("Ingrese su edad:")
    numAfiliados.append(8766)
    print("-------------------------")
    menu()

print("--------------\nSistema de gestión de Salud\n-------------")

numAfiliados = [5443,4456,3321,3210]

numAfiliado_Usuario = int(input("Ingrese su número de afiliado:"))

esAfiliado = check_If_Afiliado()

if esAfiliado:
    menu()
else:
    desea_Afiliarse = input("Desea afiliarse? (Ingrese SI de ser el caso): ")
    desea_Afiliarse.upper()
    if (desea_Afiliarse == "SI"):
        afiliarse()

print("--------------\nPrograma Finalizado\n-------------")
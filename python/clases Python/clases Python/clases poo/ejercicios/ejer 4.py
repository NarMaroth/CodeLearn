decorador = "-"*40

class PRODUCTO():
    def __init__(self,nombre,costo,tipo,marca):
        self.nombre = nombre
        self.costo = costo
        self.tipo = tipo
        self.marca = marca

    def ver_Producto(self):
        print(decorador)
        print(f"Producto: {self.nombre} \n-Marca: {self.marca} \n-Costo: {self.costo} \n-Tipo: {self.tipo}")
        print(decorador)
        
class HERRAMIENTA(PRODUCTO):
    def ver_Garantia(self):

        if self.marca == "Stanley":
            print("- Tiene una garantia de 12 meses")
        else:
            print("- Tiene una garantia de 6 meses")

        print(decorador)

class MAQUINA(HERRAMIENTA):

    def ver_Consumo(self):

        self.potencia_KW = int(input("\nIngrese la potencia de la maquina (Kw): "))
        self.uso = int(input("Ingrese las horas de uso promedio: "))
        self.consumo = self.potencia_KW * self.uso

        print(f"\n- El consumo es de {self.consumo}kwh")
        print(decorador)

class OTRO(PRODUCTO):
    def ingresar_Descripcion(self):

        self.descripcion = input("\n- Ingrese una descripcion del producto")
        print(decorador)


def Ingresar_Producto():
    nombre_Producto = input("\nIngrese el nombre del producto: ")
    marca_Producto = input("Ingrese la marca del producto: ")
    costo_Producto = float(input("Ingrese su costo: "))

    while True:
        tipo_Producto = input("Ingrese que tipo es (Herramienta/Maquina/Otro): ").upper()
        if (tipo_Producto != "HERRAMIENTA" and tipo_Producto != "MAQUINA" and tipo_Producto != "OTRO"):
            print("Respuesta Incorrecta. Ingrese si es Herramienta,Maquina u Otro")
        else:
            break

    if tipo_Producto == "HERRAMIENTA":
        return HERRAMIENTA(nombre_Producto,costo_Producto,tipo_Producto,marca_Producto)
    elif tipo_Producto == "MAQUINA":
        return MAQUINA(nombre_Producto,costo_Producto,tipo_Producto,marca_Producto)
    elif tipo_Producto == "OTRO":
        return OTRO(nombre_Producto,costo_Producto,tipo_Producto,marca_Producto)



print("""\n   ferreteria " La Tuerca " """)

while True:

    producto_Ingresado = Ingresar_Producto()

    respuesta = input("Desea ingresar a un informe del Producto cargado? (Y/N):").upper()
    if respuesta == "Y":
        producto_Ingresado.ver_Producto()

    if producto_Ingresado.tipo == "OTRO":
        respuesta = input("Desea ingresar una descripcion al producto (Y/N): ").upper()
        if respuesta == "Y":
            producto_Ingresado.ingresar_Descripcion()
    else:
        respuesta = input("Desea ver la garantia del producto (Y/N): ").upper()
        if respuesta == "Y":
            producto_Ingresado.ver_Garantia()

        if producto_Ingresado.tipo == "MAQUINA":
            respuesta = input("Desea ver el consumo del producto (Y/N): ").upper()
            if respuesta == "Y":
                producto_Ingresado.ver_Consumo()

    respuesta = input("Desea ingresar algun otro producto (Y/N): ").upper()
    if respuesta == "N":
        break

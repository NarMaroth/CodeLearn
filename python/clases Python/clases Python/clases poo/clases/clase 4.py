

#           SOBRESCRIBIR METODOS:

class PRODUCTOS():
    def __init__(self, prod,precio):
        self.prod=prod
        self.precio=precio

    def informar(self):
        print("producto: ",self.prod," Precio: ",self.precio)



# Sobreescribir el metodo constructor para añadir un parametro (material)
class TORNILLOS (PRODUCTOS):
    def __init__ (self,prod,precio,material):

        super().__init__(prod,precio) #LLama al metodo constructor de la clase superior

        self.material = material

    #Sobrescribiendo el metodo definir para que muestre el material en ves del precio
    def informar(self):
        print("producto: ",self.prod," Material: ",self.material)

t1 = TORNILLOS("Tornillo1",25,"Cobre")
t1.informar()




#           HERENCIA MULTIPLE:

class HERRAMIENTA():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo

    def informa(self):
        print("El producto es un: ",self.marca,self.modelo)


class ELECTRICA():
    def __init__(self,pot):
        self.pot=pot

    def cal_efi(self):
        if (self.pot>100) :
            print("El consumo es alto")
        else:
            print("El consumo es bajo")


# En las clases con multiples herencias, la herencia de la izquierda tiene mayor prioridad que la de la derecha
class HERRAMIENTA_ELECTRICA(HERRAMIENTA,ELECTRICA):
    pass
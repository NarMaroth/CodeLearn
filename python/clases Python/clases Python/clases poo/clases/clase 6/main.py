# Paquetes = carpetas
# Modulos = Archivos

# Paquete Distribuible: Modulos intalados en el sistema y que no se necesita indicar
#la ruta




#from variables import "nombre"    // Para importar algo en particular

from variables import *        #// Asterisco para importar todo
from funciones import *

#- from funciones import nombre as "f_nombre"
#       Si se repiten variables en distintos modulos, el ultimo modulo en ser importado 
#      sobrescribira la variable del modulo importado antes antes.

#- from "otrosModulos.otroModulo" import *
#       Para traer un modulo que se encuentra en otro paquete, indicar la ruta mediante
#      puntos.


from modulos import AUTOS

print(nombre, edad)
# Variables traidas desde el modulo Variables.

Informar()
Sumar()
# Funciones traidas desde el modulo Funciones.

fiesta = AUTOS("Fiesta")
fiesta.Informar()
# Clase traida desde el modulo Clases.
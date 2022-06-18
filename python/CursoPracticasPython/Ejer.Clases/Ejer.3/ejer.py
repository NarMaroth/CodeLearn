import random
import numpy as np
import matplotlib.pyplot as plt


arbol = 1
arbol_quemado = -1

#1)
def generar_bosque(n):
    bosque = [0]*n
    return bosque


#2)
def suceso_aleatorio(p):
    if ( random.random() < p ):
        return True
    return False

def brotes(bosque,p):
    for i in range( len(bosque) ):
        if (suceso_aleatorio(p)):
            bosque[i] = arbol


#3)  
def cuantos(bosque, tipo_celda):
    return bosque.count(tipo_celda)


#4)
def rayos(bosque,f):
    for i in range( len(bosque) ):
        if (suceso_aleatorio(f)):
            if (bosque[i] == arbol):
                bosque[i] = arbol_quemado


#5)
def propagacion(bosque):
    hay_propagacion = True
    while hay_propagacion:
        hay_propagacion = False
        for i in range( len(bosque) ):
            if( bosque[i] == arbol_quemado ):
                if (i != 0 ):   # propagar izquierda si no esta al principio de la lista
                    if(bosque[i-1] == arbol):
                        bosque[i-1] = arbol_quemado
                        hay_propagacion = True
                        
                if ( i != len(bosque)-1): # propagar derecha si no esta al final de la lista
                    if(bosque[i+1] == arbol):
                        bosque[i+1] = arbol_quemado
                        hay_propagacion = True
                        
                # No es performante porque recorre toda la lista multiples veces
                        
"""
primero propago para la derecga y luego vuelvo para la derecha

"""
#6)                      
def limpieza(bosque):
    for i in range( len(bosque) ):
            if( bosque[i] == arbol_quemado ):
                bosque[i] = 0

#7)
def dinamica(n, n_rep, p, f):
    contador_arbolesSobrevivientes = 0
    bosque = generar_bosque(n)
    
    i = 1
    while (i <= n_rep):
        
        brotes(bosque, p)
        rayos(bosque, f)
        propagacion(bosque)
        limpieza(bosque)
        
        contador_arbolesSobrevivientes += cuantos(bosque, arbol)
        i += 1
        
    return contador_arbolesSobrevivientes/n_rep
    

#8)
n = 20
n_rep = 500  

distintas_p = np. arange (0.0 , 1.0 , 0.01)
promedios = []

for p in distintas_p:
    promedios.append( dinamica(n, n_rep, p, 0.02) )

print("Valor optimo de P : " ,distintas_p [promedios.index( max(promedios) )] )

plt. title (" Promedio Cant. Arboles que Sobreviven")
plt. xlabel (" P (Probabilidad de que Cresca un Arbol)", fontsize = 16)
plt. ylabel (" Promedio", fontsize = 16)
plt. plot (distintas_p , promedios , ".")
plt. show ()


# ================================================================











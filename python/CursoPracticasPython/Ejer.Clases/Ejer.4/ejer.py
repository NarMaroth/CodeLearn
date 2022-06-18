# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib . pyplot as plt

import imageio
import os

"""
También es posible preguntar las dimensiones de t: El valor t.shape[0] es su 
cantidad de filas y t.shape[1] es su cantidad de columnas.
"""

cant_desborde = 4
cant_CoposATirar = 1000
tamanoTabla = 21

#3)
def crear_tablero(n):
    tablero = np. repeat (0 ,n*n). reshape (n ,n)
    for i in range(tablero.shape[0]):
        for j in range(tablero.shape[1]):
            if ( j == 0 or j == n-1 or i == 0 or i == n-1 ):
                tablero[(i,j)] = -1
    return tablero


"""
i=0
while i < n+2:
    matriz[0,i] = -1
    matriz[n+1,i] = -1
    matriz[i,0] = -1
    matriz[0,n+1] = -1
    
"""

#4)
t1 = crear_tablero(9)


#5)
def es_borde(tablero, coord):
    if ( tablero[coord] == -1 ):
        return True
    return False

#6)
#print( es_borde(t1,(0,1)) , es_borde(t1,(8,6)), es_borde(t1,(5,6)) )


#7)
def tirar_copo(tablero, coord):
    tablero[coord] += 1


#9)
def vecinos_de(tablero, coord):
    vecinos = []
    
    coord_vecino = (coord[0]+1, coord[1])
    if (tablero[coord_vecino] != -1):
        vecinos.append(coord_vecino)
        
    coord_vecino = (coord[0]-1, coord[1])
    if (tablero[coord_vecino] != -1):
        vecinos.append(coord_vecino)
        
    coord_vecino = (coord[0], coord[1]+1)
    if (tablero[coord_vecino] != -1):
        vecinos.append(coord_vecino)
        
    coord_vecino = (coord[0], coord[1]-1)
    if (tablero[coord_vecino] != -1):
        vecinos.append(coord_vecino)
        
    return vecinos


#10)
"""
print( vecinos_de(t1, (1, 4)) ) 
print( vecinos_de(t1, (2, 5)) )
print( vecinos_de(t1, (7, 7)) )
"""

#11)
def desbordar_posicion(tablero, coord):
    if ( tablero[coord] >= cant_desborde ):
        tablero[coord] -= 4
        for i in vecinos_de(tablero, coord):
            tablero[i] += 1

        
#12)
def desbordar_valle(tablero):
    for i in range(tablero.shape[0]):
        for j in range(tablero.shape[1]):
            desbordar_posicion(tablero, (i,j))

#13)
def hay_que_desbordar(tablero):
    for i in range(tablero.shape[0]):
        for j in range(tablero.shape[1]):
            if (tablero[(i,j)] >= cant_desborde ):
                return True
    return False


#14)
def estabilizar(tablero):
    while ( hay_que_desbordar(tablero) ):
        desbordar_valle(tablero) 

#15)
def paso(tablero):
    mitad = int((tablero.shape[0]/2))
    coord_MitadDelTablero = (mitad,mitad) 
    tirar_copo(tablero, coord_MitadDelTablero)
    estabilizar(tablero)
        
        
        
        
# -----------------------------------------------------------------------

def guardar_foto (t, paso ):
    dir_name = "output"
    if not os. path . exists ( dir_name ): # me fijo si no existe el directorio
        os. mkdir ( dir_name ) #si no existe lo creo
        
    ax = plt .gca ()
    file_name = os. path . join ( dir_name , "out {:05}.png". format ( paso ))
    plt. imshow (t, vmin = -1 , vmax =3)
    ax. set_title (" Copos tirados : {}". format ( paso +1)) # titulo
    plt. savefig ( file_name )

def hacer_video ( cant_fotos ):
    dir_name = "output"
    lista_fotos =[]
    for i in range ( cant_fotos ):
        file_name = os. path . join ( dir_name , "out {:05}.png". format (i))
        lista_fotos . append ( imageio . imread ( file_name ))
        
    video_name = os. path . join ( dir_name , " avalancha.mp4")
    # genero el video con 10 Copos por segundo . Explorar otros valores :
    imageio . mimsave ( video_name , lista_fotos , fps =10)
    print ('Estamos trabajando en el directorio ', os. getcwd ())
    print ('y se guardo el video :', video_name )


def probar (n, pasos =200):
    t = crear_tablero (n)
    for i in range ( pasos ):
        paso (t)
        guardar_foto (t, i)
        
    hacer_video ( pasos )
    return t

probar(tamanoTabla,cant_CoposATirar)
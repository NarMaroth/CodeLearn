# -*- coding: utf-8 -*-

import random
import numpy as np





#1)
def crear_album(figus_total):
    album = [0]*figus_total
    return album


#2)
def hay_alguno(l,e):
    if (l.count(e) >= 1):
        return True
    return False


#3)
def comprar_una_figu(figus_total):
    return random.randint(0, figus_total-1)


#4)
def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    
    cant_figusCompradas = 0
    while hay_alguno(album, 0):
        figu = comprar_una_figu(figus_total)
        album[figu] = 1
        
        cant_figusCompradas += 1

    return cant_figusCompradas


#5)
"""
print( 
      (cuantas_figus(670) +
      cuantas_figus(670) +
      cuantas_figus(670) +
      cuantas_figus(670) +
      cuantas_figus(670) ) / 5
      )    
"""

#6)
def experimentar(figus_total, n_rep):
    lista_figusCompradas = []
    
    i = 0
    while i < n_rep:
        lista_figusCompradas.append( cuantas_figus(figus_total) )
        
        i += 1
        
    return lista_figusCompradas
        
        
#7)
#print ( np.mean( experimentar(6, 1000) ) )
        

#8)
#print ( np.mean( experimentar(670, 100) ) )


# ========================= Paquetes =====================================


#1)
"""
paquete = []
paquete.append( comprar_una_figu(670) )
paquete.append( comprar_una_figu(670) )
paquete.append( comprar_una_figu(670) )
paquete.append( comprar_una_figu(670) )
paquete.append( comprar_una_figu(670) )
"""


#2)
def generar_paquete(figus_total, figus_paquete):
    paquete = []
    for i in range(figus_paquete):
        paquete.append( comprar_una_figu(figus_total))
    return paquete


#3)
def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    
    cant_paquetes = 0
    while hay_alguno(album, 0):
        paquete = generar_paquete(figus_total, figus_paquete)
        for i in paquete:
            album[i] = 1
            
        cant_paquetes += 1
        
    return cant_paquetes

#4)
def experimetar_con_paquetes(figus_total, figus_paquete, n_rep):
    lista_paquetesComprados = []
    
    for i in range(n_rep):
        lista_paquetesComprados.append( cuantos_paquetes(figus_total, 
                                                         figus_paquete) )
        
    return lista_paquetesComprados


#5)
print ( np.mean( experimetar_con_paquetes(670, 
                                          5, 
                                          100) ) )




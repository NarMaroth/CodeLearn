# -*- coding: utf-8 -*-

import random
import numpy as np



cant_cartas = 13



#1)
def generar_mazo(n):
    nuevo_mazo =  []
    for i in range(n):
        nuevo_mazo.extend( np.arange(1,cant_cartas+1) )
        
    random.shuffle(nuevo_mazo)
    return nuevo_mazo


#2)
def jugar(m):
    puntos = 0
    while (puntos < 21) and (m != []):
            puntos += m[0]
            m.pop(0)
    return puntos


#3)
def jugar_varios(m, j):
    puntajes = []
    for i in range(j):
        puntajes.append( jugar(m) )
        
    return puntajes


#4)
def ver_quien_gano(resultados):
    ganadores = []
    
    for i in resultados:
        if i == 21:
            ganadores.append(1)
        else:
            ganadores.append(0)
            
    return ganadores


#5)
def experimentar(rep, n):
    partidas_ganadas =[0]*n
    
    m = generar_mazo(n)
    for i in range(rep):
        resultados = jugar_varios(m, n)
        ganadores = ver_quien_gano(resultados)
        for j in range(n):
            if ganadores[j] == 1:
                partidas_ganadas[j] +=1
                
    return partidas_ganadas


print(experimentar(10, 4))
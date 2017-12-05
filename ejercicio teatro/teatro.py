'''
Created on 29 nov. 2017

@author: Diego
'''

import pandas as pd


def leerPlanta():
    planta = pd.DataFrame.from_csv("planta.csv", sep=",", index_col="fila")
    return planta

def mostrarPlanta():
    print("Planta del teatro:")
    # lo leo en cada muestra, previendo nuevos requerimientos de uso concurrente
    planta = leerPlanta()
    print(planta)
    
def grabarVenta(numeroFila,columna):
    # lo leo en cada grabacion, previendo nuevos requerimientos de uso concurrente
    # falta implementar la validacion de butaca ocupada: uso concurrente
    planta = leerPlanta() 
    planta = planta.copy()
    fila = planta.ix[numeroFila]
    fila = fila.copy()
    fila[columna]=1
    planta.ix[numeroFila]=fila    
    planta.to_csv("planta.csv", sep=",")

def imprimirEntrada(numeroFila,columna):
    print("Entrada para la Fila ",numeroFila," en la posicion ",columna)
    # implementar impresion en papell

def estadisticas():
    planta = leerPlanta() # Planta es un objeto del tipo DataFrame
    contadorAsientos = planta.count().sum()
    contadorAsientosUsados = planta.sum().sum()
    print("total asientos: ",contadorAsientos)
    print("total usados: ",contadorAsientosUsados)
    print("porcentaje ocup.: ",(contadorAsientosUsados/contadorAsientos)*100)

def estaVendidaButaca(fila, columna):
    """Esta funcion retorna True si la butaca en la fila y columna pasadas por 
    parametro esta vendida, en otro caso retorna False."""
    planta = leerPlanta()
    fila = planta.ix[fila]
    return fila[columna] == 1

def taquilla():
    continua = 'si'
    while (continua == 'si'):
        mostrarPlanta()
        numeroFila = int(input("Ingrese Fila"))
        columna = input("Ingrese Columna")
        if estaVendidaButaca(numeroFila, columna):
            print("La butaca Fila=",numeroFila," Columna=",columna," fue vendida previamente.")
        else:
            grabarVenta(numeroFila, columna)
            imprimirEntrada(numeroFila, columna)
        continua = input("continua? si/no")
    estadisticas()
              
taquilla()
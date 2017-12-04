'''
Created on 29 nov. 2017

@author: Diego
'''

import pandas as pd


def leerPlanta():
    planta = pd.DataFrame.from_csv("C:/Users/Diego/Documents/111mil/diegoromero/ejercicio teatro/planta.csv", sep=",", index_col="fila")
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
    planta.to_csv("C:/Users/Diego/Documents/111mil/diegoromero/ejercicio teatro/planta.csv", sep=",")

def imprimirEntrada(numeroFila,columna):
    print("Entrada para la Fila ",numeroFila," en la posicion ",columna)
    # implementar impresion en papell

def estadisticas():
    contadorAsientos = 0
    contadorAsientosUsados = 0
    planta = leerPlanta()
    for index, row in planta.iterrows():
        for asiento in row:
            contadorAsientos = contadorAsientos + 1
            if (asiento==1):
                contadorAsientosUsados = contadorAsientosUsados + 1

    print("total asientos: ",contadorAsientos)
    print("total usados: ",contadorAsientosUsados)
    print("porcentaje ocup.: ",(contadorAsientosUsados/contadorAsientos)*100)



def taquilla():
    continua = 'si'
    while (continua == 'si'):
        mostrarPlanta()
        numeroFila = int(input("Ingrese Fila"))
        columna = input("Ingrese Columna")
        grabarVenta(numeroFila, columna)
        imprimirEntrada(numeroFila, columna)
        continua = input("continua? si/no")
    estadisticas()
        
        
taquilla()
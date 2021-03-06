'''
Created on 29 nov. 2017

@author: Diego
'''

import pandas as pd


def leerPlanta():
    planta = pd.DataFrame.from_csv("data/planta.csv", sep=",", index_col="fila")
    return planta

def mostrarPlanta():
    print("Planta del teatro:")
    # lo leo en cada muestra, previendo nuevos requerimientos de uso concurrente
    planta = leerPlanta()
    print(planta)
    
def grabarVenta(numeroFila,columna):
    # lo leo en cada grabacion, previendo nuevos requerimientos de uso concurrente
    planta = leerPlanta() 
    planta = planta.copy()
    fila = planta.ix[numeroFila]
    fila = fila.copy()
    fila[columna]=1
    planta.ix[numeroFila]=fila    
    planta.to_csv("data/planta.csv", sep=",")

def cancelarVenta(numeroFila,columna):
    # lo leo en cada grabacion, previendo nuevos requerimientos de uso concurrente
    planta = leerPlanta() 
    planta = planta.copy()  
    fila = planta.ix[numeroFila]
    fila = fila.copy()
    fila[columna]=0
    planta.ix[numeroFila]=fila    
    planta.to_csv("data/planta.csv", sep=",")
    
def imprimirEntrada(numeroFila,columna):
    print("Entrada para la Fila ",numeroFila," en la posicion ",columna)
    # implementar impresion en papell

def estadisticas():
    planta = leerPlanta() # Planta es un objeto del tipo DataFrame
    
    print("Ocupacion por filas:")
    ocu_filas = (planta.sum(axis=1) / planta.count(axis=1)) * 100 
    print(ocu_filas)
    
    print("Ocupacion por columnas:")
    ocu_columnas = (planta.sum(axis=0) / planta.count(axis=0)) * 100 
    print(ocu_columnas)
    
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

def esValidaFila(fila):
    """Retorna True si la fila pasada como parametro, es una fila valida."""
    planta = leerPlanta()
    return fila in planta.index.values

def esValidaColumna(columna):
    """Retorna True si la columna pasada como parametro, es una columna valida."""
    planta = leerPlanta()
    return columna in planta

def venderButaca(fila, columna):
    """Vende la butaca correspondiente a la fila y la columna. Valida que no haya sido
    vendida previamente. En caso de que la butaca este vendida levanta una excepcion"""
    if estaVendidaButaca(fila, columna):
        raise Exception("La butaca esta vendida")
    grabarVenta(fila, columna)
    imprimirEntrada(fila, columna)

def cancelarButaca(fila, columna):
    """Cancela la butaca correspondiente a la fila y la columna. Valida que haya sido
    vendida previamente. En caso de que la butaca no este vendida levanta una excepcion"""
    if not estaVendidaButaca(fila, columna):
        raise Exception("La butaca no esta vendida")
    cancelarVenta(fila, columna)
    imprimirEntrada(fila, columna)

def taquilla():
    continua = 'si'
    while (continua == 'si'):
        mostrarPlanta()
        numeroFila = int(input("Ingrese Fila"))
        if not esValidaFila(numeroFila):
            print("Numero de fila invalido")
            continue
        columna = input("Ingrese Columna")
        if not esValidaColumna(columna):
            print("Columna invalida")
            continue
        try:
            venderButaca(numeroFila, columna)
        except Exception as e:
            print("La butaca Fila=",numeroFila," Columna=",columna," fue vendida previamente.")
        continua = input("continua? si/no")
    estadisticas()
 

if __name__ == "__main__":
    taquilla()
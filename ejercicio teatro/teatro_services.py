'''
Created on 29 nov. 2017

@author: Diego
'''

import pandas as pd
from flask import Flask
app = Flask(__name__)

def leerPlanta():
    planta = pd.DataFrame.from_csv("planta.csv", sep=",", index_col="fila")
    return planta

@app.route('/verPlanta')
def leerPlantaHtml():
    planta = pd.DataFrame.from_csv("planta.csv", sep=",", index_col="fila")
    html = "<table border='1'>"
    for index, row in planta.iterrows():
        if (index==1):
            html=html+"<tr><td>Fila</td>"
            for asiento in row.index:
                html=html+"<td>"+str(asiento)+"</td>"
            html=html+"</tr>"
                
        html = html + "<tr><td>"+str(index)+"</td>"
        for asiento in row.index:
            if row[asiento]==1:
                estadoAsiento = 'Ocupado'
            else:
                estadoAsiento = 'Libre'
                                
            html = html + "<td><b>"+estadoAsiento+"</b></td>"
        html = html + "</tr>"
    html = html + "</table>"
    return(html)


@app.route('/verPlantaWS')
def leerPlantaWS():
    planta = pd.DataFrame.from_csv("planta.csv", sep=",", index_col="fila")
    response = ''
    for index, row in planta.iterrows():             
        response=response+",".join(map(str, row.values))+"\n"
    return response

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
        
        
#taquilla()

app.run(host='0.0.0.0')
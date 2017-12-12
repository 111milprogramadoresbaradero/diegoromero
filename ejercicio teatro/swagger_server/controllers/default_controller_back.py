import connexion
from swagger_server.models.butaca import Butaca
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from .. import teatro

def planta_leer_get(fila=None, columna=None):
    """
    Retorna el estado de la planta
    
    :param fila: Numero de la fila a consular
    :type fila: str
    :param columna: Numero de la fila a consular
    :type columna: str

    :rtype: List[Butaca]
    """
    planta = teatro.leerPlanta()
   
    filas = []
    if fila == None:
        filas = planta.index
    else:
        filas = [int(fila)]
    
    columnas = []
    if columna == None:
        columnas = planta.columns
    else:
        columnas = [columna]
    
    butacas = []
    for each_fila in filas:
        fila_series = planta.ix[each_fila]          
        for each_columna in columnas:
            try:
                each_butaca = Butaca(each_fila, each_columna, str(fila_series[each_columna]))
                butacas.append(each_butaca)
            except KeyError as e:
                print("La columna no existe {}".format(each_columna))
    return butacas


def planta_vender_get(fila, columna):
    """
    Vende la butaca ubicada en columna y fila. Retorna -1 si la butaca no pudo ser vendida y 0 en caso de que se haya vendido
    
    :param fila: Numero de la fila a vender
    :type fila: str
    :param columna: Columna a vender
    :type columna: str

    :rtype: int
    """
    try:
        teatro.venderButaca(int(fila), columna)
        return 0
    except Exception as e:
        print(e)
        return -1

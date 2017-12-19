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
    print("Inicia planta_leer_get()")
    planta = teatro.leerPlanta()
   
    filas = []
    if fila == None:
        filas = planta.index
    else:
        filas = [fila]
    
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
    print("Finaliza planta_leer_get()")
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
    print("Inicia planta_vender_get()")
    try:
        teatro.venderButaca(fila, columna)
        print("Finaliza planta_vender_get()")
        return 0
    except Exception as e:
        print(e)
        return -1

def planta_cancelar(fila, columna):
    """
    Cancela la butaca ubicada en columna y fila. Retorna -1 si la butaca no pudo ser cancelada y 0 en caso de que se haya cancelado
    
    :param fila: Numero de la fila a cancelar
    :type fila: int
    :param columna: Columna a cancelar
    :type columna: str

    :rtype: int
    """
    print("Inicia planta_cancelar()")
    try:
        teatro.cancelarButaca(fila, columna)
        print("Finaliza planta_cancelar()")
        return 0
    except Exception as e:
        print(e)
        return -1

def menu_get():
    """
    Retorna un menu de opciones para el usuario
    

    :rtype: int
    """
    table_str = "<table><tr><td>Leer</td><td>Comprar</td><td>Cancelar</td></tr></table>"
    return '<html><head><title>Este es el menu del Teatro Colon</title></head><body>{}</body></html>'.format(table_str)

def leer_get(accion=None, fila=None, columna=None):
    """
    Lee toda la planta y retorna un html
    
    :param accion: 
    :type accion: str
    :param fila: Numero de la fila a cancelar
    :type fila: int
    :param columna: Columna a cancelar
    :type columna: str

    :rtype: int
    """
    if accion == "vender" and fila != None and columna != None:
        teatro.venderButaca(fila, columna)
    elif accion == "cancelar" and fila != None and columna != None:
        teatro.cancelarButaca(fila, columna)
        
    html_str = "<html><head><title>Planta Teatro Colon</title></head><body><table border=1>{}</table></body></html>"
    planta = teatro.leerPlanta()
    
    # Imprime el encabezado
    rows_str = "<tr><td></td>"
    for col in planta.columns:
        rows_str = rows_str +"<td>{}</td>".format(col)
    rows_str = rows_str + "</tr>"
    
    column_idx = 0
    for fila in planta.index:
        rows_str = rows_str + "<tr><td>{}</td>".format(fila)
        column_idx = 0
        for each in planta.ix[fila]:
            texto = ""
            url_str = "http://localhost:8080/v1"
            if each == 1:
                url_str = url_str + "/leer?accion=cancelar&fila={}&columna={}"
                texto = "Vendido"
            else:
                url_str = url_str + "/leer?accion=vender&fila={}&columna={}"
                texto = "Disponible"
            url_str = url_str.format(fila, planta.columns[column_idx])
            rows_str = rows_str + '<td><a href="{}">{}</a></td>'.format(url_str, texto)
            column_idx = column_idx + 1
        rows_str = rows_str + "</tr>"

    return html_str.format(rows_str)
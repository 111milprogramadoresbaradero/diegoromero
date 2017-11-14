'''
Created on 4 nov. 2017
@author: Diego
'''
import datetime as dt

DIA = "dia"
PROD = "prod"

def mostrarProductos(diccionario):
    for a in diccionario:
        print(a+"-> "+diccionario[a]["nombre"]+" - $"+str(diccionario[a]["precio"]))
        
def aplicarDescuento(producto, descuentos):
    codigo = producto["codigo"]
    dia = dt.datetime.today().weekday()
    desc_dia = descuentos[DIA][dia]
    desc_prod = 0
    if codigo in descuentos[PROD]:
        desc_prod = descuentos[PROD][codigo]
    total_desc = desc_dia + desc_prod
    if (total_desc > 0.5):
        total_desc = 0.5
    return total_desc

def sumaTicket(ticket):
    sumaTotalTicket = 0
    for total_producto in ticket[2]:
        sumaTotalTicket = sumaTotalTicket + total_producto
    return sumaTotalTicket   

def mostrarTicket(ticket):    
    print("Total: ", sumaTicket(ticket))

descuentos = {}
descuentos[DIA] = [0.2,0.3,0,0,0,0,0] 
descuentos[PROD] = {"A001": 0.25}
productos = {}
productos["A001"]={"nombre":"yerba","precio":75, "codigo":"A001"}
productos["A002"]={"nombre":"azucar","precio":25, "codigo":"A002"}
productos["A003"]={"nombre":"agua","precio":15, "codigo":"A003"}
productos["A004"]={"nombre":"pan","precio":35, "codigo" : "A004"}

ticket = [[],[],[]]

#debug
termina = 'no'
while termina == 'no':
    mostrarProductos(productos)
    codigo = input("ingresar codigo de articulo")
    cantidad = input("ingresar cantidad de articulo")
    ticket[0].append(int(cantidad))
    producto = productos[codigo]
    ticket[1].append(producto["nombre"])
    descuento = aplicarDescuento(producto, descuentos)
    print(descuento)
    total = int(cantidad)*producto["precio"] * (1 - descuento)        
    ticket[2].append(total)
    termina = input("termina? si/no")




mostrarTicket(ticket)

'''
Created on 4 nov. 2017
@author: Diego
'''

def mostrarProductos(diccionario):
    for a in diccionario:
        print(a+"-> "+diccionario[a]["nombre"]+" - $"+str(diccionario[a]["precio"]))


def mostrarTicket(matriz):
    sumaTotalTicket = 0
    for a in range(0,len(matriz)):
        print(matriz[a]["cantidad"]," - ",matriz[a]["producto"]," - $",matriz[a]["precio"])
        sumaTotalTicket = sumaTotalTicket + matriz[a]["precio"]
    print("Total: ",sumaTotalTicket)       


productos = {}
productos["A001"]={"nombre":"yerba","precio":75}
productos["A002"]={"nombre":"azucar","precio":25}
productos["A003"]={"nombre":"agua","precio":15}
productos["A004"]={"nombre":"pan","precio":35}

ticket = []

#debug
termina = 'no'
while termina == 'no':
    mostrarProductos(productos)
    codigo = input("ingresar codigo de articulo")
    cantidad = input("ingresar cantidad de articulo")
    #item = {"cantidad":int(cantidad),"producto":productos[codigo]["nombre"],"precio":int(cantidad)*productos[codigo]["precio"]}
    item = {}
    item["cantidad"]=int(cantidad)
    item["producto"]=productos[codigo]["nombre"]
    item["precio"]=int(cantidad)*productos[codigo]["precio"]
    ticket.append(item)                          
    termina = input("termina? si/no")

   
mostrarTicket(ticket)
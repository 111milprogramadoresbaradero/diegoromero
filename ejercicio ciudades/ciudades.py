import csv

ciudadesFile = open('ciudades.csv', mode='r', encoding="utf8", errors='ignore')
reader = csv.reader(ciudadesFile)
contador = 0
acumuladorPoblacion = 0

dictPaises = {}

for row in reader:
    # Saltea primer registro con cabeceras
    if (contador > 0):                
        if (row[4]!=''): # en el dataset, hay muchas ciudades sin poblacion
            if row[0] not in dictPaises.keys(): # crea una entrada al diccionario para cada codigo de pais                                 
                dictPaises[row[0]]=[]
            
            dictPaises[row[0]].append(row)            
            acumuladorPoblacion = acumuladorPoblacion + int(row[4])
                        
    contador=contador+1


#print(dictCiudades.keys())

# Calcula la ciudad mas poblada por pais
for pais in dictPaises.keys():
    max = []
    for ciudad in dictPaises[pais]:
        
        if (len(max)==0):
            max = ciudad
        if int(ciudad[4])>int(max[4]):
            max = ciudad
    
    print(pais,max,len(dictPaises[pais]))
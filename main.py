from classColeccion import Lista
from classMenu import Menu
from classObjectEncoder import ObjectEncoder
import json
import os
if __name__=='__main__':
    jsonF=ObjectEncoder()
    diccionario=jsonF.leerJSONArchivo('vehiculos.json')
    vehiculos=jsonF.decodificarDiccionario(diccionario)
    lista=Lista()
    lista=vehiculos
    menu= Menu()
    salir= False     
    os.system('cls')      
    while not salir:
            print("""-------------------Menu-------------------
1- INSERTAR VEHICULO
2- AGREGAR VEHICULO
3- TIPO POR POSICION
4- MODIFICAR PRECIO BASE(PATENTE)
5- AUTO MENOR IMPORTE
6- TODOS LOS VEHICULOS
7- CREAR ARCHIVO JSON
8- SALIR""")
            op= input('\n INGRESE UNA OPCION: ')
            if op in ('1','2','3','4','5','6','7','8'):
                menu.opcion(int(op),lista)
                if op=='8':
                    salir=True
            else:
                os.system('cls')
                print ("---OPCION NO VALIDA---")
            os.system('cls')
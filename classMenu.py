from classUsado import VehiculoUsado
from classNuevo import VehiculoNuevo
from classVehiculo import Vehiculo
import os
from classObjectEncoder import ObjectEncoder

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5,
                            6:self.opcion6,
                            7:self.opcion7,
                            8:self.salir
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self,op,li):
        func= self.__switcher.get(op, lambda: print("Opción no válida"))
        func(li)

    def salir(self,li):
        jsonF=ObjectEncoder()
        d=li.toJSON()
        jsonF.guardarJSONArchivo(d,'vehiculos.json')
        print('Salida del programa')

    def opcion1(self,li):
        os.system('cls')
        band=False
        print('~~~~~INSERTAR VEHICULO~~~~~')
        tipo=input('TIPO(NUEVO/USADO):')
        while not band:
            if tipo.upper()=='NUEVO':
                os.system('cls')
                print('~~~~~INSERTAR VEHICULO NUEVO~~~~~')
                modelo=input('MODELO DEL VEHICULO:')
                puertas=input('CANTIDAD DE PUERTAS:')
                color=input('COLOR:')
                precio=input('PRECIO BASE:')
                version=input('VERSION (BASE/FULL):')
                vehiculo=VehiculoNuevo(modelo, puertas, color, precio, version)
                band=True
            elif tipo.upper()=='USADO':
                os.system('cls')
                print('~~~~~INSERTAR VEHICULO USADO~~~~~')
                modelo=input('MODELO DEL VEHICULO:')
                puertas=input('CANTIDAD DE PUERTAS:')
                color=input('COLOR:')
                precio=input('PRECIO BASE:')
                marca=input('MARCA:')
                patente=input('PATENTE:')
                año=input('AÑO DEL VEHICULO:')
                km=input('KILOMETRAJE:')
                vehiculo=VehiculoUsado(modelo, puertas, color, precio, marca, patente, año, km)
                band=True
            else:
                os.system('cls')
                print('~~~~~INSERTAR VEHICULO~~~~~')
                print('TIPO INCORRECTO-REINTENTE')
                tipo=input('TIPO(NUEVO/USADO):')
        os.system('cls')
        posicion=int(input('\nPOSICION QUE DESEA AGREGAR:'))
        li.insertarElemento(vehiculo,posicion)
        li.listar()
        input()
        os.system('cls')
        
    def opcion2(self,li):
        os.system('cls')
        band=False
        print('~~~~~AGREGAR VEHICULO~~~~~')
        tipo=input('TIPO(NUEVO/USADO):')
        while not band:
            if tipo.upper()=='NUEVO':
                os.system('cls')
                print('~~~~~INSERTAR VEHICULO NUEVO~~~~~')
                modelo=input('MODELO DEL VEHICULO:')
                puertas=input('CANTIDAD DE PUERTAS:')
                color=input('COLOR:')
                precio=input('PRECIO BASE:')
                version=input('VERSION (BASE/FULL):')
                vehiculo=VehiculoNuevo(modelo, puertas, color, precio, version)
                band=True
            elif tipo.upper()=='USADO':
                os.system('cls')
                print('~~~~~INSERTAR VEHICULO USADO~~~~~')
                modelo=input('MODELO DEL VEHICULO:')
                puertas=input('CANTIDAD DE PUERTAS:')
                color=input('COLOR:')
                precio=input('PRECIO BASE:')
                marca=input('MARCA:')
                patente=input('PATENTE:')
                año=input('AÑO DEL VEHICULO:')
                km=input('KILOMETRAJE:')
                vehiculo=VehiculoUsado(modelo, puertas, color, precio, marca, patente, año, km)
                band=True
            else:
                os.system('cls')
                print('~~~~~INSERTAR VEHICULO~~~~~')
                print('TIPO INCORRECTO-REINTENTE')
                tipo=input('TIPO(NUEVO/USADO):')
        os.system('cls')
        li.agregarElemento(vehiculo)
        li.listar()
        input()
        os.system('cls')
    
    def opcion3(self,li):
        os.system('cls')
        print('~~~~~TIPO DE OBJETO EN POSICION~~~~~')
        pos=int(input('INGRESE POSICION:'))
        li.tipoPosicion(pos)
        input()
        os.system('cls')
    
    def opcion4(self,li):
        os.system('cls')
        print('~~~~~MODIFICAR PRECIO BASE~~~~~')
        pat=input('INGRESE PATENTE DE AUTO USADO: ')
        li.modificarPrecio(pat)
        input()
        os.system('cls')
        
    def opcion5(self,li):
        os.system('cls')
        print('~~~~~AUTO/S CON MENOR IMPRTE~~~')
        li.economico()
        input()
        os.system('cls')
        
    def opcion6(self,li):
        os.system('cls')
        print('~~~~~TODOS LOS VEHICULOS~~~')
        li.todos()
        input()
        os.system('cls')
    
    def opcion7(self,li):
        jsonF=ObjectEncoder()
        os.system('cls')
        print('~~~~~CREAR ARCHIVO JSON~~~')
        d=li.toJSON()
        jsonF.guardarJSONArchivo(d,'vehiculos.json')
        print('~~~~~ARCHIVO CREADO~~~')
        input()
        os.system('cls')
        
from classNodo import Nodo
from zope.interface import Interface
from zope.interface import implementer
from InterfaceLista import ILista
from classNuevo import VehiculoNuevo
from classUsado import VehiculoUsado
from classVehiculo import Vehiculo 
@implementer(ILista)
class Lista:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0

    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def listar(self):
        print('-----------------------------------------------------')
        for dato in self:
            print(dato)
            print('-----------------------------------------------------')

    def insertarElemento(self,elemento,posicion):
        nodo=Nodo(elemento)
        aux=self.__comienzo
        if posicion>=0 and (self.__tope==posicion==0 or posicion<self.__tope):
            if aux==None or posicion==0:
                nodo.setSiguiente(self.__comienzo)
                self.__comienzo=nodo
                self.__actual=self.__comienzo
                self.__tope+=1
            else:
                while self.__indice!=posicion:
                    ant=aux
                    aux=aux.getSiguiente()
                    self.__indice+=1
                ant.setSiguiente(nodo)
                nodo.setSiguiente(aux)
                self.__indice=0
                self.__tope+=1
                print('EL ELEMENTO SE INSERTO EN LA POSICION ',posicion)
        else:
            print('NO EXISTE LA POSICION {} EN LA LISTA ENLAZADA:'.format(posicion))
        
    def agregarElemento(self,elemento):
        nodo=Nodo(elemento)
        aux=self.__comienzo
        if aux==None:
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo=nodo
            self.__actual=self.__comienzo
            self.__tope+=1
        else:
            ant=aux
            aux=aux.getSiguiente()
            while aux!=None:
                ant=aux
                aux=aux.getSiguiente()
            ant.setSiguiente(nodo)
            nodo.setSiguiente(aux)
            self.__tope+=1
    
    def tipoPosicion(self,posicion):
        aux=self.__comienzo
        if posicion>=0 and (self.__tope==posicion==0 or posicion<self.__tope):
            if aux!=None:
                while self.__indice!=posicion:
                    aux=aux.getSiguiente()
                    self.__indice+=1
                if isinstance(aux.getDato(), VehiculoUsado):
                    print('TIPO DE OBJETO ES VEHICULOUSADO')
                elif isinstance(aux.getDato(), VehiculoNuevo):
                    print('TIPO DE OBJETO ES VEHICULONUEVO')
            else:
                print('LISTA VACIA')
        else:
            print('NO EXISTE LA POSICION {} EN LA LISTA ENLAZADA:'.format(posicion))
        self.__indice=0

    def modificarPrecio(self, patente):
        aux=self.__comienzo
        encontrado = False
        if aux==None:
            print('LISTA VACIA')
        elif isinstance(aux.getDato(), VehiculoUsado) and aux.getDato().getPatente().upper()==patente.upper():
            encontrado=True
        else:
            ant = aux
            aux = aux.getSiguiente()
            while not encontrado and aux != None:
                if isinstance(aux.getDato(), VehiculoUsado) and aux.getDato().getPatente().upper()==patente.upper():
                    encontrado=True
                else:
                    ant = aux
                    aux=aux.getSiguiente()
        if encontrado:
                precio=int(input('INDIQUE EL NUEVO PRECIO BASE:'))
                aux.getDato().setPrecio(precio)
                print('EL PRECIO DE VENTA DEL AUTO ES {} PESOS'.format(aux.getDato().importe()))
        else:
                print('El auto usado con patente {}, no está en la lista'.format(patente.upper()))
    
    def economico(self):
        print('-----------------------------------------------------')
        menor=None
        precio=10000000000
        if self.__tope!=0:
            for vehiculo in self:
                if vehiculo.importe()<precio:
                    menor=vehiculo
                    precio=vehiculo.importe()
            for vehiculo2 in self:
                if vehiculo2.importe()==precio:
                    print(vehiculo2)
                    print('IMPORTE:',precio)
                    print('-----------------------------------------------------')
        else:
            print('----NO HAY VEHICULOS CARGADOS----')   
            print('-----------------------------------------------------')
    
    def todos(self):
        print('-----------------------------------------------------')
        if self.__tope!=0:
            for vehiculo in self:
                print('MODELO:{}\tCANT.PUERTAS:{}\tIMPORTE:{}'.format(vehiculo.getModelo(),vehiculo.getCantPuertas(),vehiculo.importe()))
                print('-----------------------------------------------------')
        else:
            print('----NO HAY VEHICULOS CARGADOS----') 
    
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            vehiculos=[vehiculo.toJSON() for vehiculo in self]
                )
        return d  
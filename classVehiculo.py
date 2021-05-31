
class Vehiculo:
    __modelo=None
    __cantPuertas=0
    __color=''
    __precioBase=0
    
    def __init__(self,modelo,puertas,color,precio):
        self.__modelo=modelo
        self.__cantPuertas=puertas
        self.__color=color
        self.__precioBase=precio
    def __str__(self):
        return ('MOD:{}\tPUERTAS:{}\tCOLOR:{}\tPRECIO:{}'.format(self.__modelo,self.__cantPuertas,self.__color,self.__precioBase))
    def getModelo(self):
        return self.__modelo
    def getCantPuertas(self):
        return int(self.__cantPuertas)
    def getColor(self):
        return self.__color
    def getPrecio(self):
        return int(self.__precioBase)
    def setPrecio(self,precio):
        self.__precioBase=precio
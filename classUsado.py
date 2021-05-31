from classVehiculo import Vehiculo
from datetime import datetime
import json
from pathlib import Path
class VehiculoUsado(Vehiculo):
    __marca=''
    __patente=''
    __año=0
    __kilometraje=0
    
    def __init__(self, modelo,puertas,color,precio, marca,patente,año,km):
        super().__init__(modelo, puertas, color, precio)
        self.__marca=marca
        self.__patente=patente
        self.__año=año
        self.__kilometraje=km
    def __str__(self):
        ret1=('{}\n'.format(super().__str__()))
        ret2=('MARCA:{}\tPATENTE:{}\tAÑO:{}\tKM:{}'.format(self.__marca,self.__patente,self.__año,self.__kilometraje))
        return ret1+ret2
    def importe(self):
        fecha=datetime.now()
        antiguedad=fecha.year-self.__año
        return float(super().getPrecio()-(super().getPrecio()*(0.01*antiguedad)))
    def getPatente(self):
        return self.__patente
    def setPrecio(self,precio):
        if isinstance(precio, int):
            super().setPrecio(precio)

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(modelo=self.getModelo(),
                               patente=self.__patente,
                               puertas=int(self.getCantPuertas()),
                               color=self.getColor(),
                               precio=int(self.getPrecio()),
                               marca=self.__marca,
                               año=int(self.__año),
                               km=int(self.__kilometraje))
                )
        return d

        
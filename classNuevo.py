from classVehiculo import Vehiculo

class VehiculoNuevo(Vehiculo):
    marca='ford'
    __version=''
    
    def __init__(self, modelo,puertas,color,precio,version):
        super().__init__(modelo, puertas, color, precio)
        self.__version=version
    def __str__(self):
        ret1=('{}\n'.format(super().__str__()))
        ret2=('MARCA:{}\t\tVERSION:{}'.format(self.marca,self.__version))
        return ret1+ret2
    def importe(self):
        retorna=0.0
        if self.__version.upper()=='FULL':
            retorna=float(super().getPrecio()+(super().getPrecio()*0.1)+(super().getPrecio()*0.02))
        else:
            retorna=float(super().getPrecio()+(super().getPrecio()*0.1))
        return retorna
        
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(modelo=self.getModelo(),
                               puertas=int(self.getCantPuertas()),
                               color=self.getColor(),
                               precio=int(self.getPrecio()),
                               version=self.__version)
                )
        return d
    
    
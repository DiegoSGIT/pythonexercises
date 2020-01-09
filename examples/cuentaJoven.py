from cuenta import Cuenta

class CuentaJoven(Cuenta):

    def __init__(self, persona, cantidad, bonificacion):
        super().__init__(persona, cantidad)
        self.__bonificacion = bonificacion     

    def mostrar(self):
        super().mostrar()
        print('Bonificacion: {0}'.format(self.__bonificacion))

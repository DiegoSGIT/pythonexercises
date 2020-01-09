from persona import Persona
class Cuenta():
    def __init__(self, persona, cantidad = 0):
        self.__persona = persona
        self.__cantidad = cantidad

    def mostrar(self):
        self.__persona.mostrar()        
        print('Cantidad: {0}'.format(self.__cantidad))

    def ingresar(self, cantidad):
        self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad
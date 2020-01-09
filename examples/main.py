from persona import Persona
from cuenta import Cuenta
from cuentaJoven import CuentaJoven
""" Persona """

persona1 = Persona('Diego', 26, 'SAGD930714')
""" persona1.mostrar()
persona1.esMayorDeEdad() """

""" Cuenta """

""" cuenta1 = Cuenta(persona1)
cuenta1.mostrar()
cuenta1.ingresar(1000)
cuenta1.retirar(50)
cuenta1.mostrar() """

""" Cuenta Joven """


cuentajoven = CuentaJoven(persona1, 100, 15)
cuentajoven.mostrar()

class Persona():
	def __init__(self, nombre='', edad=0, dni=''):
		self.__nombre = nombre
		self.__edad = edad
		self.__dni = dni

	@property
	def nombre(self):
		print(self.__nombre)
	@nombre.setter
	def nombre(self, nombre):
		self.__nombre = nombre
	@property
	def edad(self):
		print(self.__edad)
	@edad.setter
	def edad(self, edad):
		self.__edad = edad
	@property
	def dni(self):
		print(self.__dni)
	@dni.setter
	def dni(self, dni):
		self.__dni = dni

	def mostrar(self):
		print('Nombre: {0}'.format(self.__nombre))
		print('Edad: {0}'.format(self.__edad))
		print('DNI: {0}'.format(self.__dni))

	def esMayorDeEdad(self):
		if self.__edad >= 0:
			print('Es mayor de edad')
		else: 
			print('No es mayor de edad')

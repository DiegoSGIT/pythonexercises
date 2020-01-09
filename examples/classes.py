class Moto():
	""" Atributos __init__ constructor"""
	def __init__(self, marca, serie):
		self.marca = marca
		self.__serie = serie
		print('Objecto Creado')
	
	""" Metodos """
	def acelerar(self):
		print('La moto {0} esta acelerando'.format(self.marca))

	def frenar(self):
		print('La moto {0} se ha detenido'.format(self.marca))

	def getSerie(self):
		print('Serie: {0}'.format(self.__serie))



moto = Moto('vento', 'ASKDCKD')
moto.acelerar()
moto.frenar()
print(moto.getSerie())

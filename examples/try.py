while True:
	try:
		a = int(input('Introduce un numero: '))
		break
	except ValueError:
		print('Necesitas ingresar un numero: ')

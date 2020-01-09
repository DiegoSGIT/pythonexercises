numero = int(input('numero: '))
def factorial(num):
	fact = 1
	if num != 1:
		 fact = factorial(num-1)
	return num * fact
		
	
print(factorial(numero))

import math

numero = int (input('numero a valorar: '))
sqrt = int(math.sqrt(numero))
primo = True
for _ in range(2, sqrt + 1, 1):
	print('divisor: ', _)
	print('res: ', numero % _)
	if numero % _ == 0:
		primo = False
if primo:
	print('primo')
else:
	print('No primo')
	

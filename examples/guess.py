from random import randint

number = randint(1,100)
tries = 10

guess = int(input('guess: '))
while number != guess:
	if guess > number:
		print('menor')	
	else:
		print('mayor')
	if tries == 0:
		break
	tries -= 1
	guess = int(input('guess: '))
	

print('Intentos: ', 10-tries)
print('Numero: ', number)

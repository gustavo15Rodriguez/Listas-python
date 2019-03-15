#-*-coding:utf-8-*-

'''4. Cargar una lista de 10 posiciones con los 10 primeros elementos de la serie de Fibonacci y
mostrarlo en pantalla.'''

try:
	lista =[]
	lista2 = []

	num = 1 
	penultimo = 0
	ultimo = 0

	for i in range(10):
		penultimo = ultimo
		ultimo = num
		num = penultimo + ultimo
		lista.append(num)

	for j in range(10):
		lista2 = lista

	print "Los 10 primeros elementos de la serie Fibonacci son: ", lista2

except ValueError:
	print "Error..."
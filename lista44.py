#-*-coding:utf-8-*-

'''44. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos de los números
almacenados en dicha lista pertenecen a los 100 primeros elementos de la serie de Fibonacci. '''

try:
	lista =[]
	lista2 = []
	
	for i in range(10):
		numero =int(raw_input("Digite el numero deseado: "))
		lista.append(numero)

	cont = 0
	for j in range(len(lista)):
		numero = lista[j]
	
		num = 1
		ultimo = 0
		penultimo = 0
		
		for k in range(100):
			penultimo = ultimo
			ultimo = num
		
			num = penultimo + ultimo
			if numero == num:
				cont +=1

	print "Hay %d numeros que pertenecen a la serie Fibonacci."%cont









except ValueError:
	print "Error..."
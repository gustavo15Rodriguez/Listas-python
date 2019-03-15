#-*-coding:utf-8-*-

'''26. Leer 10 números enteros, almacenarlos en una lista y calcularle el factorial a cada uno de
los números leídos almacenándolos en otra lista. '''

try:
	lista = [] 
	fac =[]

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	for j in range (len(lista)):
		var = lista[j]
		factorial = 1

		for k in range(1,var+1):
			factorial = factorial * k

		fac.append(factorial)

	print "Los factoriales de los numeros almacenados en la lista anterior son: ", fac


except ValueError:
	print "Error..."

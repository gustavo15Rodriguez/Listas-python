#-*-coding:utf-8-*-

'''27. Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el
promedio entero de los factoriales de cada uno de los números leídos. '''

try:
	lista = []
	factor =[]
	prom = 0
	suma = 0

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	for j in range (len(lista)):
		var = lista[j]
		factorial = 1

		for k in range(1,var+1):
			factorial = factorial * k
		
		factor.append(factorial)

	cont = 0
	for l in range(len(factor)):
		g = factor[l]
		suma+=g
		cont+=1

	prom = suma/cont

	print "Los factoriales de los numeros ingresados son: ", factor

	print "El promedio de los factoriales en la lista anterior es: %d"%prom

except ValueError:
	print "Error..."


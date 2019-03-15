#-*-coding:utf-8-*-

'''12. Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el
promedio entero de los datos de la lista.'''

try:
	lista =[]
	suma = 0
	prom = 0

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)
		suma+=num

	prom = suma/i

	print "El promedio entero de los datos de la lista es igual a %d."%prom


except ValueError:
	print "Error..."


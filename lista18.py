#-*-coding:utf-8-*-

'''18. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones están
los números positivos.'''

try:
	lista =[]
	lista2 = []
	pos = 0

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	cont = 0
	for j in range(len(lista)):
		if lista[j] > 0:
			pos = j
			lista2.append(pos)

	print "Los numeros positivos de la lista estan en las siguientes posiciones: ", lista2

except ValueError:
	print "Error..."

#-*-coding:utf-8-*-

'''1. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de la lista está el
mayor número leído.'''

try:
	lista =[]
	pos = 0

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	mayor =  lista[0]

	for j in range(len(lista)):
		if lista[j] > mayor:
			mayor = lista[j]
			pos = j

	print "El numero mayor de la lista que es mayor %d se encuentra en la posicion %d"%(mayor, pos)



except ValueError:
	print "Error..."
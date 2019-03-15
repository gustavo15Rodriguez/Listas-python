#-*-coding:utf-8-*-

'''17. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números
negativos hay.'''

try:
	lista =[]
	lista2 = []

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

		cont = 0

	for j in range(len(lista)):
		if lista[j] < 0:
			cont+=1
			lista2.append(lista[j])

	print "Hay %d"%cont + " numeros que son negativos, los cuales son: ", lista2


except ValueError:
	print "Error..."

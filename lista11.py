#-*-coding:utf-8-*-

'''11. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números
tienen, de los almacenados allí, menos de 3 dígitos.'''

try:
	lista =[]
	cont = 0

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	for j in range(len(lista)):
		if lista[j] < 100:
			cont+=1
	print lista
	print "\n"
	print "Hay %d numeros que tienen menos de 3 digitos."%cont


except ValueError:
	print "Error..."


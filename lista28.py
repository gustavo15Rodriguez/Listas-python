#-*-coding:utf-8-*-

'''28. Leer 10 números enteros, almacenarlos en una lista y mostrar en pantalla todos los
enteros comprendidos entre 1 y cada uno de los números almacenados en la lista.'''

try:
	lista =[]

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)


	for j in range(len(lista)):
		numero = lista[j]
		if numero == 1 or numero == 2:
			print "No hay numeros comprendidos entre 1 y %d"%numero

		else:
			print "Los numeros comprendidos entre 1 y %d son: "%numero
			for k in range (1,numero):
				print k

except ValueError:
	print "Error..."
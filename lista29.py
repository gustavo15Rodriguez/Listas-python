#-*-coding:utf-8-*-

'''29. Leer 10 números enteros, almacenarlos en una lista y mostrar en pantalla todos los
enteros comprendidos entre 1 y cada uno de los dígitos de cada uno de los números
almacenados en la lista.'''

try:
	lista = []

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	for j in range(len(lista)):
		numero = lista[j]

		while numero > 0:
			dig = numero % 10
			numero = numero / 10

			if dig == 1 or dig == 2:
				print "No hay numeros comprendidos entre 1 y %d."%dig

			else:
				print "Los numeros comprendidos entre 1 y %d son: "%dig

				for k in range(1, dig):
					print k


except ValueError:
	print "Error..."
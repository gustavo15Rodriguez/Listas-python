#-*-coding:utf-8-*-

'''224. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición está el
número con más dígitos.'''

try:
	lista =[]
	lista2=[]
	cont = 0
	pos = 0
	mayor = 0


	for i in range(10):
		numero = int(raw_input("Digite los numeros deseados: "))
		lista.append(numero)

	for j in range(len(lista)):
		numero = lista[j]
		cont=0
		while numero > 0:
			numero = numero//10
			cont += 1

		if cont>mayor:
			mayor = cont
			pos = j
	
	print "El numero con la mayor cantidad de digitos esta en la posicion %d de la lista."%pos



	

except ValueError:
	print "Error..."

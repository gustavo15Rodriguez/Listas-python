#-*-coding:utf-8-*-

'''23. Leer 10 números enteros, almacenarlos en una lista y determinar si existe al menos un
número repetido.'''

try:
	lista =[]
	lista2 = []

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	for k in range(len(lista)):
		cont = 0
		var = lista[k]

		
		for j in range(len(lista)):
			if var == lista[j]:
				cont+=1
				lista2.append(num)

		if cont > 1:
			break	

	if cont > 1:
		print "Hay por lo menos 1 numero repetido en la lista."

	else:
		print "No hay ni un numero repetido en la lista."


except ValueError:
	print "Error..."
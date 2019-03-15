#-*-coding:utf-8-*-

'''3. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de la lista está el
mayor número primo leído.'''

try:
	lista =[]
	var = 0
	pos = 0
	mayor = 0
	
	

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num) 


	for j in range(len(lista)):
		num = lista[j]

		cont = 0


		for k in range(1,num+1):
			if num%k == 0:
				cont+=1

		if cont == 2:
			var = num

			if var > mayor:
				mayor = var
				pos = j

	print "El numero primo mayor es %d."%mayor
	print "El numero primo mayor esta en la posicion %d de la lista."%pos
	



except ValueError:
	print "Error..."
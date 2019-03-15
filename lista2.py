#-*-coding:utf-8-*-

'''2. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de la lista está el
mayor número par leído. '''

try:
	lista =[]
	pares = []
	pos = []

	for i in range(5):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	
	cont = 0

	for j in range(len(lista)):
		par = lista[j]

		if par%2 == 0:
			pares.append(par)
			cont+=1
			
			
	mayor =  pares[0]
	for k in range(len(pares)):
		if pares[k] > mayor:
			mayor = pares[k]

	for l in range(len(lista)):
		if mayor == lista[l]:
			pos.append(l)
	
	print pares

	print "El numero par mayor de la lista que es %d"%mayor + " se encuentra en la posicion", pos

except ValueError:
	print "Error..."
#-*-coding:utf-8-*-

'''21. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición está el
número cuya suma de dígitos sea la mayor.'''

try:
	lista =[]
	mayor = 0
	pos = 0

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)



	for j in range(len(lista)):
		num = lista[j]
		suma = 0
		
		while num !=0:
			dig = num %10
			suma = suma+dig
			num = num // 10

		if suma > mayor:
			mayor = suma
			pos = j

	
	print "El numero cuya suma de digitos es mayor esta en la posicion %d."%pos


except ValueError:
	print "Error..."
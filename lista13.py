#-*-coding:utf-8-*-

'''13. Leer 10 números enteros, almacenarlos en una lista y determinar si el promedio entero
de estos datos está almacenado en la lista.'''

try:
	lista =[]
	suma = 0
	prom = 0
	cont = 0

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)
		suma += num

	prom = suma/i

	for j in range(len(lista)):
		if lista[j] == prom:
			cont +=1


	if cont == 0:
		print "El promedio no esta almacenado en la lista original."

		
	else:
		print "El promedio que es %d, si esta almacenado en la lista."%prom


except ValueError:
	print "Error..."


#-*-coding:utf-8-*-

'''35. Leer 10 números enteros, almacenarlos en una lista y determinar si el promedio entero
de dichos números es un número primo.'''

try:
	lista =[]
	suma = 0
	prom = 0
	cont = 0

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)
		suma+=num
		cont+=1
		prom = suma/cont

		cont2 = 0
	
	for j in range(1,prom+1):
		if prom%j==0:
			cont2 += 1	

	if cont2 == 2:
		print "El promedio que es %d si es un numero primo."%prom

	else:
		print "El promedio de la lista anterior no origina un numero primo."



except ValueError:
	print "Error..."
#-*-coding:utf-8-*-

'''43. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se
encuentra el número con mayor cantidad de dígitos primos.'''

try:
	lista =[]
	primos = []
	lista3=[]
	pos = 0

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	for j in range(len(lista)):
		num = lista[j]
		cont = 0

		while num > 0:
			dig = num%10
			if dig == 2 or dig == 3 or dig == 5 or dig == 7:
				cont+=1
			num = num//10

		primos.append(cont)

	mayor = primos[0]

	for k in range(len(primos)):
		if primos[k] > mayor:
			mayor = primos[k]
			pos = k

	print "El numero con la mayor cantidad de digitos primos esta en la posicion %d."%pos

except ValueError:
	print "Error..."
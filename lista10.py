#-*-coding:utf-8-*-

'''10. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se
encuentran los números con más de 3 dígitos. '''

try:
	lista =[]
	lista_mayor = []
	pos = 0
	

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)


	for j in range(len(lista)):
		num = lista[j]
		cont = 0
		n = 0

		while num > n:
			num = num//10
			cont +=1

		if cont > 3:
			pos = num
			lista_mayor.append(j)

	print "Los numeros con mas de tres digitos estan en las posiciones: ", lista_mayor


except ValueError:
	print "Error..."


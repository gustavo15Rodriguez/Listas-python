#-*-coding:utf-8-*-

'''47. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se
encuentran los números múltiplos de 10. No utilizar el número 10 en ninguna operación. '''

try:
	lista =[]
	pos = []

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	mult = 5*2

	for j in range(len(lista)):
		var = lista[j]
		if var%mult == 0:
			pos.append(j)


	print "Los numeros multipos de 10 estan en las posiciones:", pos


except ValueError:
	print "Error..."
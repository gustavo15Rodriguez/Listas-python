#-*-coding:utf-8-*-

'''30. Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar si
este último entero se encuentra entre los 10 valores almacenados en la lista.'''

try:
	lista = []
	cont = 0

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	num2 = int(raw_input("Digite el numero a evaluar: "))


	for j in range(len(lista)):
		if lista[j] == num2:
			cont+=1


	if cont == 0:
		print "El numero evaluado no se encuentra en la lista anterior."

	else:
		print "El numero evaluado si se encuentra en la lista anterior."

except ValueError:
	print "Error..."
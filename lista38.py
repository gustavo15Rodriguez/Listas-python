#-*-coding:utf-8-*-

'''38. Leer 10 números enteros, almacenarlos en una lista y determinar si la semisuma entre el
valor mayor y el valor menor es un número primo. '''

try:
	lista =[]
	suma = 0

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	mayor = lista[0]
	menor = lista[0]

	for j in range(len(lista)):
		if lista[j] > mayor:
			mayor = lista[j]

		if lista[j] < menor:
			menor = lista[j]

	suma = mayor + menor

	cont = 0
	for k in range(1, suma+1):
		if suma%k == 0:
			cont+=1

	if cont == 2:
		print "El resultado de la semisuma origina un numero primo."

	else:
		print "El resultado de la semisuma no origina un numero primo."

except ValueError:
	print "Error..."
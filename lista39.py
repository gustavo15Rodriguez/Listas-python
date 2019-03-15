#-*-coding:utf-8-*-

'''39. Leer 10 números enteros, almacenarlos en una lista y determinar si la semisuma entre el
valor mayor y el valor menor es un número par.'''

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

	if suma%2 == 0:
		print "La semisuma realizada si origina un numero par."

	else:
		print "La semisuma no origina un numero par."

except ValueError:
	print "Error..."
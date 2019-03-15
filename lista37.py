#-*-coding:utf-8-*-

'''37. Leer 10 números enteros, almacenarlos en una lista y determinar a cuántos es igual el
cuadrado de cada uno de los números leídos. '''

try:
	lista =[]
	lista_cuadrado= []

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	cuadrado = 0

	for j in range(len(lista)):
		num = lista[j]
		cuadrado = num ** 2
		lista_cuadrado.append(cuadrado)

	print "El cuadrado de cada uno de los numeros leidos es: ", lista_cuadrado

except ValueError:
	print "Error..."
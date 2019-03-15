#-*-coding:utf-8-*-

'''19. Leer 10 números enteros, almacenarlos en una lista y determinar cuál es el número
menor.'''

try:
	lista =[]

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	menor = lista[0]

	for j in range(len(lista)):
		if lista[j] < menor:
			menor = lista[j]

	print "El numero menor de la lista anterior es: %d"%menor



except ValueError:
	print "Error..."

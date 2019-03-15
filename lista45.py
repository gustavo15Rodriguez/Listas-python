#-*-coding:utf-8-*-

'''45. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los
almacenados en dicha lista comienzan por 34.'''

try:
	lista =[]
	cont = 0

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	for j in range(len(lista)):
		num = lista[j]
		while num > 0:
			dig = num % 10
			if num == 34:
				cont+=1

			num = num//10


	print "Hay %d numeros que empiezan por 34."%cont 


except ValueError:
	print "Error..."
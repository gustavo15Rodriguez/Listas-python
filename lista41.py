#-*-coding:utf-8-*-

'''41. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los
almacenados en dicha lista comienzan con 3.'''

try:
	lista =[]
	lista2 = []

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	cont = 0
	for j in range(len(lista)):
		num = lista[j]
		while num > 0:
			if num == 3:
				cont+=1
			
			num = num/10

	if cont > 0:		
		print "Hay %d numeros que empiezan por 3."%cont

	else:
		print "No hay numeros que empiezen por 3."


except ValueError:
	print "Error..."
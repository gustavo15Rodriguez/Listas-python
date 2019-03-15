#-*-coding:utf-8-*-

'''40. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los
almacenados en dicha lista terminan en 15.'''

try:
	lista = []
	
	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	cont = 0
	for j in range(len(lista)):
		if lista[j]%100== 15:
			cont+=1
		
	print "Hay %d numeros que terminan en 15."%cont 


except ValueError:
	print "Error..."
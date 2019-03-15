#-*-coding:utf-8-*-

'''50. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los
almacenados en dicha lista comienzan en dígito primo.'''

try:
	lista =[]
	cont2 = 0

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	for j in range(len(lista)):
		num = lista[j]

		cont = 0
		mayor = 0

		while num > 0:
			var = num%10
			if var > 0:
				mayor = var 

			num = num//10

		for i in range(1, mayor+1):
			if mayor%i==0:
				cont+=1

		if cont == 2:
			cont2+=1

	print "Hay %d numeros que empiezan por digito primo."%cont2

except ValueError:
	print "Error..."
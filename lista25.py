#-*-coding:utf-8-*-

'''25. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos de los números
leídos son números primos terminados en 3.'''

try:
	lista = []
	lista_primo = []
	primos = 0
	primo = []
	
	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	for j in range(len(lista)):
		primos = lista[j]

		cont = 0

		for k in range(1,primos+1):
			if primos%k == 0:
				cont+=1

		if cont == 2:
			lista_primo.append(primos)

	for l in range(len(lista_primo)):
		if lista_primo[l]%10==3:
			primo.append(lista_primo[l])
	
	print "Los numeros primos terminados en 3 son: ", primo


except ValueError:
	print "Error..."

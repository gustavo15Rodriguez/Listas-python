#-*-coding:utf-8-*-

'''5. Almacenar en una lista de 10 posiciones los 10 números primos comprendidos entre 100 y
300. Luego mostrarlos en pantalla. '''

try:
	lista =[]
	lista_primos = []
	primos = 0

	for i in range(100,301):
		lista.append(i)

	for j in range(len(lista)):
		primos = lista[j]

		cont = 0

		for k in range(1,primos+1):
			if primos % k == 0:
				cont+=1
		
		if cont == 2:
			lista_primos.append(primos)

	print "Los numeros primos comprendidos entre 100 y 300 son: ", lista_primos

except ValueError:
	print "Error..."
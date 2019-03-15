#-*-coding:utf-8-*-

'''20. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición está el
menor número primo.'''

try:
	lista =[]
	var = 0
	pos = []
	primos = []
	
	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	for j in range(len(lista)):
		num = lista[j]
		cont = 0
	

		for k in range(1,num+1):
			if num%k == 0:
				cont+=1

		if cont == 2:
			primos.append(num)

	menor = primos[0]

	for l in range(len(primos)):
		if primos[l] < menor:
			menor = primos[l]

	for m in range(len(lista)):
		if menor == lista[m]: 
			pos.append(m)
	
	print "El numero primo menor es %d"%menor +  " y se encuentra en la posicion.", pos

except ValueError:
	print "Error..."

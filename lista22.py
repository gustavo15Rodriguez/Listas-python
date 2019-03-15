#-*-coding:utf-8-*-

'''22. Leer 10 números enteros, almacenarlos en una lista y determinar cuáles son los números
múltiplos de 5 y en qué posiciones están. '''

try:
	lista =[]
	lista2 = []
	lista3 = []
	pos = 0

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	for j in range(len(lista)):
		if lista[j]%5==0:
			lista2.append(lista[j])
			pos = j
			lista3.append(pos)
	
	print "los numeros multiplos de 5 son: ", lista2
	print "Y se encuentran en las siguientes posiciones: ", lista3

except ValueError:
	print "Error..."

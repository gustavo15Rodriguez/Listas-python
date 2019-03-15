#-*-coding:utf-8-*-

'''9. Leer 10 números enteros, almacenarlos en una lista y determinar cuántas veces está
repetido el mayor. '''

try:
	lista =[]
	cont = 0
	
	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	mayor = 0
	
	for j in range(len(lista)):
		if lista[j] > mayor:
			mayor = lista[j]

	for k in range(len(lista)):
		if mayor == lista[k]:
			cont+=1
			
	print "El numero mayor que es %d,  esta %d veces."%(mayor, cont)


except ValueError:
	print "Error..."

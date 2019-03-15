#-*-coding:utf-8-*-

'''14. Leer 10 números enteros, almacenarlos en una lista y determinar cuántas veces se repite
el promedio entero de los datos dentro de la lista.'''

try:
	lista =[]
	suma = 0
	prom = 0
	cont = 0

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)
		suma+=num
	prom = suma/i

	for j in range(len(lista)):
		if prom == lista[j]:
			cont +=1
	
	print "El promedio que es %d, se repite %d veces dentro de la lista."%(prom, cont)

except ValueError:
	print "Error..."

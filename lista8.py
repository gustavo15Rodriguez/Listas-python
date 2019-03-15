#-*-coding:utf-8-*-

'''8. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se
encuentran los números terminados en 4.'''

try:
	lista =[]
	ter = 0
	pos = []
	

	for i in range(5):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	mayor = 0
	cont = 0

	for j in range(len(lista)):
		ter = lista[j]

		if ter%10==4:
			pos.append(j)

	print "Los numeros terminados en 4 estan en las posiciones: ", pos 

except ValueError:
	print "Error..."
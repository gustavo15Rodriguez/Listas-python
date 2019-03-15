#-*-coding:utf-8-*-

'''7. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se
encuentra el número mayor.'''

try:
	lista = []
	lista_pos = []
	mayor = 0 
	pos = 0
	

	for i in range(5):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	for j in range(len(lista)):
		if lista[j] > mayor:
			mayor = lista[j]

	for k in range(len(lista)):
		if lista[k] == mayor:
			lista_pos.append(k)

	print "El mayor numero leido se encuentra en la(s) posicion(es)", lista_pos


except ValueError:
	print "Error..."
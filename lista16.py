#-*-coding:utf-8-*-

'''16. Leer 10 números enteros, almacenarlos en una lista y determinar cuáles son los datos
almacenados múltiplos de 3.'''

try:
	lista =[]
	datos = []

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	cont = 0

	for j in range(len(lista)):
		if lista[j]%3==0:
			cont+=1
			datos.append(lista[j])

	print "Los datos almacenados en la lista que son multiplos de 3 son: ", datos

except ValueError:
	print "Error..."

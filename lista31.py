#-*-coding:utf-8-*-

'''31. Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar
cuántos divisores exactos tiene este último número entre los valores almacenados en la lista.'''

try:
	lista = []
	cont = 0

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	num2 = int(raw_input("Digite el numero a evaluar: "))

	for j in range(len(lista)):
		var = lista[j]
		if var%num2 == 0:
			cont+=1
	print "El numero a evaluar que es %d tiene %d divisores exactos."%(num2, cont)

except ValueError:
	print "Error..."
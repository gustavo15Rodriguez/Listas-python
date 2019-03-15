#-*-coding:utf-8-*-

'''33. Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual la
suma de los dígitos pares de cada uno de los números leídos. '''

try:
	lista = []
	sumas = []

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	for j in range(len(lista)):
		num=lista[j]

		suma = 0
		while num>0:
			dig=num%10
			
			if dig % 2 ==0:
				suma+=dig

			num=num/10


		sumas.append(suma)

	for k in range(len(sumas)):
		if sumas[k] != 0:
			print "La suma de los digitos pares del numero %d es %d"%(lista[k], sumas[k])

		else:
			print "El numero %d no tiene digitos pares"%lista[k]


except ValueError:
	print "Error..."
#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y 
determinar en qué posición se encuentra el número primo con mayor cantidad de dígitos pares.'''

try:

	lista=[]
	primos = []
	num = 0
	contador = 0
	digitos = 0
	mayor = 0
	num_mayor = 0
	posicion = 0
	
	

	for i in range(5):
		numero = int(raw_input("Favor ingrese un numero: "))
		lista.append(numero)

	for j in range(len(lista)):
		num = lista[j]
		contador = 0

		for k in range(1,num+1):
			if num % k == 0:
				contador+=1

		if contador == 2:
			primos.append(num)


	for l in range(len(primos)):
		num = primos [l]
		contador = 0

		while num > 0:
			digitos = num % 10

			if digitos % 2 == 0 :
				contador+=1


			if contador >= mayor:
				mayor = contador
				posicion = l

			num = num / 10



	if len(primos) != 0:

		for m in range(posicion+1):
			num_mayor = primos [m]

		for l in range (len(lista)):
			if num_mayor == lista[l]:
				posicion = l

		print "EL numero primo con mayor cantidad de digitos pares es %d"%num_mayor +" tiene en total %d"%mayor +" digitos y esta en la posicion %d"%posicion +" de la lista"

	else:
		print "No hay ningun numero primo que tenga digitos pares en la lista"

except ValueError:
	print "Error los datos ingresados deben ser numeros"
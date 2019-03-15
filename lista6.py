#-*-coding:utf-8-*-

'''6. Leer dos números enteros y almacenar en una lista los 10 primeros números primos
comprendidos entre el menor y el mayor. Luego mostrarlos en pantalla. '''

try:
	lista1 =[]
	lista2 =[]

	num1 = int(raw_input("Digite el primer numero: "))
	num2 = int(raw_input("Digite el segundo numero: "))


	if num1 > num2:

		for i in range(num2, num1+1):
			lista1.append(i)


		for j in range(len(lista1)):
			num = lista1[j]

			cont = 0

			for k in range(1,num+1):
				if num%k == 0:
					cont+=1

			if cont == 2:
				lista2.append(num)

	elif num2 > num1:

		for i in range(num1, num2+1):
			lista1.append(i)


		for j in range(len(lista1)):
			num = lista1[j]

			cont = 0

			for k in range(1,num+1):
				if num%k == 0:
					cont+=1

			if cont == 2:
				lista2.append(num)

	print "Los numeros primos comprendidos entre %d y %d"%(num1, num2) + " son: ",lista2

except ValueError:
	print "Error..."
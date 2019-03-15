#-*-coding:utf-8-*-

'''36. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos dígitos primos
hay en los números leídos.'''

try:
	lista = []
	primos = []
	cont2 = 0

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	for j in range(len(lista)):
		num=lista[j]

		
		while num>0:
			dig=num%10
			cont = 0

			for l in range(1, dig+1):
				if dig%l==0:
					cont+=1

			if cont == 2:
				cont2+=1
				primos.append(dig)
			num = num//10

	if cont2!=0:
		print "De los numeros anteriores, hay %d digitos primos."%cont2 + " los cuales son:", primos

	else:
		print "No hay digitos primos en la lista."
	
except ValueError:
	print "Error..."
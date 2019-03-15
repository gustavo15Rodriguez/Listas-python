#-*-coding:utf-8-*-

'''49. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números
terminan en dígito primo.'''

try:
	lista =[]
	cont2 = 0

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)


	for j in range(len(lista)):
		num = lista[j]
		dig = num%10

		cont = 0
		
		
		for k  in range(1, dig+1):
			if dig%k == 0:
				cont+=1
	
		if cont == 2:
			cont2+=1

	print "Hay %d numeros que terminan en digito primo."%cont2

except ValueError:
	print "Error..."
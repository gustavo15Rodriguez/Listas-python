#-*-coding:utf-8-*-

'''34. Leer 10 números enteros, almacenarlos en una lista y determinar cuántas veces en la lista
se encuentra el dígito 2. No se olvide que el dígito 2 puede estar varias veces en un mismo
número. '''

try:
	lista = []
	contador = []
	

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	for j in range(len(lista)):
		num=lista[j]

		cont = 0
		while num>0:
			dig=num%10
			
			if dig % 10 ==2:
				cont+=1

			num=num/10

		contador.append(cont)

	for k in range(len(contador)):
		if contador[k] != 0:
			print "El numero %d tiene el digito dos %d veces"%(lista[k], contador[k])

		else:
			print "El numero %d no tiene el digito 2."%lista[k]

except ValueError:
	print "Error..."
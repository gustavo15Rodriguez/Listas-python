#-*-coding:utf-8-*-

'''46. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los
almacenados en dicha lista son primos y comienzan por 5.'''

try:
	lista =[]
	primos = []
	primo = []

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	for g in range(len(lista)):
		num=lista[g]

		cont = 0
		for j in range(1, num+1):
			if (num%j) == 0:
				cont += 1

		if cont == 2:
			primos.append(num)

	cont2= 0
	for k in range(len(primos)):
		num = primos[k]
		while num > 0:
			dig = num%10

			if num == 5:
				primo.append(num)
				cont2+=1

			num = num//10

	print "Hay %d numeros primos que empiezan por 5."%cont2

except ValueError:
	print "Error..."
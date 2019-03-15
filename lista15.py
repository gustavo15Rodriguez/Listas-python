#-*-coding:utf-8-*-

'''15. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos datos
almacenados son múltiplos de 3.'''

try:
	lista =[]

	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

		cont = 0

		for j in range(len(lista)):
			if lista[j]%3==0:
				cont+=1
				
	print "Hay %d multiplos de 3 en la lista anterior."%cont

except ValueError:
	print "Error..."

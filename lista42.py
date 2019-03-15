#-*-coding:utf-8-*-

'''42. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números con
cantidad par de dígitos pares hay almacenados en dicha lista.'''

try:
	lista =[]
	lista2=[]


	for i in range(10):
		num = int(raw_input("Digite los numeros deseados: "))
		lista.append(num)

	for j in range(len(lista)):
		var = lista[j]

		contador=0

		while var>0:
			digito=var%10	
			contador+=1
			var=var//10
		lista2.append(contador)

	cont = 0
		
	for k in range(len(lista2)):
		if lista2[k]%2==0:
			cont+=1	

	print "Hay %d numeros con cantidad par de digitos."%cont


except ValueError:
	print "Error..."